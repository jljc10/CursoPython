numero = int(input("Ingrese su numero: "))
divisible = numero%2
if divisible == 0:
    valor = "par"
else: valor = "impar"

print(f"El número {numero} es {valor}.")