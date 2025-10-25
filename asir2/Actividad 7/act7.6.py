'''
Simula una compra básica:
1. Pide el precio de un producto
2. Pide la cantidad de unidades
3. Pide el porcentaje de descuento (0-100)
4. Calcula:
    Subtotal (precio * cantidad)
    Descuento en euros
    Total a pagar
5. Muestra todos los valores con 2 decimales
'''

precio = float(input ("Cual es el precio del producto: "))
cantidad = int(input ("Cuantas unidades quieres: "))
descuento = int(input ("Cual es el descuento a aplicar: "))

print ("---Ticket de la compra---")
print ("-------------------------")
ptotal = precio * cantidad
dtotal = (ptotal * descuento) / 100
ppagar = ptotal - dtotal
print (f"Precio total: {ptotal} €")
print (f"Descuento: {dtotal} %")
print (f"Neto a pagar: {ppagar} €")