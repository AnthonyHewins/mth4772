class Iteration():
    def __init__(self, dividend=0, divisor=0, multiples=0, remainder=0):
        dividend = dividend
        divisor = divisor
        multiples = multiples
        remainder = remainder
"""
def linear_combination(gcd, stack):
    previous_dividend, previous_divisor = None, None
    if stack:
        iteration = stack.pop()
        previous_dividend = iteration.dividend
        previous_divisor = iteration.divisor

    while stack:
        iteration = stack.pop()
        dividend = iteration.dividend
        divisor = iteration.divisor
        remainder = iteration.remainder
"""     
        
def euclidean_algorithm(int1, int2):
    if int1 == int2:
        print("They're equal, the answers obvious!")
        return int1
    if int1 < int2:
        int1, int2 = int2, int1

    stack = []
    dividend = int1
    divisor = int2
    multiples = int1 // int2
    remainder = int1 % int2
   
    while remainder != 0:
        print("%d = %d(%d) + %d" % (dividend, divisor, multiples, remainder))

        stack += [Iteration(dividend=dividend, divisor=divisor, multiples=multiples, remainder=remainder)]
        dividend = divisor
        divisor = remainder
        multiples = dividend // divisor
        remainder = dividend % divisor

    print("%d = %d(%d) + %d" % (dividend, divisor, multiples, remainder))
    print("GCD = %d" % divisor)
    
    return divisor, stack
    
if __name__ =="__main__":
    from argparse import ArgumentParser

    def valid_int(x):
        try:
            x = int(x)
        except:
            raise TypeError("Must be an int")
        if x > 0:
            return x
        else:
            raise TypeError("Not allowing negatives for this particular program")
    
    parser = ArgumentParser(description="Euclidean Algorithm (add 2 numbers to the commandline)")
    parser.add_argument("int1", type=valid_int, help="One of the ints (automatically detects which is larger)")
    parser.add_argument("int2", type=valid_int, help="One of the ints (automatically detects which is larger)")
    parser.add_argument("--no-lin-combination", action='store_true', help="Don't find a linear combination")
    args = parser.parse_args()

    gcd, stack = euclidean_algorithm(args.int1, args.int2)

#    if not args.no_lin_combination:
#       linear_combination(gcd, stack)
