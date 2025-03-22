#include <Python.h>
#include <iostream>
#include <string>
#include <iomanip>
#include <sodium.h>
#include <cstring>

// Hàm chuyển mnemonic thành seed
std::string mnemonicToSeed(const std::string& mnemonic) {
    Py_Initialize();

    // Set up Python interpreter with the `mnemonic` string
    PyObject* pMnemonic = PyUnicode_FromString(mnemonic.c_str());
    if (!pMnemonic) {
        std::cerr << "Error: Unable to create Python string from C++ string!" << std::endl;
        Py_Finalize();
        return "";
    }

    // Define Python code that will use the `mnemonic` string
    const char* pythonCode = R"(
from mnemonic import Mnemonic

def mnemonic_to_seed(mnemonic):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic, passphrase="")
    return seed.hex()

seed = mnemonic_to_seed(mnemonic)
)";

    PyRun_SimpleString("mnemonic = None");  // Clear the 'mnemonic' variable if it exists
    PyDict_SetItemString(PyModule_GetDict(PyImport_AddModule("__main__")), "mnemonic", pMnemonic);

    // Run the Python code in the current Python interpreter context
    PyRun_SimpleString(pythonCode);

    // Access the global dictionary and get the variable `seed`
    PyObject* pGlobalDict = PyModule_GetDict(PyImport_AddModule("__main__"));
    PyObject* pSeed = PyDict_GetItemString(pGlobalDict, "seed");

    std::string seedHex = "";
    if (pSeed != nullptr) {
        if (PyUnicode_Check(pSeed)) {
            seedHex = PyUnicode_AsUTF8(pSeed);
        }
    }

    Py_Finalize();
    return seedHex;
}

// Hàm tạo private key từ seed
void seedToPrivateKey(const std::string& seedHex, unsigned char privateKey[32]) {
    if (sodium_init() == -1) {
        std::cerr << "sodium initialization failed!" << std::endl;
        return;
    }

    unsigned char publicKey[32];  // Allocate space for public key
    // if (crypto_sign_ed25519_seed_keypair(publicKey, privateKey, (const unsigned char*)seedHex.c_str()) != 0) {
        if (crypto_sign_ed25519_seed_keypair(publicKey, privateKey, (const unsigned char*)seedHex.c_str())) {
        std::cerr << "Error generating keypair!" << std::endl;
    }
}

// Hàm tạo public key từ private key
// void privateKeyToPublicKey(const unsigned char privateKey[32], unsigned char publicKey[32]) {
//     if (crypto_sign_ed25519_publickeybytes(publicKey, privateKey) != 0) {
//         std::cerr << "Error generating public key from private key!" << std::endl;
//     }
// }

// Hàm tạo địa chỉ Pi từ public key
// std::string publicKeyToPiAddress(const unsigned char publicKey[32]) {
//     unsigned char hash[32];
//     crypto_hash_sha256(hash, publicKey, 32);

//     unsigned char ripemd160[20];
//     if (crypto_hash_ripemd160(ripemd160, hash, 32) != 0) {
//         std::cerr << "Error hashing with RIPEMD-160!" << std::endl;
//         return "";
//     }

//     // Pi Network address starts with "P"
//     std::stringstream address;
//     address << "P";  // Add the prefix "P" for Pi Network address
//     for (int i = 0; i < 20; ++i) {
//         address << std::setw(2) << std::setfill('0') << std::hex << (int)ripemd160[i];
//     }
//     return address.str();
// }

int main() {
    // Mnemonic của ví Pi Network
    std::string mnemonic = "dinner fever royal jump hint speak absurd invest obey village siren solar bracket trim post enroll outdoor clinic juice praise palm draft jealous lady";  

    // Chuyển mnemonic thành seed
    std::string seedHex = mnemonicToSeed(mnemonic);

    if (seedHex.empty()) {
        std::cerr << "Error converting mnemonic to seed!" << std::endl;
        return -1;
    }

    // Tạo private key từ seed
    unsigned char privateKey[32];
    seedToPrivateKey(seedHex, privateKey);
    std::cout << privateKey ;


    // Tạo public key từ private key
    // unsigned char publicKey[32];
    // privateKeyToPublicKey(privateKey, publicKey);

    // Tạo địa chỉ Pi từ public key
    // std::string piAddress = publicKeyToPiAddress(publicKey);
    // std::cout << "Pi Network Address: " << piAddress << std::endl;

    return 0;
}
