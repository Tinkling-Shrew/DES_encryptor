from binary import *
from constants import *
from helpers import *
from textwrap import wrap

def get_s(i, x, y):
    return s[i][16*x + y]

def get_i_j(bin_nr):
    i = int(bin_nr[0] + bin_nr[-1], 2)
    j = int(bin_nr[1:len(bin_nr) - 1], 2)

    return i,j

def f(R, K):
    res = xor("".join(K), "".join([R[e_bit_selection[j]-1] for j in range(48)]))
    out = ""
    c = 0
    for group in wrap(res, 6):
        i, j = get_i_j(group)
        out += int_to_binary(get_s(c, i, j))
        c+=1
    
    out = permutate(out, p)

    return out

def encode(Kn, L0, R0):
    Ln = [L0]
    Rn = [R0]
    for i in range(1,17):
        Ln.append(Rn[i-1])
        Rn.append(xor(Ln[i-1], f(Rn[i-1], Kn[i])))
    
    return Ln, Rn

def step_two(msg, Kn):
    M = hex_string_to_binary(msg)
    M = permutate(M, ip)

    L0, R0 = split(M)
    Ln, Rn = encode(Kn, L0, R0)

    R16L16 = Rn[16] + Ln[16]
    IP_1 = permutate(R16L16, ip_1)


    return binary_to_hex(IP_1)
    