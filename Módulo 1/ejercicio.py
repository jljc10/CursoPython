import random
asesor = input("Ingrese nombre de la tienda: ")
cliente = input("Ingrese DNI del cliente: ")
nro_cuotas = 36


risk =random.random()
print("El riesgo es: {}".format(risk))

if risk >= 0.5:
    print("Lamentablemente no contamos con alguna oferta para usted.")

salarioinput= float(input("Ingrese salario del cliente: "))
propiedades = input("Cuenta con propiedades (S/N): ")
monto_propiedad = 0.0

if propiedades.upper() == "S":
    monto_propiedad = float(input("Ingrese la valuación de la propiedad: "))
if risk <= 0.3:
    if propiedades.upper() == "S":
        monto_aprobado = 36*0.5*salarioinput
    elif propiedades.upper() == "N":
      monto_aprobado = 36*0.2*salarioinput  
        
elif risk <=0.5:
     monto_aprobado = 36*0.2*salarioinput

print(f"El monto aprobado es {monto_aprobado}")






