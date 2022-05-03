# distutils: language = c++
from csafebox cimport crypt as c_crypt, decrypt as c_decrypt, get_keys as c_get_keys

def crypt(char* message):
    return c_crypt(message)

def decrypt(char* crypted):
    return c_decrypt(crypted)

def get_keys():
    return c_get_keys()