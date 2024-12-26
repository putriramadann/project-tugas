import socket

# Membuat client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Hubungkan ke server dengan IP dan port
    localhost_ = '192.168.219.102'  # Ganti dengan IP server Anda
    server_port = 8080
    print(f"Connecting to server {server_ip}:{server_port}...")
    client_socket.connect((server_ip, server_port))
    print("Connected to the server.")

    # Mengirim pesan ke server
    message = "Hello from Client!"
    client_socket.sendall(message.encode())  # Mengirim data sepenuhnya
    print(f"Sent to server: {message}")

    # Menerima respons dari server
    response = client_socket.recv(4096)  # Buffer size diperbesar menjadi 4096 byte
    print(f"Response from server: {response.decode()}")

except ConnectionRefusedError:
    print("Connection refused. Please check if the server is running and reachable.")
except socket.gaierror:
    print("Invalid server address. Please ensure the IP and port are correct.")
except TimeoutError:
    print("Connection timed out. Ensure the server is reachable.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Menutup koneksi
    print("Closing the connection...")
    client_socket.close()

