from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_file_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateUserDict
from tools.fakers import get_random_email

public_users_client = get_public_user_client()
create_user_request = CreateUserDict(
    email=get_random_email(),
    password= "string",
    lastName= "string",
    firstName= "string",
    middleName= "string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data: ', create_user_response)
authentication_user_dict = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_file_client(authentication_user_dict)
courses_client = get_courses_client(authentication_user_dict)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory= 'courses',
    upload_file='./testdata/files/2024-10-20_13-19-25.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_response)

create_course_request = CreateCourseRequestDict(
    title= "Python",
    maxScore= 100,
    minScore= 10,
    description= "Python API course",
    estimatedTime= "2 weeks",
    previewFileId= create_file_response['file']['id'],
    createdByUserId= create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)