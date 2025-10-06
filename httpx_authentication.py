import httpx


login_payload = {
  "email": "test_user@example.com",
  "password": "123456789qq"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Login response data: {login_response_data}')
print(f'Status code: {login_response.status_code}')

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print(f'Login response data: {refresh_response_data}')
print(f'Status code: {refresh_response.status_code}')