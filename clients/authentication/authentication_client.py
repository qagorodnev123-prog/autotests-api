from httpx import Response, Client

from clients.api_client import APIClient
from typing import TypedDict

from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponse(TypedDict):
    token: Token

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    pass

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestDict) -> LoginResponse:
        """
        Метод выполняет аутентификацию пользователя с получением json на выходе
        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде json
        """
        response = self.login_api(request)
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())