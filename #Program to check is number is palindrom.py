#Program to check is number is palindrome or not
num = int(input("Enter a number: "))
tempnum = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if tempnum == rev:
    print(f"{tempnum} is a Palindrome number")
else:  
    print(f"{tempnum} is not a Palindrome number")