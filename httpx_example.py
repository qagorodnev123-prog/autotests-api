import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.json())
#
# data = {
#
#     "userId": 1,
#     "title": "новая задача",
#     "completed": False
#
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.status_code)
# print(response.json())
#
# data = {'username': 'test_user', 'password': '12345'}
# response = httpx.post('https://httpbin.org/post', data=data)
# print(response.status_code)
# print(response.json())
#
# headers = {'authorization': 'Bearer my secret_token'}
# response = httpx.get('https://httpbin.org/get', headers=headers)
# print(response.status_code)
# print(response.json())
# print(response.request.headers)
# print('-----------------------------')
# headers = {'id': 1}
# params = {'userId': 1}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response.url)
# print(response.json())
# print('-----------------------------')
# files = {'file': ('example.txt', open('example.txt', 'rb'))}
# response = httpx.post('https://httpbin.org/post', files=files)
# print(response.url)
# print(response.json())
# print('-----------------------------')
# with httpx.Client() as client:
#     response_1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response_2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
# print(response_1.json())
# print(response_2.json())
# print('-----------------------------')
# client = httpx.Client(headers={'Authorization': 'Bearer my secret_token'})
# response = client.get('https://httpbin.org/get')
# print(response.json())
try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid_url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса {e}')

try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print(f'Запрос превысил лимит времени')