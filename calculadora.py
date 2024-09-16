def calcular_precio_casa(precio_base, adicionales, incluir_cuatro_por_mil=True):


  # Aplicar descuento del 5% al precio base
  precio_base_descontado = precio_base * 0.05

  # Calcular el costo total de los adicionales
  costo_adicionales = sum(adicionales.values())

  # Calcular el valor sujeto a impuestos (base imponible)
  valor_imponible = precio_base_descontado + costo_adicionales

  # Calcular el IVA (19%)
  iva = valor_imponible * 0.19

  # Calcular el 4x1000 (0.4%) si es necesario
  cuatro_por_mil = valor_imponible * 0.004 if incluir_cuatro_por_mil else 0

  # Calcular el precio total sin 4x1000
  precio_total_sin_4xmil = valor_imponible + iva

  # Calcular el precio total con 4x1000
  precio_total = precio_total_sin_4xmil + cuatro_por_mil

  # Imprimir un resumen detallado
  print("Precio base con descuento:", precio_base_descontado)
  print("Costo de adicionales:", costo_adicionales)
  print("IVA (19%):", iva)
  print("Precio total sin 4x1000:", precio_total_sin_4xmil)
  if incluir_cuatro_por_mil:
    print("4x1000 (0.4%):", cuatro_por_mil)
    print("Precio total con 4x1000:", precio_total)
  else:
    print("Precio total:", precio_total_sin_4xmil)

  return precio_total

# Solicitar el precio base de la casa al usuario
precio_base = float(input("Ingrese el precio base de la casa: "))

# Solicitar los costos adicionales (opcional)
adicionales = {}
while True:
  adicional = input("Ingrese un costo adicional (o 'fin' para terminar): ")
  if adicional.lower() == "fin":
    break
  costo = float(input("Ingrese el costo de {}: ".format(adicional)))
  adicionales[adicional] = costo

# Calcular el precio total y mostrarlo
precio_final = calcular_precio_casa(precio_base, adicionales)