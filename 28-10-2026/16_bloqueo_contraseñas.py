# crea un bloqueador de contraseñas, despues de N intentos (3), con autenticación si se acierta la contraseña

#solución de Saúl
contr_usuario=1234
max_tries=3
intentos=0
contr_intento=input("introduce tu contraseña: ")

if contr_intento==contr_usuario:
    print("autenticado, buenvenid@ ")
while intentos<max_tries and contr_intento!=contr_usuario:
    intento=input("pruebe otra vez: ")
    intentos=max_tries-1 
else:
    print(f"no autenticado ")

# tip de Antonio:
acertado=False


#solución de Antonio:
password="admin"
intentos=3
acertado=False
while intentos>0 and not acertado:#acertado==False
    contra=input("Introduce contraseña ")
    if contra==password:
        acertado=True
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
if acertado:
    print("Usuario válido!")
else:
    print("Usuario no válido!") 