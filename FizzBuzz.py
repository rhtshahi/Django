#-----Program to separate multiple of 3, 5 and both 3 and 5 and display result accordingly----#

for i in range(0,101):
    #print(i)

    if(i%3==0 and i%5==0):#if the number is multiple of both 3 and 5
        print('FizzBuzz')

    elif(i%3==0):#if the number is multiple of 3 only
        print('Fizz')

    elif(i%5==0):#if the number is multiple of 5 only
        print('Buzz')

    else:#numbers which are not multiple of both 3 and 5
        print(i)    