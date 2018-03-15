from euclidean_algorithm import euclidean_algorithm as gcd

"""
Given a set of congruencies where m_i are pairwise relatively prime:

x === a1 (mod m1)
x === a2 (mod m2)   (define === := "congruent to")
x === a3 (mod m3)
x === a4 (mod m4)
                                       ___  
x has a unique solution mod M, where M=| |m.

Proof: First define
      ___
      | | m 
M1 = -------
       m1   

x = (a1)(M1)(y1) + (a2)(M2)(y2) + ...
where y_r is the inverse of M_r.

Notice x % (anything not m1) = 0 when we look at anything that isn't mod m1,
since they all contain a factor of all the other m's, and so drop to 0.
This they are all relatively prime.

This means (if we look at n=1) we are left with

(a1)(M1)(y1) === a1 (mod m1)

After some trial and error, we find y1, and that means M1 * y1 === 1 (mod m1). So

a1 * 1 === a1 (mod m1).
"""

def crt(mods, congruencies):
    big_m = 1
    for i in mods:
        big_m *= i
    
    m = []
    for i in mods:
        m += [big_m / i]

    y = []
    for i in range(len(mods)):
        coefficient = m[i] % mods[i]
        for j in range(mods[i]):
            if coefficient * j % mods[i] == 1:
                y += [j]
                break

    for i in range(len(y)):
        y[i] *= m[i] * congruencies[i]
        
    return sum(y) % big_m
        
def relatively_prime(array):
    if type(array) is int: return True
    
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if gcd(array[i], array[j], suppress_prints=True) != 1:
                return False

    return True
    
if __name__ == "__main__":
    from argparse import ArgumentParser
    
    def positive_integer(x):
        try:
            x = int(x)
            return abs(x)
        except:
            raise TypeError("All entries need to be positive ints, or it will force that type on them.")
            
    parser = ArgumentParser(description="Chinese remainder theorem")
    parser.add_argument("-a", "--array-of-mods", type=positive_integer, nargs='+', help="The relatively prime numbers to use in the mod")
    parser.add_argument("-c", "--congruencies", type=positive_integer, nargs='+', help="The congruent numbers you want to solve")
    args = parser.parse_args()

    if len(args.array_of_mods) != len(args.congruencies):
        print("This isn't a valid set of equations, we need equal length arrays")
        exit()
    
    if not relatively_prime(args.array_of_mods):
        print("The mods aren't relatively prime, chinese remainder theorem cannot solve this, exiting")
        exit()

    print("Solving this system of equations:")
    for i in range(len(args.congruencies)):
        print("x === %d (mod %d)" % (args.congruencies[i], args.array_of_mods[i]))
        
    for i in range(len(args.array_of_mods)):
        args.congruencies[i] %= args.array_of_mods[i]
        
    print(crt(args.array_of_mods, args.congruencies))
