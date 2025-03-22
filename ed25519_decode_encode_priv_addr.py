from pi_sdk import StrKey 

ss = StrKey.decode_ed25519_secret_seed("SCA2SXW47M5JVM3CJCIZOY2YGYWBZEHVSGNE2RONO5EB3D2S72X54NU2")
print('decode_ss -> bytes : ',ss)
print('decode_ss -> hex   : ', ss.hex())
print()

ss_input = b'\x81\xa9^\xdc\xfb:\x9a\xb3bH\x91\x97cX6,\x1c\x90\xf5\x91\x9aME\xcdwH\x1d\x8fR\xfe\xaf\xde'
ss_result = StrKey.encode_ed25519_secret_seed(ss_input)
print(ss_result)
print()

pk = StrKey.decode_ed25519_public_key("GBPSFXZPRKCJNPTB3P6OVS3W7DTJPNJFE4CYVSGN3AVUKEGYVEAOEE47")
print(pk)
print(pk.hex())
print()

pk_input = b'_"\xdf/\x8a\x84\x96\xbea\xdb\xfc\xea\xcbv\xf8\xe6\x97\xb5%\'\x05\x8a\xc8\xcd\xd8+E\x10\xd8\xa9\x00\xe2'
pk_result = StrKey.encode_ed25519_public_key(pk_input)
print(pk_result)
print()

z = bytes.fromhex("5f22df2f8a8496be61dbfceacb76f8e697b52527058ac8cdd82b4510d8a900e2")
print(z)
print()
