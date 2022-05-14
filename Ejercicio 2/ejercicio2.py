# Ejercicio 2
#Enunciado del ejercicio:
#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista 
# pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]
lista_impares = list(filter(lambda x: x %2 != 0, lista))
print(lista_impares)
print(f"Suma impares: {reduce(lambda x,y: x+y, lista_impares)}")