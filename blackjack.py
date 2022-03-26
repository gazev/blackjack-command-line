import classes
import time

def blackjack():
    game = classes.Game()

    game.display(1)
    while not game.end():
        x = input('Hit? [y/N]\n')
        if x.lower() == 'y' or x == '':
            print('...................................................')
            print('Player Hit')
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

    print('....................................................')
    print('Dealer reveals card')
    game.display(0)
    while not game.end():
        if game.dealer.score() < 17:
            time.sleep(2.5)
            print('....................................................')
            print('Dealer Hit')
            game.dealer.player_hit(game.deck)
            game.display(0)
        else:
            break

    if game.end():
        print('Dealer Busted!')
        return 0

    if game.dealer.score() > game.player.score():
        print('You Lost!')
    elif game.dealer.score() < game.player.score():
        print('You won!')
    else:
        print('Draw!')

    return 0

if __name__ == '__main__':
    blackjack()
