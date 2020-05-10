def countDigits(n):
    temp = n
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10

    print("The Coount of Digits in ", temp, " is : ", count)


n = int(input("Enter an Positive Number : "))
countDigits(n)