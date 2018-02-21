def mod_7(num):
    """
    So 1001 % 7 = 0. So we exploit that fact.
    Take num to be a string. Look at each digit place.
    Split it up into 3-tuples.
    e.g. 23456789 -> (023)(456)(789)


    Write it out like this:
    num = (a0)+(a1*10)+(a2*100)
     +1000(a3+(a4*10)+(a5*100))
    etc.

    And now since 1000 % 7 = -1, you only need
    to check the remaining sum of the a's to see if it works
    since the 1000's all drop out to -1.
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
    args = parser.parse_args()
    print(mod_7(args.num))
