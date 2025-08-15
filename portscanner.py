import socket


# Get user input for the target host
HOST = input("Enter the host to scan:  ")
# Ports 1-1023 are well-known ports commonly used by system processes and services
PORTS = range(1, 1024)

for port in PORTS:
    # Create a socket object for each port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
    sock.settimeout(1) # Set a timeout for socket operations
    result = sock.connect_ex((HOST, port)) # Attempt to connect to the specified host ports
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

