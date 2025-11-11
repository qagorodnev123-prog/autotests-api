from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_user_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email


public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)
create_user_response = public_users_client.create_user(create_user_request)


private_users_client_request = AuthenticationUserSchema(
    email=create_user_response.user.email,
    password=create_user_request.password
)
private_user_client = get_private_user_client(private_users_client_request)
get_users_response = private_user_client.get_users_api(create_user_response.user.id)
get_users_response_data = get_users_response.json()

get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(get_users_response_data, get_user_response_schema)


