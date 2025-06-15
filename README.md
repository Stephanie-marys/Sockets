# Sockets 🤖 🗣️ 
## Comunicação Cliente-Servidor com Sockets TCP

### Definições:
* TCP (Transmission Control Protocol): Protocolo orientado à conexão — garante entrega, ordem, e integridade dos dados.
* Socket: Interface de comunicação entre processos (localmente ou em rede).
* Servidor: espera conexões/recebe mensagens/envia respostas.
* Cliente: inicia a conexão com o servidor/envia mensagens/recebe respostas.

### Objetivo do projeto:
Estabelecer comunicação entre dois processos distintos (cliente e servidor), podendo estar na mesma máquina ou em máquinas diferentes conectadas em rede, usando sockets TCP.

### Instruções:

* No prompt de comando, verifique o endereço de IP. O endereço Ipv4 é o endereço local da sua máquina.
>ipconfig

* Além disso, verifique as portas disponíveis.
> netstat -an

* Importe o módulo socket: Ambos os programas precisam importar a biblioteca nativa socket.
> import socket

### Servidor:

* Crie o servidor em um arquivo .py.

* Em seguida, crie o socket TCP do servidor.
> socket.socket(socket.AF_INET, socket.SOCK_STREAM)

* Associe o socket a um endereço IP e porta
> s.bind(('192.168.0.12', 61840))

* Use o método listen para colocar um socket no modo de escuta, permitindo que ele receba conexões de entrada.
> s.listen()

* Use o método accept para aceitar conexões.
> conn, addr = s.accept()

* Use o método recv para receber dados.É possível receber até 1024 bytes.
> data = conn.recv(1024)
> conn.sendall(data)

* Use o método sendall para enviar os mesmos dados de volta.
> conn.sendall(data)

### Cliente:

* Crie o cliente em um arquivo .py.

* Em seguida, crie o socket TCP do cliente.
> socket.socket(socket.AF_INET, socket.SOCK_STREAM)

* Use o método connect para conectar ao servidor.
> s.connect(('192.168.0.12', 61840))

* Use o método sendall e o encode para enviar a mensagem ao servidor.
> s.sendall(mensagem.encode())

* Use o método recv para receber respostas.
> dados = s.recv(1024)

* Use o método decode para converter um objeto do tipo bytes em uma string.
> dados.decode()

### Teste a comunicação:

* Abra dois prompts de comando.

* No primeiro, execute o servidor.
> python servidor.py

* No segundo, execute o cliente.
> python cliente.py

### Envie mensagens:

* Digite mensagens no prompt do cliente.

* Veja as mensagens ecoadas pelo servidor.

### Encerre a comunicação:

* Digite sair no prompt do cliente para encerrar o loop e fechar a conexão.

