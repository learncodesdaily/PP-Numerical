def checkPalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if temp == rev:
        print("The Number ", temp, " is Palindrome")
    else:
        print("The Number ", temp, " is Not Palindrome")


n = int(input("Enter an Positive Number : "))
checkPalindrome(n)