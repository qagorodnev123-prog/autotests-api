from pydantic.alias_generators import to_camel
from pydantic import BaseModel, ConfigDict

class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры задания.
    """

    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение задания.
    """

    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на получение списка заданий.
    """

    course_id: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на создание задания.
    """

    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на обновление задания.
    """

    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema