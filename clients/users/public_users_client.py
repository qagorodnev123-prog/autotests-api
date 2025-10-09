from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient

class CreateUserDict(TypedDict):
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

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод создает нового пользователя

        :param request: Словарь с параметрами создаваемого пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('api/v1/users', json=request)

