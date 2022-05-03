cdef extern from "safebox.h":
    void get_keys()
    char *crypt(char *message)
    char *decrypt(char *crypted)