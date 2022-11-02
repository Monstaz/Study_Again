import random
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    choice = input("Menu:\n1 - Start Game\n2 - Exit\n")
    if choice == '1':
        deck()
    elif choice == '2':
        input("Good bye!\nPress any button")
        sys.exit()
    else:
        cls()
        menu()


def deck():
    player_cash = 100
    num_decks = ''

    while num_decks <= '0' or num_decks >= '5':
        num_decks = input("How many decks will be shuffled?\nChoose from 1 to 4\n")

    start_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    game_deck = start_deck * int(num_decks)
    random.shuffle(game_deck)
    random.shuffle(game_deck)
    cls()
    game(game_deck, player_cash)


def game(game_deck, player_cash):
    lose = 0
    bet = 0

    while True:
        try:
            bet = int(input("Choose the bet(From 5 to 20): "))
            if 5 <= bet <= 20:
                break
            else:
                cls()
        except (TypeError, ValueError):
            print("Enter valid bet!")
            continue

    dealer_hand = game_deck.pop(0)
    print(f"Dealer's open hand:{dealer_hand}")
    hand = game_deck[0] + game_deck[1]
    print(f"Your cards: {game_deck[0]} and {game_deck[1]}")
    del game_deck[0:2]

    if hand == 21:
        print("BlackJack! Now wait dealer.")

    elif hand == 22:
        hand = 12
        print(f"Your points:{hand}")

    while True:
        action = input("1 - Hit\n2 - Stop\n")
        if action == '1':
            hand += game_deck[0]
            if game_deck[0] == 11 and hand > 21:
                hand -= 10
            if hand == 21:
                print("Congrats! 21 points!\nWait dealer...")
                break
            player_info = f"Your card:{game_deck[0]}\nYour points:{hand}"
            if hand > 21:
                player_cash -= bet
                print(f"{player_info}You bust!\nYour cash is:{player_cas}")
                lose = 1
                break
            print(player_info)
            del game_deck[0]
        elif action == '2':
            break

    if lose != 1:
        while dealer_hand <= 16:
            dealer_hand += game_deck[0]
            if game_deck[0] == 11 and dealer_hand >= 21:
                dealer_hand -= 10
            print(f"Dealer's card:{game_deck[0]}\nDealer's player_cash:{dealer_hand}")
            del game_deck[0]
        result_info = f"Your player_cash:{hand}\nDealer's player_cash:{dealer_hand}"
        if hand < dealer_hand <= 21:
            player_cash -= bet
            print(result_info + f"\nYou Lose!\nNow your cash:{player_cash}")
        elif dealer_hand == hand:
            player_cash += bet
            print(result_info + f"\nDraw!\nNow your cash:{player_cash}")
        elif dealer_hand < hand or dealer_hand > 21:
            player_cash += bet * 2
            print(result_info + f"\nYou Win!\n Now your cash:{player_cash}")

    if player_cash <= 0:
        input("You lose all of your cash!\n Type any button to continue")
        menu()
    while True:
        retry = input("Want to play again?\n1 - Yes\n2 - Back to menu\n")
        if retry == '1':
            cls()
            game(game_deck, player_cash)
        elif retry == '2':
            input(f"Thanks for playing!\nYour cash is {player_cash}\nGood luck!\nPress any button to continue")
            menu()


menu()
