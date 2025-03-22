from pi_sdk import StrKey

print("-------------------------")

nb_int = 1
nb_hex = hex(nb_int)
nb_input = '0'*(64 - len(nb_hex)) + nb_hex[2:]

print('nb_int   : ', nb_int)
print('nb_input : ', nb_input)

ss_input = bytes.fromhex(nb_input)
print(ss_input)
print()

# ss_input = b'\x81\xa9^\xdc\xfb:\x9a\xb3bH\x91\x97cX6,\x1c\x90\xf5\x91\x9aME\xcdwH\x1d\x8fR\xfe\xaf\xde'
ss_result = StrKey.encode_ed25519_secret_seed(ss_input)
print(ss_result)
print()

print("-------------------------")


# SCA2SXW47M5JVM3CJCIZOY2YGYWBZEHVSGNE2RONO5EB3D2S72X54NU2
# 81a95edcfb3a9ab3624891976358362c1c90f5919a4d45cd77481d8f52feafde


# GBPSFXZPRKCJNPTB3P6OVS3W7DTJPNJFE4CYVSGN3AVUKEGYVEAOEE47
# 5f22df2f8a8496be61dbfceacb76f8e697b52527058ac8cdd82b4510d8a900e2