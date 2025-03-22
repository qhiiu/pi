from stellar_sdk import Server

server = Server("https://horizon-testnet.stellar.org")
# server = Server("https://horizon-mainnet.stellar.org")
public_key = "GD4NB2FLQAN5JO7PKPGZJMNBDYQXVSNVC7DEIZMOL5WSNSBLEBUTEF5Q"
account = server.accounts().account_id(public_key).call()
for balance in account['balances']:
    print(f"Type: {balance['asset_type']}, Balance: {balance['balance']}")