#! /usr/bin/env python3

import time
import random
import functools


# It's all spaghetti?
# Always has been

separator = '-' * 40 + '\n'

def blackjack():
    game = Game()

    game.display(1)
    while not game.end():
        x = input('Hit? [y/N]\n')
        if x.lower() == 'y' or x == '':
            print(separator)
            print(' ' * (int((len(separator) - len('Player Hit'))/2) - 1) + 'Player Hit\n')
            game.player.player_hit(game.deck)
        elif x.lower() == 'n':
            break
        else:
            print('invalid input')
            continue
        game.display(1)

    if game.end():
        print('You busted!')
        return 0

    print(separator)
    print(' ' * (int((len(separator) - len('Dealer reveals Card'))/2) - 1) + 'Dealer reveals card\n')
    game.display(0)
    while not game.end():
        if game.dealer.score() < 17:
            time.sleep(2.5)
            print(separator)
            print(' ' * (int((len(separator) - len('Dealer Hit'))/2) - 1) + 'Dealer Hit\n')
            game.dealer.player_hit(game.deck)
            game.display(0)
        else:
            break

    if game.end():
        print('Dealer Busted!')
        return 0

    if game.dealer.score() > game.player.score():
        print(' ' * (int((len(separator) - len('You Lost!'))/2) - 1) + 'You Lost!')
    elif game.dealer.score() < game.player.score():
        print(' ' * (int((len(separator) - len('You Won!'))/2) - 1) + 'You won!')
    else:
        print(' ' * (int((len(separator) - len('Draw!'))/2) - 1) + 'Draw!')

    return 0


class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        if self.number in ['J', 'Q', 'K']:
            self.value = 10
        elif self.number == 'A':
            self.value = 11
        else:
            self.value = int(number)

class Deck:
    def __init__(self):
        self.cards = [Card(a, b) for a in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for b in ['Hearts', 'Spades', 'Clubs', 'Diamonds']]
        
    def shuffle(self):
        random.shuffle(self.cards)

    def hit(self):
        return self.cards.pop()

class Player:
    def __init__(self, deck):
        self.hand = [deck.hit()]

    def show_hand(self, n):
        """ 
        Displays hand if n is 0. If n is 1, displays only 1 card (used for dealer's first show)
        """
        aux_dic = {'Spades': chr(9824), 'Hearts': chr(9829), 'Clubs': chr(9827), 'Diamonds': chr(9830)}
        
        for i in range(len(self.hand) - n):
            print('+----+', end = ' ')
        print('')
        for i in range(len(self.hand) - n):
            print(f'|{self.hand[i].number}', end = '')
            print(' '*(3 - len(self.hand[i].number)), end = '')
            print(f'{aux_dic[self.hand[i].suit]}|', end = ' ')
        print('')
        for i in range(2):
            for i in range(len(self.hand) - n):
                print('|    |', end = ' ')
            print('')
        for i in range(len(self.hand) - n):
            print('+----+', end = ' ')
        print('\n')
        return 0

    def player_hit(self, deck):
        self.hand.append(deck.hit())

    def score(self, n = 0):
        hand = [self.hand[i].value for i in range(len(self.hand))]

        if n:
            return self.hand[0].value

        score = functools.reduce(lambda a, b: a + b, hand)
        ace = len(list(filter(lambda x: x == 11, hand)))

        while score > 21 and ace:
            score -= 10
            ace -= 1

        return score

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(self.deck)
        self.dealer = Player(self.deck)
        self.player.player_hit(self.deck)
        self.dealer.player_hit(self.deck)

    def display(self, n = 0):
        print(f'Dealer: {self.dealer.score(n)}')
        self.dealer.show_hand(n)
        print(f'Player: {self.player.score(0)}')
        self.player.show_hand(0)

    def end(self):
        if self.player.score() > 21 or self.dealer.score() > 21:
            return True
        
        return False

def run():
    while(True):
        print("   ___ _         _    _         _\n  | _ ) |__ _ __| |__(_)__ _ __| |__\n  | _ \ / _` / _| / /| / _` / _| / /\n  |___/_\__,_\__|_\_\/ \__,_\__|_\_\ \n                 !__|__/            \n                  ___\n                / __|__ _ _ __  ___\n               | (_ / _` | '  \/ -_) \n                \___\__,_|_|_|_\___| \n")
        blackjack()
        print("\n" + separator)
        x = input('Play again? [y/N]\n')
        if(x.lower() == 'n'):
            break

if __name__ == '__main__':
    exit(run())
