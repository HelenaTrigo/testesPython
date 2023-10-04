morada = input("Indique a sua morada:\n")
cod_postal = input("Indique o seu código postal:\n")

morada_comp = morada + ", " + cod_postal

print("Morada Completa: ", morada_comp)

# ex.16
PI = 3.14759
raio = float(input("Indique o valor do raio:\n"))

print(F"Área do círculo é {PI * raio ** 2:.2f}")

# ex.22
PIN_SIST = "sysPin"

pin = input("Introduza o pin: ")

if PIN_SIST == pin:
    print("Pin está correto")
else:
    print("Pin está incorreto!")
