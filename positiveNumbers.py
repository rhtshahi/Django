#----------------------Program to return positive numbers in mix list-------------------------#

mixed_list=[1, 3, 'abc', 'xyz', 14, 10, -4, -17, 'python', 2, 18, 'list']#,ixed list

list1=list(x for x in mixed_list if isinstance(x, int))#separating integers from mixed list
#print(list1)

positive_list=[x for x in list1 if x>0]#selecting poitive numbers from mixed list
print(positive_list)