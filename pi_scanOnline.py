from pi_sdk import Keypair
import requests

def check_pi_balance(pi_address):
    # Example URL for Pi Network's balance API (this is a placeholder URL)
    url = f"https://api.mainnet.minepi.com/accounts/{pi_address}"
    # url = f"https://api.testnet.minepi.com/accounts/{pi_address}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        balance_data = response.json() 

        balance =  balance_data['balances'][0]['balance']
        print(f"The balance for Pi address {pi_address} is :\n {balance}")
        exit("------ check and take $ -------- ")

    else:
        print("---- X -----")

def run():
    mn24 = Keypair.generate_mnemonic_phrase()
    # mn24 = "dance angry orphan galaxy awkward often cream join update wing defense clerk vivid model cousin scene boil harvest hero doll expire garment tissue lesson"
    # mn24 = "exclude strong electric food food weather champion exist dry trap arrive flock life civil organ airport machine jealous virtual syrup car dizzy upper describe"
    
    print("nm24 : ", mn24)

    acc = Keypair.from_mnemonic_phrase(mn24)
    print("Public Key: " + acc.public_key)
    # print("Secret Seed: " + acc.secret)
    pi_address = acc.public_key
    check_pi_balance(pi_address)

for i in range(100000000):
    run()


# dance angry orphan galaxy awkward often cream join update wing defense clerk vivid model cousin scene boil harvest hero doll expire garment tissue lesson
# stellar : GAJQK6ISTT2ZR6PV4GRU332OM3EMFXYEMV2YBUPRY5DY6GDKSPGBOSD2
# pi : GBPSFXZPRKCJNPTB3P6OVS3W7DTJPNJFE4CYVSGN3AVUKEGYVEAOEE47 
# Secret Seed: SCA2SXW47M5JVM3CJCIZOY2YGYWBZEHVSGNE2RONO5EB3D2S72X54NU2