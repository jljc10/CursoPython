numero = int(input("Ingrese numero: "))
listadodivisores = []
for i in  range(numero):
    div = i + 1

    if numero%div == 0:
        listadodivisores.append(div)
    pass

print(listadodivisores)