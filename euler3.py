import math

def max_prime_fac(n):
    factors = []
    limit = int(math.sqrt(n))
    div = 2
    while n > 1:
        while n % div == 0 and div < limit:
            factors.append(div)
            n /= div
        div = div + 1

    print max(factors)

max_prime_fac(600851475143)
