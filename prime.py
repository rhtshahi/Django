#-----------Program to check prime number----------#

num=int(input('Enter a number: '))#Taking user input

#Conditions
if num>1:
    for i in range(2,num):
        if(num%i==0):#Checking if the number is divisible by any numbers between 2 and user input
            print(num,' is not a Prime number.')
            break
    else:
        print(num,' is a Prime number.')
else:
    print(num,' is a Prime number.')
