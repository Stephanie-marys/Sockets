# cliente.py
import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Criar socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conecta ao servidor

    while True:
        mensagem = input("Digite uma mensagem (ou 'sair'): ")
        if mensagem.lower() == 'sair':
            break
        s.sendall(mensagem.encode())       # Envia mensagem ao servidor
        dados = s.recv(1024)               # Recebe resposta
        print(f"Resposta do servidor: {dados.decode()}")