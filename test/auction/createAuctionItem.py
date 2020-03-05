import requests

headers = {'Authorization': 'Bearer 9KInFGflYxmov5kNMptWV3YlkSoK8q'}
auction_url = "http://3.92.177.227:9999/v1/auctionItem/"
response = requests.get(auction_url,headers=headers)
print(response.json())