#promedio varias filas

with open('prueba.csv',"r") as archivo:
    cont=archivo.read()
print(f"contenido \n{cont}")

lines=cont.split("\n")
print(f"lineas {lines}")

campos=[]
for line in lines[1:]:
    line=line.strip()
    print(f"Linea {line}")
    campo=line.split(";")
    print(f"Campo {campo}")#campo=['a','b']
    campos.append(campo)
print(f"Campos {campos}")

#promediar todos los campos[1]
s=0
for campo in campos:
    if len(campo) >= 2: ##importante
        s+=float(campo[1])
    s=s/len(campo)
print(f"promedio lineas: {s}")

#promediar todos los campos por separado
for campo in campos:
    if len(campo) >= 2: ##importante
        s+=float(campo[1])+float(campo[2])
    s=s/len(campo)
    print(f"promedio por línea: {s}")

#gg