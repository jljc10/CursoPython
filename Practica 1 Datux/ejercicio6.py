edad = int(input("Ingrese su edad: "))

if edad < 18:
    legalidad = "menor"
else:
    legalidad = "mayor"
print(f"Tiene {edad}; por lo tanto es {legalidad} de edad")
