# even or odd
num = int(input("Enter a number:"))

if(num > 0) :
    if(num % 2 == 0 ):
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Enter a valid number")


# pyramid 

rows = int(input("Enter numbers of rows"))

if(rows > 1):
    for i in range(1 , rows+ 1):
        print(" " * (rows-i), end="")
        print("* " * 2*i-1)
else:
    print("Enter a valid number")


# fibonacci series

n = int(input("ENter a number:"))
a, b = 0, 1

if(n > 0):
    print("Fibo")
    print(a)
    for i in range(1, n):
        print(b)
        a, b = b, a + b
else:
    print("Enter a valid number")


# factorial of number

num = int(input("Enter a number:"))
factorial = 1

if(num > 0):
    for i in range(1 , num+1):
        factorial *= i
    print("Factorial of", num, "is", factorial)
else:
    print("Enter a valid number")

# reverse of a number

number = int(input("Enter a number:"))

reverse = 0 

while number > 0: 
    digit = number % 10
    rev = rev * 10 +digit
    number //= 10

print("Reverse of the number is:", rev)

# count the number of digit in given number

number = int(input("Enter a number:"))
count = 0 

while number > 0 :
    count +=1
    number //= 10

print("Number of digits in the number is:", count)

# Number guessing game 

import random
print("Welcome to the Number Guessing Game!")
print("You will be given 3 guesses:")
number = random.randint(1,10);

for i in range(3):
    user = int(input("Guess a number between 1 to 10"))
    if(user == number):
        print("You won")
        break
    else:
        print("Try again")

print("You lost! The number was", number)

# factors of numbers 

number = int(input("Enter a number:"))
print("Factors of", number, "are:")

if(number > 0 ):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
else:    
    print("Enter a valid number")
    
# sum of digits in a number

num = int(input("Enter a number:"))
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum of digits in the number is:", sum)