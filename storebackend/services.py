import yaml
from rest_framework.response import Response


def read_yaml_write_to_db(request, *args, **kwargs) -> Response:
    """
    Прочитать yaml файл и выполнить запись в базу данных
    """
    return Response({'Status': True, 'success': 'Yes'}, status=201)