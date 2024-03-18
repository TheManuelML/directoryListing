import socket
import sys

__version__ = 1.0

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ENCODE : str = "utf-8"
BYTESIZE : int = 1024

def get_ip() -> str:
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_port() -> int:
    port = input("[?] Select a port to connect to the server: ")
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

def messages() -> None:
    print("\n[+] Write commands to execute in the server. You will recieve the output")
    print("[+] Write << close >> to end the connection")
    while True:
        message = input(">> ")
        client_server.send(message.encode(ENCODE))

        message = client_server.recv(BYTESIZE).decode(ENCODE)
        if message == "close":
            end()
        else:
            clean = regex_message(message=message)
            print(clean)

def regex_message(message : str) -> str:
    last_char = message.replace("'", "")
    no_new_liner = last_char.replace("\\n", "\n")
    return no_new_liner

def end() -> None :
    sys.exit(0)

def main() -> None:
    DEST_IP : str = get_ip()
    DEST_PORT : int = get_port()
    client_server.connect((DEST_IP, DEST_PORT))
    messages()


if __name__ == "__main__":
    main()    