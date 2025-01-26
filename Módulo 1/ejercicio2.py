salario = float(input("Ingrese su salario: "))
tasa = 0.0


if salario <= 10000:
    tasa = 0.05
elif salario > 10000 and salario <=15000:
    tasa = 0.1
elif salario > 15000 and salario <= 20000:
    tasa = 0.15
else: tasa = 0.2

impuesto = salario * tasa

print(f"El impuesto es: {impuesto}")