### Fechas ###

from datetime import datetime

ahora = datetime.now()

def imprime_fecha(fecha):
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)
    print(fecha.timestamp()) #momento justo actual

imprime_fecha(ahora) #llamamos a la función para ejectuarla con el valor ahora

year_2026 = datetime(2026, 1, 1) #año, mes, día. Utilizamos otro momento que nosotros mismos configuramos

imprime_fecha(year_2026) #ahora la función se ejecuta con el valor year_2026

from datetime import time

hora_actual = time(21,6,30) # time hay que definilo ya que no coge valores automaticamente. También time puede estar vacío
print(hora_actual.hour)
print(hora_actual.minute)
print(hora_actual.second)

from datetime import date

fecha_actual = date(2026,1,1) #Igual que time, date hay que definirlo
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

fecha_actual = date.today() #Definimos date automáticamente para que coja los valores de hoy
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

fecha_actual = date(fecha_actual.year, fecha_actual.month + 1, fecha_actual.day) #Sumamos 1 al mes actual
print(f"El mes actual sumado 1 es: {fecha_actual.month}")

diferencia = year_2026 - ahora #Se pueden restar fechas si son del mismo tipo
print(diferencia)

fecha_actual = date.today()
diferencia = year_2026.date() - fecha_actual
print(diferencia)  #La diferencia con la resta anterior es que con date.today no calcula el tiempo y datetime de la variable ahora si calcula el tiempo del día actual

from datetime import timedelta # timedelta irve para operar con fechas

ini_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)
print(ini_timedelta)
print(end_timedelta)
print(end_timedelta - ini_timedelta)
print(end_timedelta + ini_timedelta)
print(end_timedelta / ini_timedelta) #Realmente no tiene mucho sentido dividir fechas ... pero lo admite Python
#print(end_timedelta * ini_timedelta) No se pueden multiplicar



