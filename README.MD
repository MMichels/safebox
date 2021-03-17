# SAFEBOX
A minimal safe way to store your application credentials.

## DESCRIPTION
This application is build with cython and c/c++ code, this allow us to store a \"super secret key\" to encrypt and decrypt strings, using **AES** algorithm, this allow to store, with a minimum safety, crypted strings, this strings, can be, for ex. users, passwords, address to database connection.

## DEFINE YOUR KEYS!

**IMPORTANT**: This module comes with random keys, but is **EXTREMALLY RECOMENDED** than you compile this module by you own, from sources (*available on github*), to define YOUR UNIQUE secret key on the c/c++ modules.

**IMPORTANT2**: The PRIVATE_KEY **MUST** be 32bytes long (32 chars) and the PRIVATE_IV **MUST** be 16bytes (16 chars) long and ASCII characters.

To define your keys follow the steps:

1. Open the setup.py file
2. On Extensions definitions, inside "define_macros" change values of PRIVATE_KEY and PRIVATE_IV (recommend use of [UUID generator](https://www.uuidgenerator.net/version1) without '-' characters, to generate truly unique keys)

## Install Guides

Once your keys are alrealy defined, you can compile the lib.

1. Install Setuptools, wheels and Cython library
2. If your use venv, activate your enviroment
3. On main directory, run: python setup.py install
4. Ready!

## Usage Example

```
import safebox

message = "test 123 !@#"
crypted = safebox.crypt(message.encode()).decode()
decrypted = safebox.decrypt(crypted.encode()).decode()

print("Message: ", message)
print("Crypted: ", crypted)
print("Decrypted: ", decrypted)

```

### REFERENCES

Encryption algorithm take from: [Encryptions](https://github.com/calccrypto/Encryptions)


