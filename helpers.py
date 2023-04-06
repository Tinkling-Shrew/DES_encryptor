def permutate(k, pc):
    k_plus = ""

    for i in range(len(pc)):
        for j in range(len(pc[i])):
            k_plus += k[pc[i][j] - 1]
    
    return k_plus

def split(k_plus):
    C = k_plus[:len(k_plus)//2]
    D = k_plus[len(k_plus)//2:]

    return C, D

def xor(lhs, rhs):
    if(len(lhs) != len(rhs)):
        raise ValueError(f"The two arguments must be of the same length (lhs: {len(lhs)}, rhs: {len(rhs)}).")
    
    val = ""
    for i in range(len(lhs)):
        val += str((int(lhs[i]) + int(rhs[i])) % 2)
    
    return val

def arr_to_str(array: list) -> str:
    return "".join(array)