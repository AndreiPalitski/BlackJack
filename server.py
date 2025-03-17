import argparse
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import logging

from game import Game
import ui as UI


logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="Host's IPv4", type=str, required=False)
    parser.add_argument("-p", "--port", help="Port", type=int, required=False)
    args = vars(parser.parse_args())

    HOST = args["ip"] if args["ip"] is not None else "localhost"
    PORT = args["port"] if args["port"] is not None else 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.bind((HOST, PORT))
        tcp_socket.listen()

        logging.info("Waiting for new connections...")
        with ThreadPoolExecutor(max_workers=10) as executor:
            while True:
                logging.info(f"Active sub-threads: {threading.active_count() - 1}")
                connection, client_address = tcp_socket.accept()
                executor.submit(client_thread, connection, client_address)

def client_thread(connection, client_address):
    try:
        with connection:
            connection.send(UI.header().encode())
            player_name = connection.recv(1024).decode()

            game = Game(player_name)

            while True:
                game.start_round()
                player_turn = True
                while True:
                    connection.send(str(game).encode())
                    connection.recv(1024)
                    if player_turn:
                        connection.send("[Player's turn]".encode())
                        if connection.recv(1024).decode() == "True":
                            if game.give_card(0):
                                continue
                        player_turn = False
                    else:
                        if game.dealer_needs_buy():
                            connection.send("[Dealer's turn]".encode())
                            connection.recv(1024)
                            game.give_card(1)
                        else:
                            connection.send("[End of round]".encode())
                            connection.recv(1024)
                            if game.dealer_won():
                                connection.send("Sorry, you lost this time...".encode())
                            else:
                                connection.send("You won!".encode())
                            break

                if connection.recv(1024).decode() == "False":
                    break
    except (ConnectionResetError, BrokenPipeError) as e:
        logging.error(f"Error with client {client_address}: {e}")

if __name__ == "__main__":
    main()