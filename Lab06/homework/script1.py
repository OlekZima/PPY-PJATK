def is_perfect(*args):
    results = {}
    for num in args:
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            results[num] = True
        else:
            results[num] = False
    return results


print(is_perfect(6, 23))
