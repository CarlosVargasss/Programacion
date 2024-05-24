pan_viejo = int(input("cuantos panes de ayer: "))

precio = pan_viejo * 3.49
precio_viejo = pan_viejo * 3.49 * 0.6

print(round(precio,2))
print(round(precio - precio_viejo,2))
print(round(precio_viejo,2))