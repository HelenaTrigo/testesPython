planetas = ["Mercúrio", "Vénus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]  # cria lista
planeta_escolhido = input("Indique o nome de um planeta do sistema solar:\n").capitalize()

if planeta_escolhido in planetas:
    indice = planetas.index(planeta_escolhido)  # cria var int igual à posição da lista com o planeta escolhido

    # usa var indice para indicar o planeta antes e depois do escolhido
    if indice == 0:
        print(f"O único planeta após {planeta_escolhido} é {planetas[indice + 1]}.")
    elif indice == len(planetas) - 1:  # percorre a lista até ao elemento da última posição (tamanho da lista) menos 1
        print(f"O único planeta anterior a {planeta_escolhido} é {planetas[indice - 1]}.")
    else:
        print(f"O planeta anterior a {planeta_escolhido} é {planetas[indice - 1]}.")
        print(f"O planeta seguinte a {planeta_escolhido} é {planetas[indice + 1]}.")
else:
    print("O planeta não existe!")
