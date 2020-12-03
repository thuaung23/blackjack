# This is a game of BlackJack played between a user and house.
# Written by: Thu Aung
# Written on: Sept 10, 2020

print('Welcome to the BlackJack.')
print(' ')

import random

# Assign sum of two random int to dealer/computer.
def house_total():
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    return num1 + num2

# Assign sum of two random int to player/user.
def player_total():
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    return num1 + num2

# Compare house_cards and player_cards.
def compare_total(total1, total2):
    if total1 > total2 and total1 <= 21:
        print('Sorry, you lose.')
    elif total2 > total1 and total2 <= 21:
        print('Congratulations!! You won.')
    elif total1==total2:
        print('It is a draw.')


def draw_another_card():
    new_number = random.randint(1, 11)
    return int(new_number)

# Check if the player wants to play again.
def play_again():
    return input('Do you want to play again? Y or N: ').lower().startswith('y')

game_on = True

while game_on:
    total_p = player_total()
    total_h = house_total()
    new_card = draw_another_card()
    print('Your total is: ', total_p)
    # Check for instant lose (player).
    if total_p > 21:
        print('Bust!!! You lose.')
        break
    # Check for instant win (player).
    elif total_p == 21:
        print('BlackJack! You\'ve won.')
        break

    choice = input('Do you want to draw another card? Y or N: ').upper()
    if choice == 'Y':
        new_total = new_card + total_p
        # Let the player know what the new total is.
        print('Your new total is: ', new_total)
        if new_total > 21:
            print('Bust!!! You lose.')
            break

        elif new_total == 21:
            print('BlackJack! You\'ve won.')
            break
        else:
            print('The house total is : ', total_h)
            if total_h < 14:
                # If sum of house cards is less than 14, automatic draw another card.
                print('The house will be drawing another card.')
                house_new_total = total_h + new_card
                # Let the player know what the total of house cards is.
                print('The new house total is : ', house_new_total)
                # Check for instant lose (house).
                if house_new_total > 21:
                    print('House is busted!!! You won.')
                    break
                # Check for instant win (house)
                elif house_new_total == 21:
                    print("Sorry, House wins.")
                    break
                # Check to see who win.
                elif house_new_total < 21:
                    result = compare_total(house_new_total, new_total)
                    print(result)
            # If sum of house cards is equal or over 14, directly compare without drawing new card.
            elif total_h >= 14:
                result = compare_total(total_h, new_total)
                print(result)

    elif choice == 'N':
        print('The house total is : ', total_h)
        if total_h < 14:
            print('The house will be drawing another card.')
            house_new_total = total_h + new_card
            print('The new house total is : ', house_new_total)
            if house_new_total > 21:
                print('House is busted!!! You won.')
                break

            elif house_new_total == 21:
                print("Sorry, House wins.")
                break

            elif house_new_total < 21:
                result = compare_total(house_new_total, total_p)
                print(result)

        elif total_h >= 14:
            result = compare_total(total_h, total_p)
            print(result)
    # Check if the player wants to play again. If not, break out of the while loop. 
    if not play_again():
        break