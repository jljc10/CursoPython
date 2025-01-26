lista_vacia = [] 
listado_numeros = [1, 2, 3, 4, 5]
lista_elementos = [1, "dos", 3.0, True]

#tipo de lista es siempre list

type(lista_vacia)

#acceso a los datos de una lista
## en python el primer elemento comienza con el índice 0
print(lista_elementos[0]) #me trae el elemento 1

## en python el último elemento es -1, el penúltimo es -2; y así sucesivamente
print(lista_elementos[-1])

#modificar elementos de una lista
listado_numeros[0] = 10
print(listado_numeros)
## lo que hice fue colocar el índice y darle un valor, de esa manera se cambia

# suma de listas (concatenar listas)
lista_combinada = lista_elementos + listado_numeros
print(lista_combinada)

#OPERACIONES BÁSICAS DE LISTS

##Agregar un elemento al final de la lista: append()
lista_elementos.append(6)
print(lista_elementos)

##contar cuantos elementos hay en una lista: count()
cantidad = lista_elementos.count(6)
print(cantidad)

##remover elementos de una lista
lista_elementos.remove(6) ## aquí elimina la primera coincidencia
print(lista_elementos)

##como obtener le índice de un elemento de la lista
lista_elementos.index(3.0)

