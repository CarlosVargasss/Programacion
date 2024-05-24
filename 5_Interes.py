cantidad = float(input("cantidad: "))
interes = float(input("interes anual: "))
años = float(input("años: "))

capital = cantidad * ((interes+1) ** años)

print(round(capital,2))