from clients.api_client import APIClient
from httpx import Response

from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, \
    GetExerciseResponseSchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema



class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)


    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получения списка заданий в виде json
        :param query: Идентификатор курса
        :return: Ответ от сервера в виде json
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения информации о задании в виде json
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде json
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> GetExerciseResponseSchema:
        """
        Метод создания

           задания с ответом в виде json
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде json
        """
        response = self.create_exercise_api(request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        """
        Метод обновления данных задания с ответом в виде json.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде json
        """
        response = self.update_exercise_api(exercise_id, request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))