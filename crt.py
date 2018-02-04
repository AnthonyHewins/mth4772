from euclidean_algorithm import euclidean_algorithm as gcd

def relatively_prime(array):
    if type(array) is int: return True
    
    if gcd(array[i], array[i+1]) != 1:
        return False
    
    
if __name__ == "__main__":
    from argparse import ArgumentParser
    
    parser = ArgumentParser(description="Chinese remainder theorem")
    parser.add_argument("array_of_mods", type=int, nargs='+', help="The relatively prime numbers to use in the mod")
    parser.add_argument("congruencies", type=int, nargs='+', help="The congruent numbers you want to solve")
    args = parser.parse_args()

    if len(args.array_of_mods) != len(args.congruencies):
        print("This isn't a valid set of equations, we need equal length arrays")
        exit()

    if not relatively_prime(array_of_mods):
        print("The mods aren't relatively prime")
        exit()

    
