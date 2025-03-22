from pi_sdk import Keypair

# #------------ from privateKey --------------------------------------------
# acc = Keypair.from_secret("SB2LHKBL24ITV2Y346BU46XPEL45BDAFOOJLZ6SESCJZ6V5JMP7D6G5X")
acc = Keypair.from_secret("SAVSIXXGCQXAGGLTXHFATTWQJW3S2SHFAUDPKTTGLLZ6IY74BQ7K3ZAK")
# acc = Keypair.from_secret("SA6J52M5DL2NZITB2KCRU2KGRJPMQ3677OIUXB7V4Y4Z7QGXQOCEJZXE")

print("Public Key: " + acc.public_key)
print("Secret Seed: " + acc.secret)
print("------------------------")