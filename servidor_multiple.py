import socket
from concurrent.futures import ThreadPoolExecutor
import threading
lock=threading.Lock()
host = '127.0.0.1'
port = 5001

if __name__=='__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0',5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind((host, port))

    sock.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    lavadora=["lavadora",5]
    refrigerador=["refrigerador",3]
    aspiradora=["aspiradora",2]
    licuadora=["licuadora",4]

        #     #stock = {"lavadora": 5, "refrigerador”: 3, "aspiradora”: 2, "licuadora”: 4}

    def operacion_producto(arreglo, conn):
        with lock:
            arreglo[1]-=1
            print(arreglo[1])
            if arreglo[1]>=1:
                conn.sendall(b'1')
                print("envió")
            else:
                conn.sendall(b'0')
    
    def eleccion_producto(rpta, conn):
        if rpta==lavadora[0]:
            operacion_producto(lavadora, conn)
        elif rpta==refrigerador[0]:
            operacion_producto(refrigerador, conn)
        elif rpta==aspiradora[0]:
            operacion_producto(aspiradora, conn)
        else:
            operacion_producto(licuadora, conn)
    
    def handle_client(conn, address):
        print(f"Conexión entrante desde {address}")

        while True:
            rpta = conn.recv(1024).decode('utf-8')
            # if not rpta:
            #     break  # Si no hay datos, salir del bucle interno
            eleccion_producto(rpta, conn)

    workers = 3
    with ThreadPoolExecutor(max_workers=workers) as executor:
        while True:
            conn, client_address = sock.accept()
            print(f"Conexión entrante desde {client_address}")
            executor.submit(handle_client, conn, client_address)
        #try:
        #except KeyboardInterrupt:
        #   print("Interrupción")
        #finally:
        #   conn.close

    #conn.close()


    #envia
    # conn.sendall(dato.encode('utf-8'))

    #recibe
    # rpta=conn.recv(1024).decode('utf-8')

    #convertir a cadena de texto
    # str()