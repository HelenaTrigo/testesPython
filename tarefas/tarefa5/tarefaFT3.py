# Ex.1
print(
    "1 - vermelho\n"
    "2 - amarelo\n"
    "3 - verde"
)

cor_semaf = int(input("Indique o número que corresponde à cor do semáforo:\n"))

if cor_semaf == 1:
    print("Parar")
elif cor_semaf == 2:
    print("Prestar atenção")
elif cor_semaf == 3:
    print("Avançar")
else:
    print("Opção Inválida!")

# Ex.2
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
num3 = float(input("Insira o 3º número: "))

soma = num1 + num2

if soma < num3:
    print(F"A soma do {num1} e {num3} é menor que {num3}")
else:
    print(F"A soma do {num1} e {num3} é maior que {num3}")

# Ex.3
genero = input("Indique o seu género:[M/F/I]\n")

if genero == "M" or genero == "m":
    print("É do género Mascullino")
elif genero in ("F", "f"):
    print("É do genero Feminino.")
elif genero.upper() == "I":
    print("Indicou o seu género como Indeferenciado.")
else:
    print("Género Inválido!")

# Ex.4
num_inserido = float(input("Insira um número: "))

if num_inserido == 0:
    print("O número é inválido!")
elif num_inserido > 0:
    print("O dobro do número inserido é: ", 2 * num_inserido)
else:
    print("O quádruplo do número inserido é: ", 4 * num_inserido)

# Ex5
n1 = float(input("Insira um número:\n"))
n2 = float(input("Insira outro número:\n"))

if n1 < n2:
    print(F"{n1} {n2}")
elif n1 > n2:
    print(F"{n2} {n1}")
else:
    print("Os números inseridos são iguais.")

# Ex6
genero = input("Indique o seu género: [M/F]\n").upper()

if genero == "M":
    altura = float(input("Indique a sua altura em metros:\n"))
    peso_ideal = 72.7 * altura - 58
    print(F"O seu peso ideal é: {peso_ideal:.2f}")
elif genero == "F":
    altura = float(input("Indique a sua altura em metros:\n"))
    peso_ideal = 62.1 * altura - 44.7
    print(F"O seu peso ideal é: {peso_ideal:.2f}")
else:
    print("Género Desconhecido")
