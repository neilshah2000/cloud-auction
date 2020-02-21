import requests

movies_url = "http://localhost:9999/v1/movies/" # Our API!
headers = {'Authorization': 'Bearer GYIntTE8KRzBShwILOiMKwVfLWOiqO'}
record = {'title': 'The Hobbit', 'year':'2012', 'score':'5'}

bilbo_response = requests.post(movies_url, headers=headers, data=record)
print(bilbo_response.json())