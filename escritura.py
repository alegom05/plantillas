def genera_labs():
    codigo_inicial = 20230001
    with open("notas_labs.csv", "w+") as f:
        cabecera = "codigo,"
        cabecera += ",".join([f"lab_{i}" for i in range(1, 15)])
        cabecera += "\n"
        f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},"
            linea += ",".join([f"{random.randint(0, 20)}" for i in range(1, 15)])
            linea += "\n"
            f.write(linea)