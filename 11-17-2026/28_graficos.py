import matplotlib.pyplot as plt

edificios = ["Oficinas", "Almacén", "Fábrica", "Tienda"] 
consumo = [350, 220, 580, 190] 
plt.pie( 
    consumo, 
    labels=edificios, 
    autopct="%1.1f%%" #muestra los porcentajes dentro del grafico
    )
plt.title("Distribución del consumo") 
plt.show() 