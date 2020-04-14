import requests

url = "http://172.31.47.107:9999/authentication/register/"
frodo = {
    'username': 'test',
    'password':'1234'
}
frodo_response = requests.post(url, data = frodo)
frodo_response = frodo_response.json()
print(frodo_response)

# success
# {'access_token': 'bayUXHJc9yIzCJRZ2wqlxu0V88PoRZ', 'expires_in': 36000, 'token_type': 'Bearer', 'scope': 'read write', 'refresh_token': 'Ffwedz1S6jpmzKlOt9Sz2LvrXos4Jk'}