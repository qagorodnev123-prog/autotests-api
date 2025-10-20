from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseApiRequestDict
from clients.files.files_client import get_file_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserDict, get_public_user_client
from tools.fakers import get_random_email

public_client = get_public_user_client()
create_user_request = CreateUserDict(
    email=get_random_email(),
    password= "string",
    lastName= "string",
    firstName= "string",
    middleName= "string"
)
create_user_response = public_client.create_user(create_user_request)
print("Create user data:",create_user_response)

authentication_user_dict = AuthenticationUserDict(
    email=create_user_response['user']['email'],
    password= create_user_request['password']
)


files_client = get_file_client(authentication_user_dict)
file_file_request = CreateFileRequestDict(
    filename= 'dog_picture',
    directory= 'courses',
    upload_file= './testdata/files/65ab088dac8b89b4c8b3421726b32df0.jpg'
)
create_file_response = files_client.create_file(file_file_request)
print("Create file data:", create_file_response)


courses_client = get_courses_client(authentication_user_dict)
create_course_request = CreateCourseRequestDict(
    title= 'Python course',
    maxScore= 100,
    minScore= 1,
    description= 'Learning basic Python',
    estimatedTime= '100 hours',
    previewFileId= create_file_response['file']['id'],
    createdByUserId= create_user_response['user']['id']
)
response_create_course = courses_client.create_course(create_course_request)
print("Create course data:", response_create_course)


exercises_client = get_exercises_client(authentication_user_dict)
create_exercise_request = CreateExerciseApiRequestDict(
    title= 'Variable Creation',
    courseId= response_create_course['course']['id'],
    maxScore= 5,
    minScore= 0,
    orderIndex= 3,
    description= "Create a variable 'a' and assign it the value 1",
    estimatedTime= '10 min'
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)