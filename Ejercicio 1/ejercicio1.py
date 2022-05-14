# Ejercicio 1
# Enunciado del ejercicio:

# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
#  No debería haber países repetidos (haz uso de set). Finalmente, 
#  muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


lista = input("Ingrese una lista de paises separados por coma:\n")
lista_paises = [pais for pais in lista.split(",")]
print(",".join(sorted(set(lista_paises))))


