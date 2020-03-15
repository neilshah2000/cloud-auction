import requests

url = 'http://127.0.0.1:9999/authentication/token/'
user = {'username': 'bilbo', 'password': '1234'}
response = requests.post(url, data = user)

# Let us transform the response in JSON format
json_response = response.json()
print(json_response)