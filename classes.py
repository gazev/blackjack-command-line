import random

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
        self.cards = [Card(a, b) for a in ['2', '3', '4', '5','6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for b in ['Hearts', 'Spades', 'Clubs', 'Diamonds']]
        
    def shuffle(self):
        random.shuffle(self.cards)

    def hit(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.hit()]

    def show_hand(self, n):
        """ Displays hand if n is 0. If n is 1, displays only 1 card (used for dealer first show)
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
        print('')
        return 0

    def player_hit(self, deck):
        self.hand.append(deck.hit())

    def score(self, n = 0):
        if n:
            return self.hand[0].value
        score = 0
        ace = 0
        for card in self.hand:
            score += card.value
            if card.value == 11:
                ace += 1
        
        if score > 21 and ace != 0:
            score = score - ace*10

        return score

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('Player', self.deck)
        self.dealer = Player('Dealer', self.deck)
        self.player.player_hit(self.deck)
        self.dealer.player_hit(self.deck)

    def display(self, n = 0):
        print(f'Dealer: {self.dealer.score(n)}')
        self.dealer.show_hand(n)
        print(f'Player: {self.player.score(0)}')
        self.player.show_hand(0)

    def end(self):
        if self.player.score(0) > 21 or self.dealer.score(0) > 21:
            return True
        
        return False