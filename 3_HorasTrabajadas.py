
horas = int(input("Introduce el número de horas trabajada: "))
coste = int(input("Introduce tu valor por hora: "))

total = 0


# agrega un aumento si trabajó más de 8 horas.
if horas > 8:
    horas_extra = horas - 8 

    pago_normal = 8 * coste
    pago_extras = horas_extra * (coste*1.75)

    total = pago_normal + pago_extras
else:
    total = horas * coste


print("Usted generó", total)
