from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetExercisesApiQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class CreateExerciseApiRequestDict(TypedDict):
    """
    Описание структуры запроса для создания задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseApiRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления данных задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesApiQueryDict) -> Response:
        """
        Метод получения списка заданий.

        :param query: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseApiRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseApiRequestDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')