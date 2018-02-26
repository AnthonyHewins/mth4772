def extended_euclidean_algorithm(int1,int2):
    if int1 < int2:
        int1, int2 = int2, int1

    x,y,u,v = 0,1,1,0
    while int1 != 0:
        quotient, remainder = int2//int1, int2%int1
        m, n = x-u*quotient, y-v*quotient
        int2,int1, x,y, u,v = int1,remainder, u,v,m,n
    return x, y

def euclidean_algorithm(int1, int2, suppress_prints=True):
    if int1 == int2:
        return int1
    if int1 < int2:
        int1, int2 = int2, int1

    dividend = int1
    divisor = int2
    multiples = int1 // int2
    remainder = int1 % int2
   
    while remainder != 0:
        if not suppress_prints: print("%d = %d(%d) + %d" % (dividend, divisor, multiples, remainder))

        dividend = divisor
        divisor = remainder
        multiples = dividend // divisor
        remainder = dividend % divisor

    return divisor
    
if __name__ =="__main__":
    from argparse import ArgumentParser

    def valid_int(x):
        try:
            return abs(int(x))
        except:
            raise TypeError("Euclidean algorithm only makes sense with integer inputs")
    
    parser = ArgumentParser(description="Euclidean Algorithm (add 2 numbers to the commandline)")
    parser.add_argument("int1", type=valid_int, help="One of the ints (automatically detects which is larger)")
    parser.add_argument("int2", type=valid_int, help="One of the ints (automatically detects which is larger)")
    parser.add_argument('-nl', "--no-linear-combination", action='store_true', help="If you don't want to see a linear combination afterwards, flag this")
    parser.add_argument('-s', "--suppress-prints", action='store_true', help="If you don't want the process to print the process out, flag this")
    args = parser.parse_args()

    if args.int1 < args.int2: args.int1, args.int2 = args.int2, args.int1
    
    if not args.suppress_prints:
        print("Euclidean algorithm:")
        print("====================================")
    gcd = euclidean_algorithm(args.int1, args.int2, suppress_prints=args.suppress_prints)
    print("GCD: %d" % gcd)
    print("\n")
    
    if not args.no_linear_combination:
        x,y = extended_euclidean_algorithm(args.int1, args.int2)
    
    if not args.suppress_prints:    
        print("Extended Euclidean algorithm:")
        print("====================================")
    print("%d = (%d)%d + (%d)%d" % (gcd, x, args.int1, y, args.int2))
    print("All solutions:")
    print("x = %d + %dn" % (y, args.int1 / gcd))
    print("y = %d - %dn" % (x, args.int2 / gcd))
