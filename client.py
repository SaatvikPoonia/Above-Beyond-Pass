import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server address and port
server_address = ('localhost', 5000)

# Start the conversation
while True:
    # Start the conversation
    print('Starting conversation...')

    # Send a "Hello" message to the server
    message = 'Hello'
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Wait for a question from the server
    data, server_address = client_socket.recvfrom(1024)
    question = data.decode('utf-8')

    # Print the question and ask for a response
    print(f'Received message from server {server_address}: {question}')
    response = input('Enter your Name: ')

    # Send the response to the server
    client_socket.sendto(response.encode('utf-8'), server_address)

    # Wait for a message containing the response from the server
    data, server_address = client_socket.recvfrom(1024)
    message = data.decode('utf-8')

    # Print the message containing the response and the server's instructions
    print(f'Received message from server{server_address}: {message}')

    # Ask the user to quit or continue
    choice = input('Do you want to continue (y/n)? ')

    # If the user chooses to quit, break out of the loop and end the conversation
    if choice.lower() == 'n':
        print('Conversation ended.')
        break
    else:
        continue

# Close the socket
client_socket.close()
