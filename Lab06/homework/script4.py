def print_numbers_divisible_by_2_not_by_3(n, sort_order='ascending'):
    numbers = []
    i = 0
    while len(numbers) < n:
        if i % 2 == 0 and i % 3 != 0:
            numbers.append(i)
        i += 1
    if sort_order == 'ascending':
        numbers.sort(key=lambda x: x)
    elif sort_order == 'descending':
        numbers.sort(key=lambda x: x, reverse=True)
    for number in numbers:
        print(number)


print_numbers_divisible_by_2_not_by_3(10, 'ascending')
