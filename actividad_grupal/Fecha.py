meses = {
    
    "Enero": 1,
    "enero": 1,
    "Febrero": 2,
    "febrero": 2,
    "Marzo": 3,
    "marzo": 3,
    "Abril": 4,
    "abril": 4,
    "Mayo": 5,
    "mayo": 5,
    "Junio": 6,
    "junio": 6,
    "Julio": 7,
    "julio": 7,
    "Agosto": 8,
    "agosto": 8,
    "Septiembre": 9,
    "septiembre": 9,
    "Octubre": 10,
    "octubre": 10,
    "Noviembre": 11,
    "noviembre": 11,
    "Diciembre": 12,
    "diciembre": 12
}

print("")
Fecha = input("Introduce la fecha: ")
print("")

partes = Fecha.split(", ")
dia = partes[0]  
mes_año = partes[1].split(" ")  

mes = mes_año[0]  
año = mes_año[1]  


mes_num = meses[mes]

print(f"{dia} {mes_num} {año}")
print("")