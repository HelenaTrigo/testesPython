
# ex. 11
num1 = float(input("insira em número com casas décimais.\n"))
num2 = float(input("insira outro número com casas décimais\n"))

print(F"{num1} + {num2} = {num1 + num2}")

# ex 12
preco = float(input("Indique o preço do produto: \n"))
IVA = 1.23

print(
    "O preço do profuto sem iva é: ", preco, "€.\n"
    F"O preço do produto com iva a 23% é: {preco * IVA:.2f} €."
)

# ex 13
num1 = float(input("Insira o 1º valor\n"))
num2 = float(input("Insira o 2º valor\n"))
num3 = float(input("Insira o 3º valor\n"))
num4 = float(input("Insira o 4º valor\n"))
num5 = float(input("Insira o 5º valor\n"))

print(f"A média dos números inseridos é: {(num1 + num2 + num3 + num4 + num5) / 5:.2f}")
