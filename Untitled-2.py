num = int(input("Enter a number: "))
remainder = num % 7

if remainder == 0:
    print(f"{num} is divisible by 7")
else:
    print(f"{num} is not divisible by 7")
