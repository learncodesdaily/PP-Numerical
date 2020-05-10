def sumOfDigits(n):
    temp = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    print("The Sum of Digits of Number  ", temp, " is : ", sum)


n = int(input("Enter an Positive Number : "))
sumOfDigits(n)
