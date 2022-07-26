#---Program to check if list and it's reverse is same---#


list1=[1, 4, 7, 4, 'list1', -2]#random list
#list1=['one', 2, 'three', 4, 'three', 2, 'one']
list2=list1[::-1]#reverse of list1
#print(list2)

if list1==list2:#conditon when true
    print(bool(True))

else:
    print(bool(False))