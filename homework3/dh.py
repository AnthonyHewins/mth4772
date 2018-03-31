from math import gcd

# Using the power of abstract for a little: in a cyclic group the order of any element
# must divide the order of the group it generates. In particular, \mathbb{Z^*}_17 has
# 16 elements, range(1,17). So the order of each element is either 1, 2, 4, 8, or 16. If we find that
# a^1 == 1 or a^2 == 1 or a^4 == 1 or a^8 == 1, that means order(a)!=16 and it can't be a
# generator. Use that logic to test for generators.
def find_generators(n):
    if n <= 1:
        raise ValueError("Positive ints only")

    # I test that it's prime stupidly; this should be assumed to be true.
    # If the number isn't prime then the multiplicative set mod n isn't even
    # a group; e.g. Z/9Z* = range(1,10). But 3 * 3 == 0, not in Z/9Z*.
    for i in range(2, int(n ** 0.5 // 1) + 1):
        if n % i == 0:
            raise ValueError("Primes only. Given %d, %d % %d == 0." % n,n,i)
    
    # First, before trying generators, it's worth finding the factors of our 
    # Since we're excluding zero in our group, our group's order is n - 1.
    # So we need factors of n-1 that aren't 1 or n-1 itself (why? if the elements
    # order is 1 then it's 1, otherwise if it's n-1 it's a generator).
    factors = [i for i in range(2, (n-1)//2 + 1) if (n-1) % i == 0]

    # Now that we have our factors, we can test generators much faster by
    # skipping lots of values. Use the description at the top on how these
    # loops work.
    flag = False
    generators = []
    for i in range(1,n):
        for j in factors:
            if pow(i, j, n) == 1:
                flag = False
                break
            flag = True
        if flag:
            generators += [i]
            flag = False
    return set(generators)

def _test_generators():
    # This just tests that my generator functions worked
    for i in range(2,100):
        if not _is_prime(i):
            continue
    
        g = find_generators(i)

        if len(g) == 0: continue

        print("For",i)
        for z in range(1,i):
            x = set([pow(z,j,i) for j in range(1,i)])
            print(x)
        print("Generators:", g)
