def header():
    return '''\
========================================
        Welcome to Blackjack       
========================================

Please, tell us your name: '''


def scoreboard(players):
    message = '''\
========================================
               Scoreboard
----------------------------------------
'''
    message += "\n".join(f"{player.name}: {player.wins}" for player in players)
    message += '''\
----------------------------------------
'''
    message += "\n".join(show_hand(player) for player in players)
    message += '''\
========================================

'''
    return message


def show_hand(player):
    cards = " ".join(card[1] for card in player.hand)
    return f'''
Player    : {player.name}
Hand Value: {player.hand_value()}
Cards     : {cards}
'''


def won():
    return '''\
========================================
             You Won!
========================================
'''


def lost():
    return '''\
========================================
            You lost!
========================================
'''
