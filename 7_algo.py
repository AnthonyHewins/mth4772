def mod3(num):
    """
    10 % 3 = 1.
    Take a number, say n=123456, and split it up like so:

    n = 1*(100000) + 2*(10000) + 3*(1000) + 4 * (100) + 5 * (10) + 6
      = 1 + 2 + 3 + 4 + 5 + 6 = 21 under mod 3; therefore 123456 % 3 == 0.
    """

    string = str(num)
    x = sum(map(lambda x: int(x), string))
    return x % 3 == 0

def mod7(num):
    """
    1001 % 7 = 0 -> 1000 % 7 = -1.
    So we exploit that fact.
    Take num to be a string. Look at each digit place.
    Logically, split it up into 3-tuples.
    Programmatically we don't do this.
    e.g. 23456789 -> (023)(456)(789)

    Write it out like this:
    num =   (a0+(a1*10)+(a2*100))
     +1000  (a3+(a4*10)+(a5*100))
     +1000^2(a6+(a7*10)+(a8*100))
    etc.

    And now since 1000 % 7 = -1, you only need
    to check the remaining sum of the a's to see if it works
    since the 1000's all drop out to -1.

    e.g. Using the above
         (023)
        -(456) <-- notice the negative, that's important
        +(789)
        ------
          356. That's easier to check by far.

    Or you could just do n % 7 == 0.
    """
    
    x = str(abs(num))
    sum = 0
    parity = 1
    while len(x) >= 1:
        sum += parity * int(x[-3:])
        x = x[:-3]
        parity *= -1

    return sum % 7 == 0
    
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Determines if a number is divisible by 7 by algorithm (not with a simple %)")
    parser.add_argument("num", type=int, help="The number")
    parser.add_argument("mod", nargs='?', type=int, choices=[7, 3], default=7, help="The modulo")
    args = parser.parse_args()

    if args.mod == 7:
        print(mod7(args.num))
    else:
        print(mod3(args.num))
