#------------Program to filter even numbers from list------------#

list1=[i for i in range(51)]#list of numbers from 1 to 50
#print(list1)
evenList=[x for x in list1 if x>1 and x%2==0]#condition to select even numbers from the list
print(evenList)