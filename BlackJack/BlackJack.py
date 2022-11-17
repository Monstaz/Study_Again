import json
import random
import os
import sys
import pathlib


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_to_file(name, score):
    with open('Scoreboard.json', 'r') as file_read:
        score_list = json.load(file_read)
    score_list.append(name)
    score_list.append(score)
    with open('Scoreboard.json', 'w') as file_write:
        json.dump(score_list, file_write)


def show_scoreboard():
    with open('Scoreboard.json', 'r') as file_load:
        file_list = json.load(file_load)
    name_lst = file_list[0::2]
    score_list = file_list[1::2]
    for i in range(len(name_lst)):
        print(f"{name_lst[i]} has {score_list[i]} points")


def menu():
    choice = input("Menu:\n1 - Start Game\n2 - Exit\n3 - Scoreboard\n")
    if choice == '1':
        global player_name
        player_name = input("Enter your name: ")
        deck()
    elif choice == '2':
        input("Good bye!\nPress any button")
        sys.exit()
    elif choice == '3':
        cls()
        show_scoreboard()
        input("Press any button to continue... ")
        menu()
    else:
        cls()
        menu()


def deck():
    decks_in_shuffle = random.randint(2, 8)
    game_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * decks_in_shuffle
    start_game_deck = game_deck.copy()
    for count in range(5):
        random.shuffle(game_deck)
    game(game_deck, 100, start_game_deck)


def game(game_deck, player_cash, start_game_deck):
    lose = 0
    bet = 0
    # Check that current decks is bigger than started deck
    # If so refresh it
    if len(game_deck) < len(start_game_deck) / 2:
        game(start_game_deck, player_cash, start_game_deck)

    while True:
        try:
            bet = int(input("Choose the bet(From 5 to 25): "))
            if 5 <= bet <= 25:
                cls()
                break
            else:
                cls()
        except (TypeError, ValueError):
            print("Enter valid bet!")
            continue

    dealer_hand = game_deck.pop(0)
    print(f"Dealer's open hand:{dealer_hand}\n")
    hand = game_deck[0] + game_deck[1]
    print(f"Your cards: {game_deck.pop(0)} and {game_deck.pop(0)}\nTotal:{hand}")

    if hand == 21:
        print("BlackJack! Now wait dealer.\n")
    elif hand == 22:
        hand = 12
        print(f"Your points:{hand}")

    while hand != 21:
        action = input("\n1 - Hit\n2 - Stop\n")
        cls()
        print(game_deck)
        if action == '1':
            hand += game_deck[0]
            if game_deck[0] == 11 and hand > 21:
                hand -= 10
            if hand == 21:
                print(f"Your card: {game_deck[0]}\nCongrats! 21 points!\nWait dealer...")
                game_deck.pop(0)
                break
            player_info = f"Your card:{game_deck.pop(0)}\nYour points:{hand}"
            if hand > 21:
                player_cash -= bet
                print(f"\n{player_info} you bust!\nYour cash is:{player_cash}")
                lose = 1
                break
            print(player_info)
        elif action == '2':
            break

    if lose != 1:
        while dealer_hand <= 16:
            dealer_hand += game_deck[0]
            if game_deck[0] == 11 and dealer_hand >= 21:
                dealer_hand -= 10
            print(f"Dealer's card:{game_deck.pop(0)}\nDealer's score:{dealer_hand}\n")
        result_info = f"Your score:{hand}\nDealer's score:{dealer_hand}\n"
        if hand < dealer_hand <= 21:
            player_cash -= bet
            print(result_info + f"\nYou Lose!\nNow your cash:{player_cash}")
        elif dealer_hand == hand:
            print(result_info + f"\nDraw!\nNow your cash:{player_cash}")
        elif dealer_hand < hand or dealer_hand > 21:
            player_cash += bet * 2
            print(result_info + f"\nYou Win!\nNow your cash:{player_cash}")

    if player_cash <= 0:
        input("You lost all of your cash!\nType any button to continue")
        menu()

    while True:
        retry = input("\nWant to play again?\n1 - Yes\n2 - Back to menu\n")
        if retry == '1':
            cls()
            game(game_deck, player_cash, start_game_deck)
        elif retry == '2':
            input(f"Thanks for playing!\nYour cash is {player_cash}\nGood luck!\nPress any button to continue")
            save_to_file(player_name, player_cash)
            menu()


file_check = pathlib.Path('Scoreboard.json')
basic_list = ["Dima", "12", "Andrey", "97", "Steve", "150"]
if not file_check.exists():
    with open('Scoreboard.json', 'w') as f:
        json.dump(basic_list, f)

menu()
