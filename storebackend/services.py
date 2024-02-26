import yaml
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response

from storebackend.models import Shop, ProductInfo, Category, Product, Parameter, ProductParameter, User, \
    ConfirmEmailToken
from storebackend.serializers import UserSerializer


def read_yaml_write_to_db(request, *args, **kwargs) -> Response:
    """
    Прочитать yaml файл и выполнить запись в базу данных
    """

    #  !!!!!!!!!!!!!! Добавить владельца магазина после аутентификации

    categories_created = 0
    categories_updated = 0
    products_created = 0
    products_updated = 0
    parameters_created = 0
    parameters_updated = 0

    try:
        import_file = request.FILES['upload_file'].file.read()
        import_data = yaml.load(import_file, Loader=yaml.FullLoader)
    except Exception as error:
        return error_prompt(False, "File didn't load", 400)
    #  Записать/обновить данные по магазину
    #  Магазин
    if type(import_data['shop']) is not str:
        return error_prompt(False, f"File didn't load. More than one shop", 400)
    shop, status_result = Shop.objects.get_or_create(name=import_data['shop'], user_id=request.user.id)
    shop_name_db = shop.name
    if not status_result:
        if shop.user_id == request.user.id:
            ProductInfo.objects.filter(shop_id=shop.id).delete()
        else:
            return error_prompt(False, f"File didn't load. "
                                       f'Authentification problem for {shop_name_db}', 403)
    #  Категории товаров
    for category in import_data['categories']:
        try:
            category_current, status_result = Category.objects.get_or_create(id=category['id'], name=category['name'])
            category_current.shops.add(shop.id)
            category_current.save()
            if status_result:
                categories_created += 1
            else:
                categories_updated += 1
        except Exception as error:
            return error_prompt(False, "File didn't load. Category id and name problem",
                                400)

    #  Товары
    for product in import_data['products']:
        try:
            product_current, status_result = Product.objects.get_or_create(
                name=product['name'],
                category_id=product['category'])
            if status_result:
                products_created += 1
            else:
                products_updated += 1
            product_info = ProductInfo.objects.create(product_id=product_current.id,
                                                      shop_id=shop.id,
                                                      external_id=product['id'],
                                                      model=product['model'],
                                                      price=product['price'],
                                                      price_rrc=product['price_rrc'],
                                                      quantity=product['quantity'])
            #  Параметры товаров
            for name, value in product['parameters'].items():
                parameter_current, status_result = Parameter.objects.get_or_create(name=name)
                if status_result:
                    parameters_created += 1
                else:
                    parameters_updated += 1
                ProductParameter.objects.create(product_info_id=product_info.id,
                                                parameter_id=parameter_current.id,
                                                value=value)
        except Exception as error:
            return error_prompt(False, f"File didn't load. Product's problem: {product}",
                                400)

    return Response({'Status': True,
                     'description': f'shop: {shop_name_db}, '
                                    f'categories_created: {categories_created}, '
                                    f'categories_updated: {categories_updated}, '
                                    f'products_created: {products_created}, '
                                    f'products_updated: {products_updated}, '
                                    f'parameters_created: {parameters_created}, '
                                    f'parameters_updated: {parameters_updated}'
                     },
                    status=201)


def create_user_data(request, *args, **kwargs) -> Response:
    """
    Создать пользователя в базе данных и направить токен по почте
    """
    user_data = {'email': '',
                 'password': '',
                 'company': '',
                 'position': '',
                 'username': '',
                 'type': '',
                 'first_name': '',
                 'last_name': ''}
    try:
        for key, value in user_data.items():
            if user_data['email']:
                if User.objects.filter(email=user_data['email']).exists():
                    return error_prompt(False, f'User already exists', 400)
            if user_data['password']:
                validate_password(user_data['password'])
            user_data[key] = request.data[key]

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user_data['password'])
            user.save()
        else:
            return error_prompt(False, f'Please check: {user_serializer.errors}', 400)
    except Exception as error:
        return error_prompt(False, f'Please check: {error}', 400)

    email_confirmation = user_data['email']
    return Response({'Status': True,
                     'description': f'Thank you for registration. Please, check your email:{email_confirmation} and '
                                    f'confirm your registration'
                     },
                    status=201)


def confirm_user_email(request, *args, **kwargs) -> Response:
    """
    Активировать пользователя в базе данных
    """
    try:
        email_confirmation = request.data['email']
        token = ConfirmEmailToken.objects.filter(user__email=email_confirmation,
                                                 key=request.data['token']).first()
        token.user.is_active = True
        token.user.save()
        token.delete()
        return Response({'Status': True,
                         'description': f'Your email:{email_confirmation} has been confirmed. Please, get your '
                                        f'access and refresh tokens via link webstore_python/token/'}, status=201)
    except Exception as error:
        return error_prompt(False, f'Please check: {error}', 400)


def error_prompt(status_data: bool, error_data: str, code_data: int) -> Response:
    """
    Вернуть сообщение об ошибке
    """
    return Response({'Status': status_data, 'Error': error_data}, status=code_data)
