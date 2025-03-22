from mnemonic import Mnemonic

def mnemonic_to_seed(mnemonic):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic, passphrase="")
    return seed.hex()

if __name__ == "__main__":
    mnemonic = "region train protect combine bid security gadget woman close average genius combine series dentist nasty title shrimp wave siege violin slab lunch give cart"
    seed = mnemonic_to_seed(mnemonic)
    print(seed)
