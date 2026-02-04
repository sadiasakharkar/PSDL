'''
UCE2025002
Subject: PSDL 
Assignment no: Assignment 02

Aim: To understand the List and String datatypes in Python

Problem Statement:
    
Part A: Perform the following operations on Lists:
    
⮚ Append an element to the list.
⮚ Insert an element in the given position.
⮚ Remove an element from the list.
⮚ Print the largest and smallest number from the list.
⮚ Print the second largest number from the list.
⮚ Concatenate two lists.
⮚ Reverse the list.
⮚ Print the numbers from the list which are from the given range.
⮚ Create a copy of the given list.
⮚ Remove repeating elements from the list.
⮚ Use the list as matrix and perform addition of 2 matrices

Part B: Perform the following operations on Strings:

⮚ Find the length.
⮚ Reverse the string.
⮚ Concatenation of two strings.
⮚ Compare two strings.
⮚ Check if Substring is present.
⮚ Convert the string to upper case.
⮚ Count the number of occurrences of a character in a string.
⮚ Count the number of occurrences of a substring in the string.
⮚ Accept a sentence from the user and compute the length of each word in that
sentence.

Part C: Consider a list of words and find the words which are longer than ‘n’
'''

lst = [12, 19, 67, 45, 43, 87, 12]
print("List 1: ",lst)

lst.append(55)
print("Using append(), appended 55: ",lst)

lst.insert(3, 99)
print("using insert() , inserted at 3rd position(0-indexed): ",lst)

lst.remove(19)
print("Removed 19 using remove(value): ",lst)

print("Using min() and max(): ")
print("Largest:" , max(lst))
print("Smallest:" , min(lst))


print("Finding second largest element from list - set(): to avoid dulicate, again casted to list")
unique_ele = list(set(lst))
unique_ele.sort()
print("Second largest: ", unique_ele[-2])

lst2 = ["sadia" , 23, False , 65.3]
print("List 2: ",lst2)

print("Concatenate two lists: ", lst+lst2)

print("Reversed list: " , lst[::-1])

print(lst)
low , high = 50 , 70
print("Numbers in range (50-70)", [ x for x in lst if low <= x <= high])

copy_lst = lst.copy()
print("Copied list: ",copy_lst)

print("Original: " ,lst)
unique_ele = list(set(lst))
print("List with unique elements: " , unique_ele)

print("Matrix additon")

mat1 = [ [1 , 2], 
         [3 , 4], 
         [5 , 6]
        ]

mat2 =[  [7,8],
         [5,7],
         [4,5]
         ]

print("Matrix 1: ", mat1)
print("Matrix 2: ",mat2)

result = []

for i in range(3):
    row = []
    for j in range(2):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)
    
print("Addition of matrix: " , result )

print("----------------------------------")

s1 = "Sadia"
s2 = "Sakharkar"
print("String 1:",s1)
print("String 2: ",s2)

print("Length:", len(s1))

print("Reverse:", s1[::-1])

print("Concatenated:", s1 + " " + s2)

print("Same or Not:", s1 == s2) # returns true or false

print("Substring Present:", "sad" in s1)

print("Uppercase:", s1.upper())

print("Count of 'a':", s1.count('a'))

print("Count of 'sad':", s1.count("sad"))

# Length of each word
# sentence =input("Enter a sentence: ")

# words = sentence.split()
# for word in words:
#    print(word, ":", len(word))

print("----------------------------------")

word_list = input("Enter the word list (separated by space ):").split()
n = int(input("Enter n: "))

longer_word = []

for i in range(len(word_list)):
    if len(word_list[i]) > n :
        longer_word.append(word_list[i])
        
print("The words longer than ", n, "are : " , longer_word)