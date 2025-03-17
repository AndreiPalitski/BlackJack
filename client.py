import argparse
import os
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="Host's IPv4", type=str, required=False)
    parser.add_argument("-p", "--port", help="Port", type=int, required=False)
    args = vars(parser.parse_args())

    HOST = args["ip"] if args["ip"] is not None else "localhost"
    PORT = args["port"] if args["port"] is not None else 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(5)  # Timeout in seconds
        try:
            connection.connect((HOST, PORT))
        except (ConnectionRefusedError, socket.timeout):
            print(f"Unable to connect to {HOST}:{PORT}. Is the server running?")
            return

        try:
            start_game(connection)
        except KeyboardInterrupt:
            print("\nGame interrupted. Closing connection.")
            connection.close()
            return


def get_yes_no_input(prompt, default=True):
    while True:
        response = input(prompt).strip().lower()
        if response in ["", "y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def start_game(connection):
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        name = input(connection.recv(1024).decode()).strip()
    except UnicodeDecodeError:
        print("Error decoding data from server.")
        return

    if not name:
        name = "You"
    connection.send(name.encode())

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print(connection.recv(1024).decode())  # Show game state
        except UnicodeDecodeError:
            print("Error decoding game state from server.")
            break
        connection.send("[OK]".encode())

        game_status = connection.recv(1024).decode()

        if game_status.startswith("[Player's turn]"):
            buy_card = get_yes_no_input("Do you want more cards? [y/n]: ")
            connection.send(str(buy_card).encode())

        elif game_status.startswith("[Dealer's turn]"):
            input("Press [Enter] to continue.")
            connection.send("[OK]".encode())

        else:
            connection.send("[OK]".encode())
            try:
                print(connection.recv(1024).decode())  # Show game result
            except UnicodeDecodeError:
                print("Error decoding game result from server.")
                break

            keep_playing = get_yes_no_input("Do you want to keep playing? [Y/n]: ")
            connection.send(str(keep_playing).encode())

            if not keep_playing:
                connection.close()
                return


if __name__ == "__main__":
    main()