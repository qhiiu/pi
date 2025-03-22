# from stellar_sdk import Keypair
from pi_sdk import Keypair

#------------ random --------------------------------------------
# keypair = Keypair.random()

# print("Public Key: " + keypair.public_key)
# print("Secret Seed: " + keypair.secret)
# print("------------------------")

#------------ mnemonic --------------------------------------------
# mn24 = Keypair.generate_mnemonic_phrase()
# "coyote timber absorb palace cabin deny saddle document mosquito alley dismiss elephant"
mn24 = "dance angry orphan galaxy awkward often cream join update wing defense clerk vivid model cousin scene boil harvest hero doll expire garment tissue lesson"
print("mn24 : ", mn24)

acc = Keypair.from_mnemonic_phrase(mn24)
print("Secret Seed: " + acc.secret)
print("Public Key: " + acc.public_key) 


# mn24 :  dance angry orphan galaxy awkward often cream join update wing defense clerk vivid model cousin scene boil harvest hero doll expire garment tissue lesson
# Secret Seed: SARPB6VKSWSAMX5LBQWV2ZKZPGLGFJTTNGSH25VG74LUBAQWYSMRJMDP
# Public Key: GAJQK6ISTT2ZR6PV4GRU332OM3EMFXYEMV2YBUPRY5DY6GDKSPGBOSD2


# pi : GBPSFXZPRKCJNPTB3P6OVS3W7DTJPNJFE4CYVSGN3AVUKEGYVEAOEE47 
print("------------------------")


