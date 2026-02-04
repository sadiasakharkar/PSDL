import random

total_days=tuple(range(1,366))
n=int(input("Enter the number of people in the group: "))
trials=int(input("Enter the number of simulations to run: "))

same_day_birthday=0
for i in range (trials):
    birthdays=[]
   
    for i in range(n):
        birthday=random.choice(total_days)
        birthdays.append(birthday)
       
        #to check if there are any duplicate values
    if len(birthdays)!=len(set(birthdays)):
        same_day_birthday+=1
         
probability=same_day_birthday/trials
print("Estimated probability: ")
print("In a grounp of" , n , "people, the probability that atleast two people share the same birthday is: " ,probability )