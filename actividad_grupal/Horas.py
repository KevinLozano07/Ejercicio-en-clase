print("")

Tiempo = input("Ingrese las horas y los minutos (HH:MM) ")

print("")

Horas = int(Tiempo[:2])
Minutos = Tiempo[3:]

if Horas == 0:
    Periodo = "AM"
elif Horas < 12:
    Periodo = "AM"
elif Horas == 12:
    Periodo = "PM"
else:
    Periodo = "PM"


Horas = Horas - 12


Horas_str = str(Horas)

Reloj = Horas_str + ":" + Minutos + " " + Periodo

print(Reloj)

print("")