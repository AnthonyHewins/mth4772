def extended_euclidean_algorithm(int1,int2):
    if int1 < int2:
        int1, int2 = int2, int1

    x,y,u,v = 0,1,1,0
    while int1 != 0:
        quotient, remainder = int2//int1, int2%int1
        m, n = x-u*quotient, y-v*quotient
        int2,int1, x,y, u,v = int1,remainder, u,v,m,n
    return x, y
