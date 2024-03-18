import socket
import subprocess
import sys

__version__ = 1.0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ENCODE : str = "utf-8"
BYTESIZE : int = 1024

def get_ip() -> str:
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_port() -> int:
    port = input("[?] Select a port to host the server: ")
    valid_port = validate_port(port=port) 
    return valid_port

def validate_port(port : str) -> int:
    try:
        port = int(port)
        if not (port <= 65535 and port >= 1):
            raise ValueError
    except (ValueError, TypeError):
        print("[!] Error: Invalid port number")
        sys.exit(1)
    return port

def set_listening_port(ip : str, port : int) -> None:
    try:
        server_socket.bind((ip, port))
    except OSError:
        print("[!] OSError: Port no allowed or already in use")
        sys.exit(1)
    server_socket.listen()
    print("[*] The server is now running")
    print("\n[+] Waiting for upcoming connections...")

def accept_connections():
    client_socket = server_socket.accept()
    print("\n[*] Connection established!!!")
    print("[+] Waiting to recieve commands... Look for the output in the client-side connection")
    return client_socket

def messages(client_socket) -> None:
    while True:
        message = client_socket.recv(BYTESIZE).decode(ENCODE)
        if message == "close":
            close_connection(client_socket=client_socket)
        
        command : list[str] = get_command(message=message)
        output : str = str(subprocess.run(command, capture_output=True))
        
        message : str = regex(output=output)
        client_socket.send(message.encode(ENCODE))

def get_command(message: str) -> list[str]:
    command : list[str] = []
    word : str = ""
    for letter in message:
        if letter == " ":
            command.append(word)
            word : str = ""
        else:
            word += letter
    command.append(word)
    return command

def regex(output : str) -> str:
    start_index = output.find("stdout=b") + len("stdout=b'")
    end_index = output.find(", stderr=b'")
    clean_output = output[start_index:end_index]
    return clean_output 

def close_connection(client_socket) -> None:
    client_socket.send("close".encode(ENCODE))
    client_socket.close()
    sys.exit(0)

def main() -> None:
    HOST_IP : str = get_ip()
    HOST_PORT : int = get_port()
    set_listening_port(ip=HOST_IP, port=HOST_PORT)
    CLI_SOCK = accept_connections()
    messages(client_socket=CLI_SOCK[0])


if __name__ == "__main__":
    main()