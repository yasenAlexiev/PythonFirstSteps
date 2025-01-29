from GameObjects.GameObjects import *
from colorama import Fore


class BlackjackPlayer(Player):
    def __init__(self, name, amount):
        Player.__init__(self, name)
        self.aces = None
        self.hand_value = None
        self.account = Account(name, amount)
        self.clear_hand()

    def print_hand(self):
        for card in self.player_cards:
            print(card)

    def add_cards(self, new_cards):
        self.player_cards.append(new_cards)
        self.hand_value += new_cards.value

        if new_cards.rank == "Ace":
            self.aces += 1

        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.hand_value > 21 and self.aces > 0:
            self.hand_value -= 10
            self.aces -= 1

    def point_in_hand(self):
        return self.hand_value

    def clear_hand(self):
        self.player_cards = []
        self.hand_value = 0
        self.aces = 0


def setup_game():
    deck = Deck(Game.BLACKJACK)
    deck.shuffle_cards()

    player = BlackjackPlayer("Yasen", 500)
    dealer = BlackjackPlayer("Dealer", 500)

    return player, dealer, deck


def game_play():
    player, dealer, deck = setup_game()

    play_again = 'Y'
    while play_again == 'Y':

        print(Fore.BLUE + f"Your balance: {player.account.balance}")
        if player.account.balance == 0:
            print(Fore.RED + "You are bankrupt. Go home!!!")
            break
        while True:
            try:
                bet_amount = int(input(Fore.BLUE + "What is your bet?"))
            except ValueError:
                print(Fore.RED + "That is not a number")
            else:
                if bet_amount > player.account.balance:
                    print(Fore.RED + "You do not have enough tokens for the bet")
                else:
                    print(Fore.GREEN + "Good choice!")
                    player.account.withdraw(bet_amount)
                    dealer.account.withdraw(bet_amount)
                    break
        player.clear_hand()
        dealer.clear_hand()

        try:
            player.add_cards(deck.deal_one())
            player.add_cards(deck.deal_one())
            dealer.add_cards(deck.deal_one())
            dealer.add_cards(deck.deal_one())
        except IndexError:
            # return the bet amount in the player and dealer account, because the deck is empty
            player.account.deposit(bet_amount)
            dealer.account.deposit(bet_amount)
            print(Fore.RED + "No more cards in the deck. Good game")
            print(Fore.BLUE + f"Your balance: {player.account.balance}")
            break

        print(Fore.YELLOW + "Dealer card:")
        print(dealer.player_cards[0])
        print(Fore.YELLOW + f"Total of: {dealer.player_cards[0].value}")
        player_keep_playing = True
        while player_keep_playing:
            print(Fore.BLUE + "Player cards:")
            player.print_hand()
            print(Fore.BLUE + f"Total of: {player.point_in_hand()}")

            choice = input(Fore.BLUE + "Do you want to Hit(H) or Stand(S)?")
            if choice == 'H':
                try:
                    player.add_cards(deck.deal_one())
                except IndexError:
                    # return the bet amount in the player and dealer account, because the deck is empty
                    player.account.deposit(bet_amount)
                    dealer.account.deposit(bet_amount)
                    print(Fore.RED + "No more cards in the deck. Good game")
                    play_again = 'N'
                    break

                if player.point_in_hand() > 21:
                    print(Fore.BLUE + "Player cards:")
                    player.print_hand()
                    print(Fore.BLUE + f"Total of: {player.point_in_hand()}")

                    print(Fore.RED + "Player lose. Dealer Win")
                    dealer.account.deposit(2 * bet_amount)
                    player_keep_playing = False
                    break
            elif choice == 'S':
                break

        if player_keep_playing:
            print(Fore.YELLOW + "Dealer cards:")
            dealer.print_hand()
            print(Fore.YELLOW + f"Total of: {dealer.point_in_hand()}")
            while dealer.point_in_hand() <= player.point_in_hand() and dealer.point_in_hand() <= 21:
                try:
                    dealer.add_cards(deck.deal_one())
                    print(Fore.YELLOW + "=======================")
                    print(Fore.YELLOW + "Dealer cards:")
                    dealer.print_hand()
                    print(Fore.YELLOW + f"Total of: {dealer.point_in_hand()}")
                except IndexError:
                    # return the bet amount in the player and dealer account, because the deck is empty
                    player.account.deposit(bet_amount)
                    dealer.account.deposit(bet_amount)
                    print(Fore.RED + "No more cards in the deck. Good game")
                    play_again = 'N'
                    break

            if dealer.point_in_hand() > 21:
                print(Fore.GREEN + "Dealer lose. Player Win")
                player.account.deposit(2 * bet_amount)
            elif dealer.point_in_hand() > player.point_in_hand():
                print(Fore.RED + "Player lose. Dealer Win")
                dealer.account.deposit(2 * bet_amount)

        play_again = input(Fore.CYAN + "Do you want to play again? (Y/N)")


game_play()
