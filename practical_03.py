import random 

total_days = tuple(range(1, 366))

count = 0 
n =  int(input("Enter the number of people in the group: "))
trails = int (input("Enter the number of trails: "))

for _ in range(trails):
    birthday =[]
    
    for _ in range (n):
        month = random.randint(1,12)
        
        if month == 2:
            day = random.randint(1,29)
        elif month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
        else:
            day = random.randint(1,30)
        
        birthday.append((day, month))
    
    if len(birthday) != len(set(birthday)):
        count += 1

probabilty = count / trails ;
print(f"The probability of at least two people sharing a birthday in a group of {n} people is approximately {probabilty:.4f}")