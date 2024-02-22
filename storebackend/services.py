from pprint import pprint

import yaml
from rest_framework.response import Response


def read_yaml_write_to_db(request, *args, **kwargs) -> Response:
    """
    Прочитать yaml файл и выполнить запись в базу данных
    """
    with open('file.yaml', 'wb') as f:
        f.write(request.FILES['upload_file'].file.read())
    with open('file.yaml', encoding='utf-8') as f:
        import_data = yaml.load(f, Loader=yaml.FullLoader)
        pprint(import_data)
    return Response({'Status': True, 'success': 'Yes'}, status=201)