

# from pi_sdk import Keypair

# # #------------ from privateKey --------------------------------------------
# acc = Keypair.from_secret("SCA2SXW47M5JVM3CJCIZOY2YGYWBZEHVSGNE2RONO5EB3D2S72X54NU2")

# print("Public Key: " + acc.public_key)
# print("Secret Seed: " + acc.secret)
# print("------------------------")


# # #------------ from raw privateKey --------------------------------------------
# from pi_sdk import StrKey

# ss_raw = StrKey.decode_ed25519_secret_seed("SCA2SXW47M5JVM3CJCIZOY2YGYWBZEHVSGNE2RONO5EB3D2S72X54NU2")
# print('decode_ss -> bytes   : ',ss_raw)

# ss_raw = b'\x81\xa9^\xdc\xfb:\x9a\xb3bH\x91\x97cX6,\x1c\x90\xf5\x91\x9aME\xcdwH\x1d\x8fR\xfe\xaf\xde'
# print('ss_raw               : ',ss_raw)

# acc = Keypair.from_raw_ed25519_seed(ss_raw)

# print("Public Key: " + acc.public_key)
# print("Secret Seed: " + acc.secret)
# print("------------------------")


def from_secret(cls, secret: str) -> "Keypair":
    """Generate a :class:`Keypair` object from a secret key.

    :param secret: secret key (ex. ``"SB2LHKBL24ITV2Y346BU46XPEL45BDAFOOJLZ6SESCJZ6V5JMP7D6G5X"``)
    :return: A new :class:`Keypair` object derived by the secret.
    :raise: :exc:`Ed25519SecretSeedInvalidError <stellar_sdk.exceptions.Ed25519SecretSeedInvalidError>`:
        if `secret` is not a valid ed25519 secret seed.
    """
    raw_secret = StrKey.decode_ed25519_secret_seed(secret) # decode ss -> bytes 
    return cls.from_raw_ed25519_seed(raw_secret) 


@classmethod
def from_raw_ed25519_seed(cls, raw_seed: bytes) -> "Keypair":
    """Generate a :class:`Keypair` object from ed25519 secret key seed raw bytes.

    :param raw_seed: ed25519 secret key seed raw bytes
    :return: A new :class:`Keypair` object derived by the ed25519 secret key seed raw bytes
    """
    signing_key = ed25519.SigningKey(raw_seed)
    verify_key = signing_key.verify_key
    return cls(verify_key, signing_key)


