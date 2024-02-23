from pprint import pprint

import yaml
from rest_framework.response import Response

from storebackend.models import Shop, ProductInfo


def read_yaml_write_to_db(request, *args, **kwargs) -> Response:
    """
    Прочитать yaml файл и выполнить запись в базу данных
    """
    try:
        import_file = request.FILES['upload_file'].file.read()
        import_data = yaml.load(import_file, Loader=yaml.FullLoader)
    except Exception as error:
        return error_prompt(False, "File didn't load", 400)
    #  Записать/обновить данные по магазину

    #  !!!!!!!!!!!!!! Добавить владельца магазина после аутентификации

    shop, status_result = Shop.objects.get_or_create(name=import_data['shop'])  #  , user_id=request.user.id)
    if not status_result:
        if shop.user_id == request.user.id:
            ProductInfo.objects.filter(shop_id=shop.id).delete()
    print(shop, status_result)

    return Response({'Status': True, 'success': 'Yes'}, status=201)


def error_prompt(status_data: bool, error_data: str, code_data: int) -> Response:
    """
    Вернуть сообщение об ошибке
    """
    return Response({'Status': status_data, 'Error': error_data}, status=code_data)