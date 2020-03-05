import requests
# Use the correct URL to retrieve data from the database
# The database is empty, but still we can send a request...
url = "http://3.92.177.227:9999/v1/auctionItem/"
response = requests.get(url)
# Let us transform the response in JSON format
json_response = response.json()
print(json_response)