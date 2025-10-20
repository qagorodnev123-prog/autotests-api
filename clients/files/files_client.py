from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponseDict(TypedDict):
    file: File

class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    """
   Клиент для работы с /api/v1/files
   """
    def get_file(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/files/{file_id}')

    def create_file(self, request: CreateFileRequestDict) ->CreateFileResponseDict:
        """
        Метод создания файла с получением json на выходе
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде json
        """
        response = self.create_file_api(request)
        return response.json()

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            f'/api/v1/files',
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')})

    def delete_file(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/files/{file_id}')

def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))