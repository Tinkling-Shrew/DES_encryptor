from step_one import *
from step_two import *

def DES_encrypt(msg: hex, key: hex) -> hex:
    return step_two(msg, step_one(key))

def main():
    key = "133457799BBCDFF1"
    msg = "0123456789ABCDEF"
    print("MESSAGE: ", msg)
    print("KEY: ", key, "\n---------------------------------")
    print("ENCRYPTED: ", DES_encrypt(msg, key))
    

if __name__ == "__main__":
    main()