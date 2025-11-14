num = int(input("Enter a number: "))
remainder = num % 30

if 30 % num == 0:
    print(f"{num} is a factor of 30")
else:
    print(f"{num} is not a factor of 30")
