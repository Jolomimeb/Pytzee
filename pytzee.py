"""
File:     pytzee.py
Author:   Oritsejolomisan Mebaghanje
Date:     4/7/2022
section:  11
E-mail:   xz94254@umbc.edu
Description: 
      This program develops a pytzee game. It allows the user to enter various inputs and it acts based on the users choice. It makes use of lists, functions,booleans and several order things to ensure it works properly. 

"""

import random
TOTAL_DICE = 5
DICE_FACES = 6


# rolls the dice
def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    print('\t', "\t".join(map(str, roll_list)))
    return roll_list


# function to count rounds
def count_round(round_num):
    """
    :param round_num: counts the number of rounds
    :return: round_counter
    """
    round_counter = 0
    while round_counter != round_num:
        round_counter += 1
    return round_counter


# function to keep the score in the game and print it out
def score_card(card_1, card_2, card_1_number, card_2_number):
    print('\t''Scorecard: ')
    print('  '.join(card_1))
    print(card_1_number[0], '  ', card_1_number[1], '  ', card_1_number[2], '  ', card_1_number[3],'  ', card_1_number[4],'  ', card_1_number[5])
    print('  '.join(card_2))
    print(card_2_number[0], '\t', card_2_number[1], '\t', card_2_number[2], '\t', card_2_number[3], '\t', card_2_number[4], '\t', card_2_number[5], '\t', card_2_number[6])
    return


def play_game(num_rounds):
    # variables and lists used in this function
    card_1 = ["1's", "2's", "3's", "4's", "5's", "6's"]
    card_2 = ['Three of a kind', 'Four of a kind', 'Full house', 'Small straight', 'Large straight', 'pytzee',
              'Chance']
    card_1_number = [0, 0, 0, 0, 0, 0]
    card_2_number = [0, 0, 0, 0, 0, 0, 0]
    check = True
    check_1 = True
    check_2 = True
    check_3 = True
    check_4 = True
    check_5 = True
    check_6 = True
    three_checker = True
    four_checker = True
    small_checker = True
    large_checker = True
    full_checker = True
    chance_checker = True

    # while loop to start the rounds
    round_counter = 0
    while round_counter != num_rounds:
        round_counter += 1
        print(f'***** Beginning Round {round_counter} *****')
        print(f'      your score is: {sum(score_list)}')

        dice = roll_dice()
        scored = 0
        ans = 0
        counter = input('How would you like to count this dice roll? ')
        counter = counter.strip()
        if counter.lower() != 'skip':

            # different count statements the user can use.
            # These checks the user input and outputs based on what the user enters
            if counter.lower() == 'count 1' and check_1 == True:
                check_1 = False
                print('Accepted the 1! ')
                for numb in dice:
                    if numb == 1:
                        scored += 1
                    ans = scored * 1
                    card_1_number[0] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 1' and check_1 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            if counter.lower() == 'count 2' and check_2 == True:
                check_2 = False
                print('Accepted the 2! ')
                for numb in dice:
                    if numb == 2:
                        scored += 1
                    ans = scored * 2
                    card_1_number[1] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 2' and check_2 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            if counter.lower() == 'count 3' and check_3 == True:
                check_3 = False
                print('Accepted the 3! ')
                for numb in dice:
                    if numb == 3:
                        scored += 1
                    ans = scored * 3
                    card_1_number[2] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 3' and check_3 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            if counter.lower() == 'count 4' and check_4 == True:
                check_4 = False
                print('Accepted the 4! ')
                for numb in dice:
                    if numb == 4:
                        scored += 1
                    ans = scored * 4
                    card_1_number[3] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 4' and check_4 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            if counter.lower() == 'count 5' and check_5 == True:
                check_5 = False
                print('Accepted the 5! ')
                for numb in dice:
                    if numb == 5:
                        scored += 1
                    ans = scored * 5
                    card_1_number[4] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 5' and check_5 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            if counter.lower() == 'count 6' and check_6 == True:
                check_6 = False
                print('Accepted the 6! ')
                for numb in dice:
                    if numb == 6:
                        scored += 1
                    ans = scored * 6
                    card_1_number[5] = ans
                score_list.append(ans)
            elif counter.lower() == 'count 6' and check_6 == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for three of a kind
            if (counter.lower() == 'three of a kind' or counter.lower() == '3 of a kind') and three_checker == True:
                three_checker = False
                if dice[0] == dice[1] == dice[2] or dice[1] == dice[2] == dice[3] or dice[2] == dice[3] == dice[4]:
                    print('Three of a kind! ')
                    score_list.append(sum(dice))
                    card_2_number[0] = sum(dice)
            elif (counter.lower() == 'three of a kind' or counter.lower() == '3 of a kind') and three_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for four of a kind
            if (counter.lower() == 'four of a kind' or counter.lower() == '4 of a kind') and four_checker == True:
                four_checker = False
                if dice[0] == dice[1] == dice[2] == dice[3] or dice[1] == dice[2] == dice[3] == dice[4]:
                    print('four of a kind! ')
                    score_list.append(sum(dice))
                    card_2_number[1] = sum(dice)
            elif (counter.lower() == 'four of a kind' or counter.lower() == '4 of a kind') and four_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for full house
            if counter.lower() == 'full house' and full_checker == True:
                full_checker = False
                if dice[0] == dice[1] == dice[2] and dice[3] == dice[4]:
                    score_list.append(25)
                    card_2_number[2] = 25
                elif dice[1] == dice[2] == dice[3] and dice[0] == dice[4]:
                    score_list.append(25)
                    card_2_number[2] = 25
                elif dice[2] == dice[3] == dice[4] and dice[0] == dice[1]:
                    score_list.append(25)
                    card_2_number[2] = 25
            elif counter.lower() == 'full house' and full_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for small straight
            if counter.lower() == 'small straight' and small_checker == True:
                small_checker = False
                if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
                    score_list.append(30)
                    card_2_number[3] = 30
                    print('You have a small straight and get 30 points.')
                elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                    score_list.append(30)
                    card_2_number[3] = 30
                    print('You have a small straight and get 30 points.')
                elif 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                    score_list.append(30)
                    card_2_number[3] = 30
                    print('You have a small straight and get 30 points.')
            elif counter.lower() == 'small straight' and small_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for large straight
            if counter.lower() == 'large straight' and large_checker == True:
                large_checker = False
                if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                    score_list.append(40)
                    card_2_number[4] = 40
                    print('You have a large straight and get 40 points.')
                elif 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                    score_list.append(40)
                    card_2_number[4] = 40
                    print('You have a large straight and get 40 points.')
            elif counter.lower() == 'large straight' and large_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for chance
            if counter.lower() == 'chance' and chance_checker == True:
                chance_checker = False
                score_list.append(sum(dice))
                card_2_number[6] = sum(dice)
            elif counter.lower() == 'chance' and chance_checker == False:
                print('There was already a score in that slot.')
                counter = input('How would you like to count this dice roll? ')

            # checks for pytzee
            if counter.lower() == 'pytzee':
                if dice[0] == dice[1] == dice[2] == dice[3] == dice[4] and check == True:
                    score_list.append(50)
                    check = False
                    card_2_number[5] = 50
                else:
                    score_list.append(100)
                    card_2_number[5] += 100

        # calls the scorecard function
        score_card(card_1, card_2, card_1_number, card_2_number)

    # gives the bonus point for at least 63
    if sum(card_1_number) >= 63:
        score_list.append(35)

    # prints the final score
    print(f'your final score was {sum(score_list)}')
    return sum(score_list)


if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to skip: '))
    score_list = []
    if seed:
        random.seed(seed)
    play_game(num_rounds)
