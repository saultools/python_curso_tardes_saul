# 1+2+3+4.....¿hasta que número tendremos que llegar
#para que la suma alcance o supere el valor 1000?

#solución de Saúl
limitador=1000
num_inicio=0
sumador=0

while num_inicio<limitador:
    num_inicio=num_inicio+1
    sumador=sumador+num_inicio
print(f"hay que llegar al número {sumador}")


#solución de Antonio
total=1000
suma=0
num=0;
while suma<total:
    num=num+1
    suma=suma+num
print("Hay que sumar hasta el ",num)