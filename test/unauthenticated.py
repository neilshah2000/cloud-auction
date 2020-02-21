import requests
# Use the correct URL to retrieve data from the database
# The database is empty, but still we can send a request...
url = "http://localhost:9999/v1/movies/"
response = requests.get(url)
# Let us transform the response in JSON format
json_response = response.json()
print(json_response)