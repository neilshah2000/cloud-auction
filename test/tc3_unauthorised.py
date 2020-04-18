from helpers import loginUser, addAuctionItem

olgaToken = 'faketoken'

minutesToEnd = 1
response = addAuctionItem('Olgas Item', 'olga adds an item', minutesToEnd, olgaToken)

print(response.json())
    