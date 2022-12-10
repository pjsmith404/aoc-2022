tallied_calories = []
with open('day1-input.txt') as f:
    calorie_count = 0
    for line in f:
        if line != '\n':
            snack_calorie = int(line.strip())
            #print(f'{calorie_count} += {snack_calorie}')
            calorie_count += snack_calorie
        else:
            tallied_calories.append(calorie_count)
            calorie_count = 0
            #print(tallied_calories)

tallied_calories.sort(reverse=True)
print(tallied_calories[0])
print(tallied_calories[0] + tallied_calories[1] + tallied_calories[2])