N1 = int(input("Ingrse el primer numero: "))
Ni = range(1, N1 + 1)
Ne = ""


for i in Ni:
    Ne += str(i) + " "
    
Ne = Ne[::-1]   
print(Ne) 