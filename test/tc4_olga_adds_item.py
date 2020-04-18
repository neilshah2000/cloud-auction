from helpers import loginUser, addAuctionItem

olga = {'username': 'olga', 'password': 'olga'}
olgaToken = loginUser(olga)

minutesToEnd = 1
response = addAuctionItem('Olgas Item', 'olga adds an item', minutesToEnd, olgaToken)

print(response.json())
    
