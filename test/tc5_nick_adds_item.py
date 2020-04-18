from helpers import loginUser, addAuctionItem

nick = {'username': 'nick', 'password': 'nick'}
nickToken = loginUser(nick)

minutesToEnd = 1
response = addAuctionItem('Nicks Item', 'nick adds an item', minutesToEnd, nickToken)

print(response.json())
    
