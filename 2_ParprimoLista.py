# ------------------------------------------------------ #
# Este va a ser un programa para ver si el número es:    #
#             par o impar y si es primo.                 #
# ------------------------------------------------------ #

#################################################################
# Este algortmo comprobará si es par o impar y si es primo o no #
#################################################################
# El operador % toma la parte decimal de la división, si dividimos x
# entre 2 y el resultado es 0 significa que es par.
def par_primo(x):
    if x == 2:
        return "Es Par y Primo" 
    elif x%2 == 0: 
        return "Es Par"
    # Este es el caso donde es impar, ya que el resultado de la división 
    # anterior es diferente de 0. Vamos a comprobar si es primo.
    else: 
        # Un número primo es uno que solo se puede dividir entre el mismo y 1. 

        # Primero asignamos a la variable mit_x la parte entera de x entre 2, ya que
        # que un número no puede ser divisible por otro más grande que su mitad.
        # Asignamos la variable "primo", por defecto será de verdadero.
        # Para que no se divida entre 1 el rango será hasta mit_x - 1.

        # En cada ciclo se va a dividir el número x entre mit_x menos el número de ciclo 
        # en el que se encuentre (si es el ciclo 0, no se restara nada, si es el ciclo 1, se le 
        # restara 1 al valor mit_x, y así sucesivamente), si en alguno de estos ciclos el resultado
        # es un entero, entonces se comprueba que no es un número primo (ya que es divisible) y se
        # cambia el valor de "primo" a False, además de parar el ciclo.
        primo = True
        mit_x = x//2
        for num in range(mit_x-1):
            if x%(mit_x-num) == 0:
                primo = False
                break
        # Por ultimo se comprueba si es primo o no y se manda el mensaje correspondiente.
        if primo == True:
            return "Es impar y Primo"
        else:
            return "Es impar y NO Primo"


reversa = []

seleccion = int(input("Ingrese 1 si quiere ver la propiedad de un solo número o 2 si quiere hacer una lista descendente: "))
numero = int(input("ingrese un número: "))

if seleccion == 1:
    print(par_primo(numero))
elif seleccion == 2:
    for x in range(numero - 1):
        num_list = numero - x
        reversa.append((num_list, par_primo(num_list)))

r = reversa[::-1]

for z in r:
    print(z)






