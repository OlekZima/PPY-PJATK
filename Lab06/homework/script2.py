def catalan_numbers(n, option='all'):
    if option == 'even':
        start = 2
        step = 2
    elif option == 'odd':
        start = 1
        step = 2
    else:
        start = 1
        step = 1
    c = 1
    for i in range(start, n, step):
        yield c
        c = c * 2 * (2 * i + 1) // (i + 2)
    yield c


print(list(catalan_numbers(10)))
