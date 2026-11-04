import datetime
print(f"fecha de hoy; {datetime.date.today()}")
print(f"hora actual: {datetime.datetime.now()}")

f_posterior=datetime.datetime.now()+datetime.timedelta(days=20,hours=3)
print(f_posterior)

fechahora_actual=datetime.datetime.now()
print(f"La fecha y hora actuales: {datetime.datetime.strftime(fechahora_actual,"%d/%m/%Y - %H:%M:%S")}")

fecha1="10/11/2003"
fecha2="25/04/2002"
fecha1=datetime.datetime.strptime(fecha1,"%d%m%Y")
fecha2=datetime.datetime.strptime(fecha2,"%d%m%Y")
if fecha1 < fecha2:
    print(f"la mas antigua es {fecha1}")
else: 
    print(f"la mas antigua es {fecha2}")
