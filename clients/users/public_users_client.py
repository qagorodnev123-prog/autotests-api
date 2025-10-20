from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает нового пользователя

        :param request: Словарь с параметрами создаваемого пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('api/v1/users', json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод создание пользователя с получением json на выходе
        :param request: Словарь с параметрами создаваемого пользователя
        :return: Ответ от сервера в виде json
        """
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())