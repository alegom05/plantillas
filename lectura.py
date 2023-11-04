#promedio varias filas

with open('base.csv',"r") as archivo:
    cont=archivo.read()
print(f"contenido \n{cont}")

lines=cont.split("\n")
print(f"lineas {lines}")

k=[]
for i in range (len(lines)):

    linea=lines[i].strip()
    campos=linea.split(",")

    if len(campos) >= 5:
        s=0
        for j in range (len(campos)):
            s+=float(campos[j])
        s=s/len(campos)
        print(f"promedio linea {i+1}: {s}")

        k.append(s)

    else:
        pass

print(f"arreglo de promedios {k}")

#gg