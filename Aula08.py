# Ex.33
for x in range(20, 101):
    print(x)

# Ex.34
for x in reversed(range(23, 53)):
    print(x)

print("\n")

for x in range(52, 22, -1):
    print(x)

# EX.36
PIN_VAL = 1234
tentativas = 0

while True:  # condição fixa cria ciclo infinito
    pin = int(input("Insira o seu pin de 4 algarismo:\n"))

    if pin != PIN_VAL:
        tentativas += 1
        if tentativas == 3:
            print("Login bloqueado!\n")
            break  # quebra ciclo infinito sem me preocupar com modificar a condição do while
        else:
            print(F"O pin está incorreto. Tem mais {3-tentativas} tentativas.")
    else:
        print("Seja bem-vindo!")
        break

