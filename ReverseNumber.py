def reverseNumber(n):
    temp = n
    rev = 0
    while (n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print("The Reverse of Number ",temp," is ", rev)


n = int(input("Enter an Positive Number : "))
reverseNumber(n)
