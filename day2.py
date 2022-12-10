choice_keys = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

result_keys = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

choice_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

result_points = {
    'lose': 0,
    'draw': 3,
    'win': 6
}

def calculate_points(choice, result):
    score = choice_points[choice] + result_points[result]
    return score

def play_game(their_choice, your_choice):
    #print(f'Playing Game')
    #print(f'Your Choice: {your_choice}')
    #print(f'Their Choice: {their_choice}')
    if your_choice == their_choice:
        result = 'draw'
    elif your_choice == 'rock' and their_choice == 'scissors':
        result = 'win'
    elif your_choice == 'paper' and their_choice == 'rock':
        result = 'win'
    elif your_choice == 'scissors' and their_choice == 'paper':
        result = 'win'
    else:
        result = 'lose'

    score = calculate_points(your_choice, result)
    #print(f'Result: {result}, Score: {score}\n')
    return score

def calculate_choice(their_choice, expected_result):
    if expected_result == 'lose' and their_choice == 'rock':
        your_choice = 'scissors'
    elif expected_result == 'lose' and their_choice == 'paper':
        your_choice = 'rock'
    elif expected_result == 'lose' and their_choice == 'scissors':
        your_choice = 'paper'
    elif expected_result == 'win' and their_choice == 'rock':
        your_choice = 'paper'
    elif expected_result == 'win' and their_choice == 'paper':
        your_choice = 'scissors'
    elif expected_result == 'win' and their_choice == 'scissors':
        your_choice = 'rock'
    elif expected_result == 'draw':
        your_choice = their_choice

    return your_choice

with open('day2-input.txt') as f:
    total_score = 0
    for line in f:
        their_choice, expected_result = line.strip().split(' ')
        their_choice = choice_keys[their_choice]
        expected_result = result_keys[expected_result]
        your_choice = calculate_choice(their_choice, expected_result)
        total_score += play_game(their_choice, your_choice)

print(f'Total Score: {total_score}')