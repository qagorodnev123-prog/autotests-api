import  httpx

login_payload = {
    "email": "test_user@example.com",
    "password": "123456789qq"
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_payload_data = login_response.json()

get_user_headers = {'Authorization': f'Bearer {login_payload_data["token"]["accessToken"]}'}
get_user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=get_user_headers)
get_user_data = get_user_response.json()
print(get_user_data)
print(get_user_response.status_code)