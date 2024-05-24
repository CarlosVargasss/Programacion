cantidad = float(input("cantidad: "))
interes = 0.1/12


for x in range(12*20):
    capital = (cantidad * (x+1)) * ((interes+1) ** (x+1))
print(round(capital,2))