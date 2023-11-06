import socket

host = '127.0.0.1'
port = 5001

if __name__=='__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0',5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind((host, port))

    sock.listen(5)

    print(f"Servidor de eco escuchando en {host}:{port}")

    while True:
        conn, client_address = sock.accept()
        print(f"Conexión entrante desde {client_address}")

        #try:
        #except KeyboardInterrupt:
        #   print("Interrupción")
        #finally:
        #   conn.close

    #conn.close()

    #envia
    # conn.sendall(codigo.encode('utf-8'))

    #recibe
    # dato=conn.recv(1024).decode('utf-8')
