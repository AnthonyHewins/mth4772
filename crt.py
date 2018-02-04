from euclidean_algorithm import euclidean_algorithm as gcd

def crt(mods, congruencies):
    # Find the M's

    big_m = reduce(lambda x,y:return x*y, mods)
    m = []
    for i in mods:
        m += [big_m / i]

    for i in range(len(mods)):
        coefficient = m[i] % mods[i]
        inverse = None
        for j in range(1, mods[i]):
            if j * coefficient % mods[i] == congruencies[i]:
                inverse = j
        
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
    
    parser = ArgumentParser(description="Chinese remainder theorem")
    parser.add_argument("-a", "--array-of-mods", type=int, nargs='+', help="The relatively prime numbers to use in the mod")
    parser.add_argument("-c", "--congruencies", type=int, nargs='+', help="The congruent numbers you want to solve")
    args = parser.parse_args()

    if len(args.array_of_mods) != len(args.congruencies):
        print("This isn't a valid set of equations, we need equal length arrays")
        exit()
    
    if not relatively_prime(args.array_of_mods):
        print("The mods aren't relatively prime, exiting")
        exit()    