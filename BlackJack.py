import json
import random
import os
import sys
import pathlib


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_to_file(name, score):
    with open('Scoreboard.json', 'r') as file_read:
        lis = json.load(file_read)
    lis.append(name)
    lis.append(score)
    with open('Scoreboard.json', 'w') as file_write:
        json.dump(lis, file_write)


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
        deck()
    elif choice == '2':
        input("Good bye!\nPress any button")
        sys.exit()
    elif choice == '3':
        show_scoreboard()
        input("Press any button to continue... ")
        menu()
    else:
        cls()
        menu()


def deck():
    num_decks = ''

    while num_decks <= '0' or num_decks >= '5':
        num_decks = input("How many decks will be shuffled?\nChoose from 1 to 4\n")

    start_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    game_deck = start_deck * int(num_decks)
    random.shuffle(game_deck)
    random.shuffle(game_deck)
    cls()
    game(game_deck, 100)


def game(game_deck, player_cash):
    lose = 0
    bet = 0
    player_name = input("Enter your name: ")

    while True:
        try:
            bet = int(input("Choose the bet(From 5 to 20): "))
            if 5 <= bet <= 20:
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
    print(f"Your cards: {game_deck[0]} and {game_deck[1]}\nTotal:{hand}")
    del game_deck[0:2]

    if hand == 21:
        print("BlackJack! Now wait dealer.\n")

    elif hand == 22:
        hand = 12
        print(f"Your points:{hand}")

    while hand != 21:
        action = input("\n1 - Hit\n2 - Stop\n")
        cls()
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
                print(f"\n{player_info}You bust!\nYour cash is:{player_cash}")
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
            print(f"Dealer's card:{game_deck[0]}\nDealer's score:{dealer_hand}\n")
            del game_deck[0]
        result_info = f"Your score:{hand}\nDealer's score:{dealer_hand}\n"
        if hand < dealer_hand <= 21:
            player_cash -= bet
            print(result_info + f"\nYou Lose!\nNow your cash:{player_cash}")
        elif dealer_hand == hand:
            player_cash += bet
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
            game(game_deck, player_cash)
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
