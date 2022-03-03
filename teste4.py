





linha = ("2 * 3 =")
n1=""
n2=""
num = int(linha[0])*int(linha[4])
print(len(linha))

for cha in range(len(linha)):
    print(cha)
    if linha[cha].isdigit():
        if n1:
            n2=linha[cha]
        else:
            n1=linha[cha]

print(f'n1= {n1} n2= {n2}')
print(int(n1)*int(n2))
