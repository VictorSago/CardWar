from warlib import Deck, Player

# Game setup
ADDITIONAL_CARDS = 5

player_one = Player("One")
player_two = Player("Two")

game_deck = Deck()
game_deck.shuffle()

for card in range(int(len(game_deck)/2)):
    player_one.add_cards(game_deck.deal_one())
    player_two.add_cards(game_deck.deal_one())

print(f"Player {player_one.name}: {len(player_one.card_hand)}")
print(f"Player {player_two.name}: {len(player_two.card_hand)}")

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round: {round_num}")

    if player_one.cards_left() == 0:
        print(f"Player {player_one.name} is out of cards. Player {player_two.name} wins")
        game_on = False
        break
    if player_two.cards_left() == 0:
        print(f"Player {player_two.name} is out of cards. Player {player_one.name} wins")
        game_on = False
        break

    # Start new round
    player_one_cards = [player_one.play_card()]
    player_two_cards = [player_two.play_card()]

    at_war = True
    while at_war:
        print(f"Player {player_one.name}: ", player_one_cards)
        print(f"Player {player_two.name}: ", player_two_cards)
        if player_one_cards[-1] > player_two_cards[-1]:
            player_one.add_cards(player_one_cards, player_two_cards)
            at_war = False
        elif player_one_cards[-1] < player_two_cards[-1]:
            player_two.add_cards(player_two_cards, player_one_cards)
            at_war = False
        else:
            print("WAR!")
            if player_one.cards_left() < ADDITIONAL_CARDS:
                print(f"Player {player_one.name} unable to play. Player {player_two.name} wins!")
                game_on = False
                break
            elif player_two.cards_left() < ADDITIONAL_CARDS:
                print(f"Player {player_two.name} unable to play. Player {player_one.name} wins!")
                game_on = False
                break
            else:
                for num in range(ADDITIONAL_CARDS):
                    player_one_cards.append(player_one.play_card())
                    player_two_cards.append(player_two.play_card())

    print("Goodbye!")
