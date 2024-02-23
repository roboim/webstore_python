import yaml
from rest_framework.response import Response

from storebackend.models import Shop, ProductInfo, Category


def read_yaml_write_to_db(request, *args, **kwargs) -> Response:
    """
    Прочитать yaml файл и выполнить запись в базу данных
    """
    categories_created = 0
    categories_updated = 0
    products_created = 0
    products_updated = 0

    try:
        import_file = request.FILES['upload_file'].file.read()
        import_data = yaml.load(import_file, Loader=yaml.FullLoader)
    except Exception as error:
        return error_prompt(False, "File didn't load", 400)
    #  Записать/обновить данные по магазину

    #  !!!!!!!!!!!!!! Добавить владельца магазина после аутентификации
    #  Магазин
    if type(import_data['shop']) is not str:
        return error_prompt(False, f"File didn't load. More than one shop", 400)
    shop, status_result = Shop.objects.get_or_create(name=import_data['shop'])  # , user_id=request.user.id)
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
            if status_result:
                categories_created += 1
            else:
                categories_updated += 1
        except Exception as error:
            return error_prompt(False, "File didn't load. Category id and name problem",
                                400)
    print(shop, status_result)

    return Response({'Status': True,
                     'description': f'shop: {shop_name_db}, '
                                    f'categories_created: {categories_created}, '
                                    f'categories_updated: {categories_updated}, '
                                    f'products_created: {products_created}, '
                                    f'products_updated: {products_updated}'},
                    status=201)


def error_prompt(status_data: bool, error_data: str, code_data: int) -> Response:
    """
    Вернуть сообщение об ошибке
    """
    return Response({'Status': status_data, 'Error': error_data}, status=code_data)
