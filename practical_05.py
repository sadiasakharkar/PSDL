# from functools import reduce
# import operator

# program to find the factorial of a number
number = int(input("Enter a number: "))
factorial = reduce(lambda x, y: x * y, range(1, number + 1))
print("Factorial =", factorial)

# program to create a recursive function to add elements
def recursive(lst):
    ans = 1
    user = input("Enter fruit: ")
    lst.append(user)
    ans = input("Do you want to add more ? 0 or 1")
    if ans == '1':
        recursive(lst)
    else:
        print(lst)
        return 
    
lst = []
recursive(lst)

# program to use mapping for temperature conversion
c = [0, 10, 20, 30, 40]

f = list(map(lambda x : x* (9/5) + 32 , c))
print(f)
print(c)

# program to find the average
lst = [1, 2, 3, 4, 5]
total = reduce(lambda x, y : x+y, lst)
average = total /len(lst)

# program to filter employees by department
employees = [{"id": 1, "name": "Gargi Kajave", "dept": "HR"},
{"id": 2, "name": "Rahul Kajave", "dept": "IT"},
{"id": 3, "name": "Sara Kausale", "dept": "IT"},
{"id": 4, "name": "Neena Mehta", "dept": "Finance"}
]

it = list(filter(lambda x : x['dept'] == 'IT', employees))
print (it)

# program to find square
def square(x):
    return x*x

lst = [1, 2, 3, 4, 5]
squared = list(map(square , lst))
print(squared)

# program to reverse a string
string = "Hello World"
reversed = list(map(lambda x : x , string[::-1]))
print(reversed)

lst = ["apple", "banana", "cherry", "date"]
reversed_lst = list(map(lambda x : x[::-1] , lst))
print(reversed_lst)


