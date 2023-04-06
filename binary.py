def shift_to_left(binary_number: str, shifts: int) -> str:
    return binary_number[shifts:] + binary_number[:shifts]


def shift_to_right(binary_number: str, shifts: int) -> str:
    return binary_number[-shifts:] + binary_number[:-shifts]

# returns string


def hex_to_binary(hex_nr: str) -> str:
    return f'{int(hex_nr, 16):02b}'[-4:].rjust(4, "0")

# returns string


def binary_to_hex(binary: str) -> str:
    return hex(int(binary, 2))


def int_to_binary(int_nr: int) -> str:
    return f'{int(int_nr):02b}'[-4:].rjust(4, "0")


def hex_string_to_binary(msg: str):
    binary_string = ""
    for chr in msg:
        binary_string += hex_to_binary(chr)

    return binary_string
