import requests

url = 'http://172.31.80.164:9999/authentication/token/'
user = {'username': 'bilbo', 'password': '1234'}
response = requests.post(url, data = user)

# Let us transform the response in JSON format
json_response = response.json()
print(json_response)