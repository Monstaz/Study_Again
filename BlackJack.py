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
    num_decks = ''

    while num_decks <= '0' or num_decks >= '5':
        num_decks = input("How many decks will be shuffled?\nChoose from 1 to 4\n")

    start_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    game_deck = start_deck * int(num_decks)
    random.shuffle(game_deck)
    random.shuffle(game_deck)
    cls()
    game(game_deck)


def game(game_deck):
    lose = 0

    dealer_hand = game_deck.pop(0)
    print("Dealer's open hand: ", dealer_hand)
    hand = game_deck[0] + game_deck[1]
    print("Your cards:\n", game_deck[0], 'and', game_deck[1])
    del game_deck[0:2]

    if hand == 21:
        print("BlackJack! Now wait dealer.")

    elif hand == 22:
        hand = 12
        print("Your points: ", hand)

    while True:
        action = input("1 - Hit\n2 - Stop\n")
        if action == '1':
            hand += game_deck[0]
            if game_deck[0] == 11 and hand > 21:
                hand -= 10
            if hand == 21:
                print("Congrats! 21 points!\nWait dealer.")
                break
            if hand > 21:
                print("Your card: ", game_deck[0], "\nYour points: ", hand, "\nYou got bust!")
                lose = 1
                break
            print("Your card: ", game_deck[0], "\nNow your points: ", hand)
            del game_deck[0]
        elif action == '2':
            break

    if lose != 1:
        while dealer_hand <= 16:
            dealer_hand += game_deck[0]
            if game_deck[0] == 11 and dealer_hand >= 21:
                dealer_hand -= 10
            print("Dealer's card:", game_deck[0], "\nDealer's score:", dealer_hand)
            del game_deck[0]
        result = "Your score:" + str(hand) + "\nDealer's score:" + str(dealer_hand)
        if hand < dealer_hand <= 21:
            result += "\nYou lose!"
            print(result)
        elif dealer_hand == hand:
            result += "\nDraw!"
            print(result)
        elif dealer_hand < hand or dealer_hand > 21:
            result += "\nYou win!"
            print(result)
    else:
        print("You lose!")

    retry = ''
    while retry != 1 or retry != 2:
        retry = input("Want to play again?\n1 - Yes\n2 - No(Back to menu)\n")
        if retry == '1':
            cls()
            game(game_deck)
        elif retry == '2':
            menu()
        else:
            continue


menu()
