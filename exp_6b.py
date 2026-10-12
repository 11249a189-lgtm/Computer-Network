import socket

def file_transfer_client():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect(('localhost', 12345))

    # Get filename from user
    filename = input("Enter the filename to send: ")

    # Send filename to server
    client_socket.sendall(filename.encode())

    try:
        # Open file in binary mode
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(1024)

                if not chunk:
                    break

                # Send file data
                client_socket.sendall(chunk)

        print(f"File {filename} sent successfully.")

    except FileNotFoundError:
        print(f"File {filename} not found.")

    # Close connection
    client_socket.close()


if __name__ == '__main__':
    file_transfer_client()
