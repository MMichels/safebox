#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include "Encryptions/Encryptions.h"
#include "safebox.h"
#include "base64.h"

using namespace std;

SymAlg *aes;
CBC *cbc;


void init(void){
    string key = TOSTRING(PRIVATE_KEY);
    string iv = TOSTRING(PRIVATE_IV);    

    cout << "Key: " << key << endl;
    cout << "iv: " << iv << endl;

    if (key.compare("f2b403ea764d11eb94390242ac130002") == 0 ||
        iv.compare("76fc77c44a46c70a") == 0
    )
    {
        cout << "!!!ATTENTION!!! YOU ARE USING THE DEFAULT PRIVATE AND IV KEYS, ";
        cout << "WHATs IS NOT!!! A FULL SAFE POLICY, ";
        cout << "LEARN MORE ON: https://github.com/MMichels/safebox" << endl;
    }
    
    aes = new AES(key);
    cbc = new CBC(aes, iv);
}


void finish(void){
    delete(aes);
    delete(cbc);
}

void get_keys(void){    
    string key = TOSTRING(PRIVATE_KEY);
    string iv = TOSTRING(PRIVATE_IV);

    cout << "Key: " << key << endl;
    cout << "iv: " << iv << endl;

    if (key.compare("f2b403ea764d11eb94390242ac130002") == 0 ||
        iv.compare("76fc77c44a46c70a") == 0
    )
    {
        cout << "!!!ATTENTION!!! YOU ARE USING THE DEFAULT PRIVATE AND IV KEYS, ";
        cout << "WHATs IS NOT!!! A FULL SAFE POLICY, ";
        cout << "LEARN MORE ON: https://github.com/MMichels/safebox" << endl;
    }
}

char* crypt(char *message){
    init();

    string str(message);
    string crypted = cbc->encrypt(str);
    string b64_cpt = base64_encode(crypted);

    char *cstr = new char[b64_cpt.length() + 1];
    strcpy(cstr, b64_cpt.c_str());
        
    return cstr;
}

char* decrypt(char *b64_crypted){
    init();

    string b64_str(b64_crypted);
    string str = base64_decode(b64_str);
    string decrypted = cbc->decrypt(str);

    char *cstr = new char[decrypted.length() + 1];
    strcpy(cstr, decrypted.c_str());

    return cstr;
}
