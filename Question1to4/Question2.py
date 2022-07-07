#A
num = 5 

for num in range(1, num):
    if num % 2 != 0:
        for num in range(1, num+1):
            print("*", end = " ")
    print()
#B
num = 5 
for num in range(num,0,-1):
    if num % 2 != 0:
        for num1 in range(1, num+1 ):
            print("*", end = " ")
    print()

# To Widen the range you need to change A and B to the same number eg. odd number 1 -10, change A and B to 10 manually 