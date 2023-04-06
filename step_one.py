from binary import *
from constants import *
from helpers import *

def get_k(key: str):
    key_as_list = [i for i in key]
    k = ""
    
    for i, j in zip(key_as_list[0::2], key_as_list[1::2]):
        k += hex_to_binary(i) + hex_to_binary(j)
    
    return k

def generate_shifted_blocks(C0: list, D0: list):
    Cn = []
    Dn = []
    
    Cn.append("".join(C0))
    Dn.append("".join(D0))

    for i in range(16):
        Cx = shift_to_left(Cn[i], no_left_shifts[i])
        Dx = shift_to_left(Dn[i], no_left_shifts[i])
        Cn.append(Cx)
        Dn.append(Dx)
        
    return Cn, Dn

def encode_key(key):
    k = get_k(key)
    k_plus = permutate(k, pc1)

    C, D = split(k_plus)

    return C,D

def step_one(key: str):
    if len(key) < 16: 
        raise ValueError("Key size is invalid. It must be 16 chars long.")
    
    C, D = encode_key(key)
    Cn, Dn = generate_shifted_blocks(C,D)
    Kn = []
    for i in range(17):
        Kn.append(permutate(Cn[i] + Dn[i], pc2))

    return Kn