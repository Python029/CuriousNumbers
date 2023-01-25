import math

digits = []
fact = []
num = 0
i=1

while True:
    for thing in str(i):
        #Seperate Digits
        digits.append(thing)
    for x in range(0,len(digits)):
        #Add Factorials of Individual Digits
        num = num + math.factorial(int(digits[x]))
    if(i==num):
        #Add Curious Number to List
        fact.append(num)
        num=0
        digits.clear()
       
    else:
        #Reset Variables
        digits.clear()
        num=0
    if(len(fact)==4):
        break
    i=i+1
print(f"Curious Numbers: {fact[0]}, {fact[1]}, {fact[2]}, {fact[3]}")
