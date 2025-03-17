
# Multiplayer Blackjack Game

A multiplayer Blackjack game implemented in Python using sockets for client-server communication. Players can connect to the server, play against the dealer, and compete in a turn-based game where they can draw cards and try to reach 21 points without going over.

## Features

- **Multiplayer**: Supports one player and one dealer (the server acts as the dealer).
- **Card Drawing**: Players can choose to draw cards or stand.
- **Turn-Based Gameplay**: The player and dealer take turns drawing cards.
- **Game Logic**: Includes game logic for calculating card values, handling Aces, and determining the winner.
- **Networking**: Player connects to the server over a TCP connection.
- **UI**: Displays game status, player's hand, and results via the console.

## Components

- **Client**: The client allows players to connect to the server, interact with the game, and view the results.
- **Server**: The server listens for incoming connections, manages game state, handles multiple players using threads, and sends updates to clients.
- **Game**: The game logic where the round is managed, cards are dealt, and win/loss conditions are checked.
- **Player**: Defines player attributes such as name, hand, score, and provides methods for adding cards, calculating hand value, and determining if the player has lost.
- **UI**: Displays user interfaces for the game, including prompts, player hands, and results.

## Requirements

- Python 3.x
- No external libraries required (uses built-in Python modules: `socket`, `threading`, `argparse`, `os`)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/BlackJack.git
   cd BlackJack
   ```

2. Run the server script:
   ```sh
   python server.py
   ```

3. Run the client script:
   ```sh
   python client.py
   ```

## Usage

### Server
- Start the server on your host machine. By default, it listens on `localhost` and port `3000`, but you can specify a custom IP address and port using the command-line options:
  ```sh
  python server.py -i <host-ip> -p <port>
  ```

### Client
- Start the client and connect to the server. The client will ask for your name, and then you'll play against the dealer.
  ```sh
  python client.py -i <server-ip> -p <port>
  ```

### Game Flow

1. When the client connects, the server sends a welcome message and prompts the client for their name.
2. The game starts with the dealer and player being dealt two cards each.
3. The player decides whether to draw another card or stand.
4. The dealer draws cards according to the rules (e.g., draws if the total value is below 17).
5. The game ends when the player or dealer goes over 21, or when the round is completed.
6. The result (win or loss) is displayed, and the client can choose whether to continue or exit.

## Game Rules

- **Card Values**: The value of the cards is as follows:
  - Cards 2-10 are worth their face value.
  - Face cards (Jack, Queen, King) are worth 10 points.
  - Aces can be worth either 1 or 11 points (whichever benefits the player more).
  
- **Winning**: The player wins if they have a hand value closer to 21 than the dealer without going over 21. If the dealer exceeds 21, the player wins.

## Future Improvements

- **Multiple Players**: Extend the game to support more than one player.
- **GUI**: Implement a graphical user interface for a better user experience.
- **Database Integration**: Store player stats and game history in a database.
