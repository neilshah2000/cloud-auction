import requests

url = "http://localhost:9999/authentication/register/"
bilbo = {
    'username': 'bilbo',
    'password':'1234'
}
bilbo_response = requests.post(url, data = bilbo)
bilbo_response = bilbo_response.json()
print(bilbo_response)


# success
# {'access_token': 'GYIntTE8KRzBShwILOiMKwVfLWOiqO', 'expires_in': 36000, 'token_type': 'Bearer', 'scope': 'read write', 'refresh_token': 'oHrCBiuoTVTP8sU33V1QfYDGAulSFi'}