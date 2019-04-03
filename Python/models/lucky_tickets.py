def easy_way_counting(f):
    count_easy_way = 0
    for line in f:
        line = list(line[:6])
        line = [int(i) for i in line]
        first_half = line[:3]
        last_half = line[3:6]
        if sum(first_half) == sum(last_half):
            count_easy_way += 1
    return count_easy_way


def difficult_way_counting(f):
    count_difficult_way = 0
    for line in f:
        line = list(line[:6])
        line = [int(i) for i in line]
        even_line = [i for i in line if i % 2 == 0]
        odd_line = [i for i in line if i % 2 != 0]
        if sum(even_line) == sum(odd_line):
            count_difficult_way += 1
    return count_difficult_way






