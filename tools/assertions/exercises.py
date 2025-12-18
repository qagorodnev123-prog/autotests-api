import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response

@allure.step("Check create exercise response")
def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с созданным упражнением.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что все поля фактического объекта ExerciseSchema совпадают
    с соответствующими полями ожидаемого объекта ExerciseSchema.

    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(get_response: GetExerciseResponseSchema, create_response: CreateExerciseResponseSchema):
    """
    Проверяет, что данные из ответа на получение упражнения соответствуют данным из ответа на создание упражнения.

    :param get_response: Ответ на запрос получения задания.
    :param create_response: Ответ на запрос создания упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_response.exercise, create_response.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что данные из запроса на обновление упражнения соответствуют данным из ответа на обновление упражнения.

    :param request: Запрос на обновление упражнения.
    :param response: Ответ на запрос обновление упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что при запросе на получение упражнения, которого нет, получаем ошибку 404 "Exercise not found".

    :param actual: Фактическая ошибка.
    :raises AssertionError: Если сообщение об ошибке не равно "Exercise not found".
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что все созданные упражнения присутствуют в ответе на получение списка упражнений.

    :param get_exercises_response: Ответ API со списком упражнений
    :param create_exercise_responses: Список созданных упражнений для проверки
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")
    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(
            get_exercises_response.exercises[index],
            create_exercise_response.exercise
        )