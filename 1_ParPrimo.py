# ------------------------------------------------------ #
# Este va a ser un programa para ver si el número es:    #
#             par o impar y si es primo.                 #
# ------------------------------------------------------ #

#################################################################
# Este algortmo comprobará si es par o impar y si es primo o no #
#################################################################
# El operador % toma la parte decimal de la división, si dividimos x
# entre 2 y el resultado es 0 significa que es par, por ende tampoco es
# primo. 
def par_primo(x):
    if x==2:
        print(f"El número {x} es par y primo")
        return(0)
    elif x%2 == 0: 
        print(f"El número {x} es par")
        return(1)
    # Este es el caso donde es impar, ya que el resultado de la división 
    # anterior es diferente de 0, pero tambien vamos a comprobar si es primo.
    else: 
        # Un número primo es por definición un número que solo se puede dividir
        # entre el mismo y 1. 

        # Primero asignamos a la variable mit_x la parte entera más pequeña de
        # la división entre 2 de x, esto ya que un número no puede ser divisible
        # por un numero más grande que su mitad. 
        mit_x = x//2

        # Creamos las variable i para crear un ciclo while donde se le ira sumando
        # 1 en cada ciclo que se realice hasta cumplir con la condición propuesta.
        # Creamos la variable primo, que sera un boleano, la condición por defecto 
        # será de verdadero, en el ciclo se cambiara si se comprueba que no es primo.
        i=0
        primo = True


        # Este ciclo ira hasta que i+1 (esto para que no se divida entre 1 en el ultimo ciclo, 
        # ya que ningun numero cumpliría la condición para ser primo) sea menor a mit_x. 

        # En cada ciclo se va a dividir el número x entre mit_x menos el número de ciclo 
        # en el que se encuentre (si es el ciclo 0, no se restara nada, si es el ciclo 1, se le 
        # restara 1 al valor mit_x, y así sucesivamente), si en alguno de estos ciclos el resultado
        # es un entero, entonces se comprueba que no es un número primo (ya que es divisible) y se
        # cambia el valor de "primo" a False, además de parar el ciclo.
        while i+1 < mit_x:
            if x%(mit_x-i) == 0:
                primo = False
                i=mit_x
            i+=1 

        # Por ultimo se comprueba si es primo o no y se manda el mensaje correspondiente.
        if primo == True:
            print(f"El número {x} es impar y primo")
            return(2)
        else:
            print(f"El número {x} es impar pero no es primo")
            return(3)
        


# x va a ser el número que elegirá el usuario.
numero = int(input("ingrese un número: "))
par_primo(numero)