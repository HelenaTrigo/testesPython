pais = input("Indique um país.\n").capitalize()

if pais == "Alemanha":
    print(F"As cores da bandeira do país {pais} são: preto, vermelho e amarelo.")
elif pais in ("Dinamarca", "Áustria"):
    print(F"As cores da bandeira do país {pais} são: vermelho e branco.")
elif pais == "Estónia":
    print(F"As cores da bandeira do país {pais} são: azul, preto e branco.")
else:
    print(" Cores da bandeira desconhecidas para o país indicado.")
