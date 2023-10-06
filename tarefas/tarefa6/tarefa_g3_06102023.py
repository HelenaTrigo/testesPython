# Grupo3 - Irina, Jennifer, Helena
# Ex. 1
num = float(input("Indique um número:\n"))

if num % 2 == 0 and num != 0:
  print(F"O número {num} é par.")
elif num % 2 != 0:
  print(F"O número {num} é ímpar.")
else:
  print("O número é nulo.")

# Ex. 2
num1 = float(input("Insira o primeiro número:\n"))
num2 = float(input("Insira o segundo número:\n"))
num3 = float(input("Insira o terceiro número:\n"))

if num1 == num2:
    print(F"A soma dos 3 números é {num1 + num2 + num3}")
else:
    print(F"A multiplicação dos 3 números é {num1 * num2 * num3}")

# Ex. 3
cor1 = input("Digite a primeira cor: ")
cor2 = input("Digite a segunda cor: ")
cor3 = input("Digite a terceira cor: ")

if cor1 == cor2 and cor2 == cor3:
    print("Todas as cores são iguais.")
else:
    print("As cores são diferentes.")

# Ex. 4
preco_produto = float(input("Digite o preço do produto: "))
importado = input("O produto é importado? (sim ou nao): ")

comissoes = 0
if importado.lower() == "sim":
    comissoes = 5
    valor_iva = 0.23 * preco_produto
    print(
        F"Você deve pagar {comissoes + valor_iva:.2f}€, sendo {comissoes}€"
        F" de comissões de desalfandegamento e {valor_iva:.2f}€ de IVA."
    )
else:
    print("Você não tem nada a pagar.")