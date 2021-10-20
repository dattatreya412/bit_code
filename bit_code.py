bit_code = input("Enter you's bit code : ")
length = len(bit_code)
verification = 0
i = 0
while verification == 0:
    verification = 1
    while i <= length-4:
        if bit_code[i] == bit_code[i+1] == bit_code[i+2] == bit_code[i+3] == "0":
            bit_code = bit_code[:i+4] + "1" + bit_code[i+5:]
            length = length + 1
            verification = 0
        if bit_code[i] == bit_code[i+1] == bit_code[i+2] == bit_code[i+3] == "1":
            bit_code = bit_code[:i+4] + "0" + bit_code[i+5:]
            length = length + 1
            verification = 0
        i = i + 1

print(bit_code)
