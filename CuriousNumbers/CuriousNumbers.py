import math

digits = []
fact = []
num = 0
i=1

while True:
    for letter in str(i):
        digits.append(letter)
    for x in range(0,len(digits)):
        num = num + math.factorial(int(digits[x]))
    if(i==num):
       fact.append(num)
       num=0
       digits.clear()
       
    else:
        digits.clear()
        num=0
    if(len(fact)==4):
        break
    i=i+1
print(f"Curious Numbers: {fact}")
