def get_item_score(item):
    item_score = list(map(chr, range(97,123))) + list(map(chr, range(65,91)))
    return item_score.index(item) + 1

item_list = []

with open('d3-input.txt') as f:
    for line in f:
        stripped_line = line.strip()
        first_compartment = stripped_line[:len(line)//2]
        second_compartment = stripped_line[len(line)//2:]
        #print(first_compartment)
        #print(second_compartment)
        set_intersection = set(first_compartment).intersection(set(second_compartment)).pop()
        #print(set_intersection)
        item_list.append(set_intersection)

print(list(map(get_item_score, item_list)))
print(sum(map(get_item_score, item_list)))