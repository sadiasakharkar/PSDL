# birthday paradox

import random 

total_day = tuple(range(1 , 366))

count = 0 
n = int(input("enter the number of people in simulation:"))
trail = int(input("Enter the number of trails:"))

for _ in range(trail):
    birthday = []
    duplicate = []
    for _ in range(n):
        month = random.randint(1 , 12)
        year = random.randint(2000, 2026)
        
        if month == 2 :
            if year % 400 == 0 or (year %100 != 0 and year%4 == 0 ):
                day = random.randint(1 , 29)
            else:
                day = random.randint(1 , 28)
        elif month == [1,3, 5 , 7, 8, 10 , 12]:
            day = random.randint(1 , 31)
        else:
            day = random.randint(1 , 30)
        
        birthday.append((day , month , year))
        
    if len(birthday) != len(set(birthday)):
        count += 1
        
probability = count/ trail
print(f"The probability of at least two people sharing a birthday in a group of {n} people is approximately {probability:.4f}")