"""calcula con numpy:

1.Consumoo total semanal
2.Consumo medio diario
3.Días con mayor y menor consumo
4.Días con consumo superior a la media
5.Porcentaje de consumo cada día
6.Días con un consumo 20% inferior a la media
7.Coste total, sabiendo que de L-V el coste del Kw/h es de 0,02 y en fin de seman ed del 0,018
8. mostrar consumo e cada día, en €. 
"""
#datos
consumos=[1250,1680,980,1450,1520,1100,1600]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

import numpy as np
consumos = np.array([1250, 1680, 980, 1450, 1520, 1100, 1600])
dias = np.array(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])


total_semanal = np.sum(consumos) #1
media_diaria = np.mean(consumos) #2

dia_mayor = dias[np.argmax(consumos)] #3
dia_menor = dias[np.argmin(consumos)] #3

dias_superiores = dias[consumos > media_diaria] #4
porcentajes = (consumos / total_semanal) * 100 #5
dias_inferiores_20 = dias[consumos < (media_diaria * 0.8)] #6

precios = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.018, 0.018])
coste_total = np.sum(consumos * precios) #7

# función np.zip #8

print(f"1. Consumo total semanal: {total_semanal} kWh")
print(f"2. Consumo medio diario: {media_diaria:.2f} kWh")
print(f"3. Día mayor: {dia_mayor}, Día menor: {dia_menor}")
print(f"4. Días superiores a la media: {dias_superiores}")
print(f"5. Porcentajes diarios: {np.round(porcentajes, 2)}")
print(f"6. Días 20% inferiores a la media: {dias_inferiores_20}")
print(f"7. Coste total: {coste_total:.2f} €")


# función np.zip #8 ejemplo: 
a = np.array([1, 3, 5, 7])
b = np.array([2, 4, 6, 8])
c = np.array(list(zip(a, b)))
print(c)