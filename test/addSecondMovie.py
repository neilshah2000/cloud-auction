import requests
movies_url = "http://localhost:9999/v1/movies/"
headers = {'Authorization': 'Bearer bayUXHJc9yIzCJRZ2wqlxu0V88PoRZ'}
record = {'title': 'The LOTR','year':'2001','score':'4.5'}

frodo_response = requests.post(movies_url, headers=headers, data = record)
print(frodo_response.json())