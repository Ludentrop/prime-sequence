def is_prime(n: int) -> bool:
    '''
    INPUT: integer
    OUTPUT: bool
    DESCRIPTION: Return True or False depending on is n prime number
    '''

    flag = True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = False
    if flag and n > 1:
        return True
    return False


def prime_seq(n: int) -> list:
    '''
    INPUT: integer
    OUTPUT: generator
    DESCRIPTION: Return a list of prime numbers which size is n
    '''

    primes = []
    x = 2
    while len(primes) != n:
        if is_prime(x):
            primes.append(x)
        x += 1

    return primes


if __name__ == '__main__':
    print(*prime_seq(int(input())))
