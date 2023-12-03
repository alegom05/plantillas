import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)

    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)

    while(1):

        a=input("Ingrese el nombre del electrodoméstico: ")

        if a=="lavadora":
            sock.sendall(b'lavadora')
        elif a=="refrigerador":
            sock.sendall(b'refrigerador')
        elif a=="aspiradora":
            sock.sendall(b'aspiradora')
        else:
            sock.sendall(b'licuadora')

        #Segunda parte
        rpta=sock.recv(SOCK_BUFFER).decode('utf-8')
        print("recibió")
        msg1="Producto en stock. Pedido procesado"
        msg2="Producto agotado. Pedido procesado"
        if rpta=="1":
            print(msg1)
        else:
            print(msg2)

    sock.close()



    #envia
    # sock.sendall(dato.encode('utf-8'))

    #recibe
    # rpta=sock.recv(SOCK_BUFFER).decode('utf-8')
    # if not rpta:
    #   break

    # sock.close()