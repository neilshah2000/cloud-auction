import requests

headers = {'Authorization': 'Bearer GYIntTE8KRzBShwILOiMKwVfLWOiqO'}
movies_url = 'http://localhost:9999/v1/movies/1'
response = requests.get(movies_url,headers=headers)
print(response.json())
