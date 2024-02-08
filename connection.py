import bluetooth

'''
code provided by my friend Charles Gipty
you can find him on chat.openai.com
'''

def start_exchange(server_socket):
    client_socket, address = server_socket.accept()
    print("Accepted connection from", address)
    return client_socket

def receive_message(client_socket):
    message = client_socket.recv(1024).decode()
    print("Received:", message)
    return message

def send_message(client_socket, message):
    client_socket.send(message.encode())
    print("Sent:", message)

def main():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]

    print("Waiting for connection on RFCOMM channel", port)

    client_socket = start_exchange(server_socket)

    # Step 1: Receive start message from 'a'
    receive_message(client_socket)

    # Step 2: Send acknowledgement
    send_message(client_socket, "ack")

    # Step 3: Receive wireless connection info from 'a'
    connection_info = receive_message(client_socket)

    # Step 4: Send acknowledgement
    send_message(client_socket, "ack")

    # Step 5: Simulate connection attempt result
    connection_result = "Connection successful"  # Simulate connection attempt result
    send_message(client_socket, connection_result)

    # Step 6: Wait for message to end Bluetooth connection
    receive_message(client_socket)

    # Step 7: Send message to end Bluetooth connection
    send_message(client_socket, "End connection")

    # Closing connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
