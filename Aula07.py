# Ex.31
veloc = int(input("Introduza a velocidade, em Km/h, a que circula:\n"))

print("A sua condução ", end="")

if veloc < 50:
    print("é lenta.")
elif veloc == 50:
    print("é moderada.")
elif veloc < 70:
    print("é rápida.")
else:
    print("está em excesso de velocidade.\nEstá a cometer uma contraordenação ",
          "grave." if veloc <= 90 else "muito grave.", end="")  # operador ternário


