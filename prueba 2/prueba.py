nombre_cliente = "Pedro Ramirez"
tienda = "falabella"
jeans_precio = 125.000
camisas_precio = 45.000
polo_precio = 30.000

cantidad_jeans = 2
cantidad_camisas = 2
cantidad_polo = 1

total_jeans = cantidad_jeans * jeans_precio
total_camisas = cantidad_camisas * camisas_precio
total_polo = cantidad_polo * polo_precio

total_compra = total_jeans + total_camisas + total_polo

descuento_polo = 0
if cantidad_polo > 0:
    descuento_polo = total_polo * 0.05
    
descuento_compra = 0
if total_compra > 200000:
    descuento_compra = total_compra * 0.30
    
#total descuento 
total_descuento = descuento_polo + descuento_compra

#total a pagar
total_a_pagar = total_compra - total_descuento

print (f"factura de compra - {tienda}")
print (f"Cliente: {nombre_cliente}\n")
print (f"2 jeans: ${total_jeans}")
print (f"2 camisas: ${total_camisas}")
print (f"1 camisa tipo polo: ${total_polo}\n")
print (f"descuento por compra superior a 200 mil pesos: -${descuento_compra}")
print (f"total descuentos: -$ {total_descuento: ,}\n")
print (f"total a pagar: ${total_a_pagar: ,}")




        