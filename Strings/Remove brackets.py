char = "(a-b)+[c*d]+{e/f}"
equ = str()
for i in char:
    if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
        pass
    else:
        equ += i

print(equ)