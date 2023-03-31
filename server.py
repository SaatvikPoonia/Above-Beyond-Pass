import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('', 5000)
server_socket.bind(server_address)

print('Server is running...')

# Wait for incoming messages
while True:
    data, address = server_socket.recvfrom(1024)
    message = data.decode('utf-8')

    # Print the message and sender's address
    print(f'Received message from client {address}: {message}')

    # Respond with a question
    response = 'Hello, What"s your name ? '
    server_socket.sendto(response.encode('utf-8'), address)

    # Wait for a response from the client
    data, address = server_socket.recvfrom(1024)
    response = data.decode('utf-8')

    # Print the response
    print(f'Received response from client {address}: {response}')

    # Send a message containing the response
    message = f'Hello {response}, Welcome to SIT202'
    server_socket.sendto(message.encode('utf-8'), address)



