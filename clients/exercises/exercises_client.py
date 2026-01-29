import allure

from clients.api_client import APIClient
from httpx import Response

from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, \
    GetExerciseResponseSchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))


    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получения списка заданий в виде json
        :param query: Идентификатор курса
        :return: Ответ от сервера в виде json
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Get exercise")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения информации о задании в виде json
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде json
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания

           задания с ответом в виде json
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде json
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Update exercise by exercise id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        """
        Метод обновления данных задания с ответом в виде json.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде json
        """
        response = self.update_exercise_api(exercise_id, request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Delete exercises by exercise id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))