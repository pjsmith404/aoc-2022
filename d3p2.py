def get_item_score(item):
    item_score = list(map(chr, range(97,123))) + list(map(chr, range(65,91)))
    return item_score.index(item) + 1

def chunks(iterable, step):
    for i in range(0, len(iterable), step):
        yield iterable[i:i+step]

def get_badge(bags):
    bag_1 = bags[0]
    bag_2 = bags[1]
    bag_3 = bags[2]
    badge = set(bag_1) & set(bag_2) & set(bag_3)
    return badge.pop()

item_list = []

with open('d3-input.txt') as f:
    lines = [line.rstrip() for line in f]
    for group in chunks(lines, 3):
        badge = get_badge(group)
        item_list.append(badge)

print(list(map(get_item_score, item_list)))
print(sum(map(get_item_score, item_list)))