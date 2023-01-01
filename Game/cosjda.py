import random

# MIN_PRICE = 20
# MAX_PRICE = 100
# BONUS = 10
# ROUNDS = 100
# current_round, your_score, enemy_score - integers
# your-choices, enemy_choices - arrays of 100 integers


def get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
    if enemy_choices[0] and enemy_choices[1] == 20:
        return 20
    if enemy_choices[current_round] == enemy_choices[current_round - 1] - 1:
        your_choices[current_round] == enemy_choices[current_round - 1] - 2
        if enemy_choices[current_round] == 20:
            your_choices == 20
    if enemy_choices[current_round] == enemy_choices[current_round - 1] - 2:
        your_choices[current_round] == enemy_choices[current_round - 1] - 3
        if enemy_choices[current_round] == 20:
            your_choices == 20
    if enemy_choices[0] and enemy_choices[1] == 100:
        return 99
    if enemy_choices[0] and enemy_choices[1] == 99:
        return 98
    if enemy_choices[current_round - 1] == your_choices[current_round - 2]:
        your_choices[current_round] == 100
    if enemy_choices[0] == 20 and enemy_choices[1] == 21:
        your_choices == 20
    if enemy_choices[current_round-1] == enemy_choices[current_round-1] - 1:
        your_choices[current_round] == enemy_choices[current_round-1] -1
    return random.randint(20,100)



def get_second_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):

    return random.randint(20,100)


# Ctrl + / to remove comments
# 1. random bot
# def get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
#     return random.randint(0, 120)


# 2. constant bot
# def get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
#     return 60


# 3. very nice bot
# def get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
#     if current_round == 0:
#         return 100
#     else:
#         return enemy_choices[current_round - 1]


def game():
    min_price = 20
    max_price = 100
    bonus = 10
    rounds = 100

    first_player_choices = [0 for i in range(0, rounds)]
    second_player_choices = [0 for i in range(0, rounds)]
    first_player_total_score = 0
    second_player_total_score = 0

    for currentRound in range(0, rounds):
        first_player_choices_temp = []
        second_player_choices_temp = []
        for i in range(0, rounds):
            first_player_choices_temp.append(first_player_choices[i])
            second_player_choices_temp.append(second_player_choices[i])
        first_player_choice = get_first_player_choice(currentRound, first_player_total_score, second_player_total_score, first_player_choices_temp, second_player_choices_temp)

        first_player_choices_temp = []
        second_player_choices_temp = []
        for i in range(0, rounds):
            first_player_choices_temp.append(first_player_choices[i])
            second_player_choices_temp.append(second_player_choices[i])
        second_player_choice = get_second_player_choice(currentRound, second_player_total_score, first_player_total_score, second_player_choices_temp, first_player_choices_temp)

        first_player_choices[currentRound] = first_player_choice
        second_player_choices[currentRound] = second_player_choice

        first_player_score = -1
        second_player_score = -1

        if first_player_choice < min_price or first_player_choice > max_price:
            first_player_score = 0
            if min_price <= second_player_choice <= max_price:
                second_player_score = second_player_choice + bonus

        if second_player_choice < min_price or second_player_choice > max_price:
            second_player_choice = 0
            if min_price <= first_player_choice <= max_price:
                first_player_score = first_player_choice + bonus

        if first_player_score == -1 and second_player_score == -1:
            if first_player_choice == second_player_choice:
                first_player_score = second_player_score = first_player_choice
            elif first_player_choice < second_player_choice:
                first_player_score = first_player_choice + bonus
                second_player_score = first_player_choice - bonus
            else:
                first_player_score = second_player_choice - bonus
                second_player_score = second_player_choice + bonus

        first_player_total_score += first_player_score
        second_player_total_score += second_player_score

        print("First player choice: {0} and score: + {1} (= {2}), second player choice {3} and score: + {4} (= {5}).\n"
              .format(first_player_choice, first_player_score, first_player_total_score, second_player_choice, second_player_score, second_player_total_score))

    print("First player score: {0}, second player score: {1}.".format(first_player_total_score, second_player_total_score))
    print("First player choices: ", first_player_choices)
    print("Second player choices: ", second_player_choices)


if __name__ == '__main__':
    game()