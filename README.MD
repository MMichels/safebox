# SAFEBOX
A minimal safe way to store your application credentials.

## DESCRIPTION
This application is build with cython and c/c++ code, this allow us to store a \"super secret key\" to encrypt and decrypt strings, using **AES** algorithm, this allow to store, with a minimum safety, crypted strings, this strings, can be, for ex. users, passwords, address to database connection.

**IMPORTANT**: This module comes with random keys, but is EXTREMALLY RECOMENDED than you compile this module by you own, from sources (*available on github*), to define YOUR UNIQUE secret key on the c/c++ modules.

**IMPORTANT2**: The PRIVATE_KEY must be 32bytes long (32 chars) and the PRIVATE_IV must be 16bytes long.

### REFERENCES

Encryption algorithm take from: [Encryptions](https://github.com/calccrypto/Encryptions)


