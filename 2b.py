#p2b
def bin2Dec(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1
    return dec

def oct2Hex(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1

    hex_list = []
    while dec != 0:
        hex_list.append(dec % 16)
        dec = dec // 16

    hex_string = ""
    for elem in hex_list[::-1]:
        if elem <= 9:
            hex_string += str(elem)
        else:
            hex_string += chr(ord('A') + (elem - 10))

    return hex_string

num1 = input("Enter a binary number: ")
print(bin2Dec(num1))

num2 = input("Enter an octal number: ")
print(oct2Hex(num2))
