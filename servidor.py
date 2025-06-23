import socket

HOST = '192.168.0.39'  # Endereço IP local (localhost)
PORT = 61840        # Porta que o servidor irá escutar

# Criar socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))       # Associa o socket ao endereço e porta
    s.listen()                 # Escuta por conexões
    print(f"Servidor ouvindo em {HOST}:{PORT}...")

    conn, addr = s.accept()    # Aceita conexão
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)  # Recebe até 1024 bytes
            if not data:
                break
            print(f"Mensagem recebida: {data.decode()}")
            conn.sendall(data)  # Envia os mesmos dados de volta (echo)