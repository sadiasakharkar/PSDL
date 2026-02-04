#
# Programming for System Design Lab (PSDL)
# Assignment No: 01
#
# Name     : Sadia Ansar Husain Sakharkar
# UCE No   : UCE2025002
# Subject  : PSDL
#
# Aim:
# To study and implement basic programs using Python programming language.


# 1. Write a Python program to check whether the given number
#    is even or odd.
# OUTPUT:
# Enter positive number: 86
# 86 is an even number
#
# Enter positive number: 67
# 67 is an odd number
#
# Enter positive number: -83
# Number should be a positive number

num = int(input("Enter positive number: "))

if num >= 0:
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
else:
    print("Number should be a positive number")


# 2. Write a Python program to print a pyramid pattern using *
# OUTPUT:
# Enter the number of rows: 5
#     *
#    ***
#   *****
#  *******
# *********
#
# Enter the number of rows: -2
# Enter a valid number

rows = int(input("\nEnter the number of rows: "))

if rows > 1:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))
else:
    print("Enter a valid number")


# 3. Write a Python program to print Fibonacci series
# OUTPUT:
# Enter number of terms: 10
# Fibonacci series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
#
# Enter number of terms: 0
# Enter a positive number > 0

n = int(input("\nEnter number of terms: "))
a, b = 0, 1

if n > 0:
    print("Fibonacci series:")
    for i in range(n):
        print(a)
        a, b = b, a + b
else:
    print("Enter a positive number > 0")


# 4. Write a Python program to find factorial of a number
# OUTPUT:
# Enter a number: 5
# Factorial of 5 is: 120
#
# Enter a number: -5
# Please enter a valid number

num = int(input("\nEnter a number: "))
fact = 1

if num > 0:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is:", fact)
else:
    print("Please enter a valid number")


# 5. Write a Python program to reverse a number entered by user
# OUTPUT:
# Enter a number: 123456
# Reversed number: 654321
#
# Enter a number: 623784
# Reversed number: 487326

num = int(input("\nEnter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)


# 6. Write a Python program to count the number of digits
#    in a given integer
# OUTPUT:
# Enter a number: 6472864
# Number of digits are: 7

num = int(input("\nEnter a number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Number of digits are:", count)


# 7. Write a Python program to implement Number Guessing Game
# OUTPUT:
# ----Number Guessing Game----
# *You will be given 3 tries*
#
# Guess the number (1-10): 9
# Try Again!
#
# Guess the number (1-10): 2
# Try Again!
#
# Guess the number (1-10): 4
# Try Again!
#
# The correct number was 7
#
# Guess the number (1-10): 5
# Correct!!!! You won!!
# The correct number was 5

import random

print("\n----Number Guessing Game----")
random_number = random.randint(1, 10)
print("*You will be given 3 tries*")

for i in range(3):
    num = int(input("\nGuess the number (1-10): "))
    if num == random_number:
        print("Correct!!!! You won!!")
        break
    else:
        print("Try Again!")

print("\nThe correct number was", random_number)


# 8. Write a Python program to find factors of a number
# OUTPUT:
# Enter a number: 56
# The factors are:
# 1
# 2
# 4
# 7
# 8
# 14
# 28
# 56

num = int(input("\nEnter a number: "))

if num > 0:
    print("The factors are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    print("Please enter a valid number")


# 9. Write a Python program to find sum of digits of a number
# OUTPUT:
# Enter a positive number: 4546
# Sum of digits: 19

num = int(input("\nEnter a positive number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num = num // 10

print("Sum of digits:", sum_digits)


# 10. Write a Python program to find prime numbers
#     in the given range
# OUTPUT:
# Enter start range: 2
# Enter end range: 25
# Prime numbers are:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23


start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# 11. Write a Python program to implement Collatz Conjecture
# 
# OUTPUT:
# Enter a positive number: 20
# 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# Enter a positive number: 25
# 25 -> 76 -> 38 -> 19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 ->
# 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 ->
# 8 -> 4 -> 2 -> 1

n = int(input("\nEnter a positive number: "))

while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(1)
