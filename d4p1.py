def get_sections(assignment):
    start, end = [int(x) for x in assignment.split('-')]
    section_range = range(start, end + 1)
    if len(section_range) > 0:
        sections = set(section_range)
    else:
        sections = set([start])

    return sections

count = 0

with open('d4-input.txt') as f:
    for line in f:
        assignment_pair = line.strip().split(',')
        #print(assignment_pair)
        assignment_1 = get_sections(assignment_pair[0])
        #print(assignment_1)
        assignment_2 = get_sections(assignment_pair[1])
        #print(assignment_2)
        if assignment_1.issubset(assignment_2) or assignment_2.issubset(assignment_1):
            count += 1

print(count)