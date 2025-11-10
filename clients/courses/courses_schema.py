from pydantic.alias_generators import to_camel
from pydantic import BaseModel, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema



class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры курса.
    """

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema


class CreateCourseResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры ответа при создании курса.
    """

    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на получение списка курсов.
    """

    user_id: str


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на создание курса.
    """

    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    """
    Описание структуры запроса на обновление курса.
    """

    title: str | None
    max_score: int | None
    min_score: int | None
    description: str | None
    estimated_time: str | None
