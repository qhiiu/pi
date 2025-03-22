import requests

def check_pi_balance(pi_address):
    # Example URL for Pi Network's balance API (this is a placeholder URL)
    url = f"https://api.mainnet.minepi.com/accounts/{pi_address}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        balance_data = response.json()
        return balance_data['balances'][0]['balance']
    else:
        return "Error fetching balance"

# Usage example
# pi_address = 'GBTJM4JPOQABFSSSELKYVXRFI7GFPQZO3Y6ETEVHSI2MTIO6UQJB646C'
pi_address = 'GDWKZ6B742GXHEOW6ZRF6JVDYZHELQFT4S7C7KAJKSBBO6JATNXNXVBR'
balance = check_pi_balance(pi_address)
print(f"The balance for Pi address {pi_address} is :\n {balance}")
