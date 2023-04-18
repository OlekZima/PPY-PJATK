def sieve_of_eratosthenes(n=541):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False
    for i in range(n + 1):
        if primes[i]:
            yield i


for prime in sieve_of_eratosthenes():
    print(prime)
    if prime == 541:
        break
