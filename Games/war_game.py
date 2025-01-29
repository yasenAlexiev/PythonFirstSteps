from GameObjects.GameObjects import *


def setup_game():
    player_one = Player("Yasen")
    player_two = Player("Stefy")
    deck = Deck(Game.WAR)
    deck.shuffle_cards()

    half_of_cards = int(len(deck.all_cards)/2)
    for _ in range(half_of_cards):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    return player_one, player_two


def game_play():
    player_one, player_two = setup_game()
    round_count = 1
    game_on = True
    while game_on:
        print(f"Round {round_count}")
        round_count += 1

        if len(player_one.player_cards) == 0:
            print(f"Player {player_one.name}  out of cards")
            print(f"Player {player_one.name}  Lose. Player {player_two.name} Win. Game over")
            game_on = False
            break
        if len(player_two.player_cards) == 0:
            print(f"Player {player_two.name} out of cards")
            print(f"Player {player_two.name} Lose. Player {player_one.name} Win. Game over")
            game_on = False
            break

        player_one_played_cards = []
        player_two_played_cards = []

        player_one_played_cards.append(player_one.remove_one())
        player_two_played_cards.append(player_two.remove_one())
        at_war = True
        while at_war:

            player_one_last_added_card = player_one_played_cards[-1]
            player_two_last_added_card = player_two_played_cards[-1]

            if player_one_last_added_card.value < player_two_last_added_card.value:
                player_two.add_cards(player_one_played_cards)
                player_two.add_cards(player_two_played_cards)
                at_war = False
            elif player_one_last_added_card.value > player_two_last_added_card.value:
                player_one.add_cards(player_one_played_cards)
                player_one.add_cards(player_two_played_cards)
                at_war = False
            else:
                print("WAR")
                if len(player_one.player_cards) < 5:
                    print(f"Player {player_one.name} do not have enough cards for the war.")
                    print(f"Player {player_one.name} Lose. Player {player_two.name} Win. Game over")
                    game_on = False
                    break
                elif len(player_two.player_cards) < 5:
                    print(f"Player {player_two.name} do not have enough cards for the war.")
                    print(f"Player {player_two.name} Lose. Player {player_one.name}  Win. Game over")
                    game_on = False
                    break
                else:
                    for _ in range(5):
                        player_one_played_cards.append(player_one.remove_one())
                        player_two_played_cards.append(player_two.remove_one())


game_play()