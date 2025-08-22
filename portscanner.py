import socket
from concurrent.futures import ThreadPoolExecutor



def scan_port(target_ip, port):
    """Function to scan a single port on the specified host."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((target_ip, port))  # Attempt to connect to the specified host and port
    if result == 0:
        try:
            service_name = socket.getservbyport(port)  # Get the service name for the port
            print(f"Port {port} is open ({service_name}) on {target_ip}.")
        except:
            print(f"Port {port} is open (unknown service) on {target_ip}.")
    sock.close()


# Get user input for the target host
HOST = input("Enter the host to scan:  ")
# Ports 1-1023 are well-known ports commonly used by system processes and services
PORTS = range(1, 1024)


try:
    # Attempt to resolve the host to an IP address
    target_ip = socket.gethostbyname(HOST)
except socket.gaierror:
    print(f"Hostname {HOST} could not be resolved. Exiting.")
    exit()


MAX_THREADS = 64  # Maximum number of threads to use for scanning
user_threads = int(input(f"Enter the number of threads to use (max {MAX_THREADS}): "))

if user_threads > MAX_THREADS:
    print(f"Number of threads exceeds maximum limit using {MAX_THREADS}.")
    user_threads = MAX_THREADS
elif user_threads < 1:
    print("Defaulting to 1 thread.")
    user_threads = 1

with ThreadPoolExecutor(max_workers=user_threads) as executor:
    # Submit port scanning tasks to the thread pool
    for port in PORTS:
        executor.submit(scan_port, target_ip, port)