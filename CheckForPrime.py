def checkPrime(n):
    k = 0
    for i in range(2,n//2+1):
        if(n % i == 0):
            k = k + 1
    if(k <= 0):
        print("The Number ",n," is  PRIME Number")
    else:
        print("The Number ", n, " is Not PRIME Number")


n = int(input("Enter an Positive Number : "))
checkPrime(n)
