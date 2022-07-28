#----------------filter to get values consisting letters a b c-----------------#
a = {'1':'pending', '2': 'approved', '3':'abcd', '4':'Name', '5':'Hello', 6:'Ant'}#random dictionary

for x in a:
    # print(a[x])
    # print(type(a[x]))
    key_value=a[x]#getting values of the dictionary
    #print(key_value)

    #----Checking if the values from dictionary contains the mentioned letters----#
    
    if 'a' in key_value:
        print(key_value)

    elif 'b' in key_value:
         print(key_value)

    elif 'c' in key_value:
        print(key_value)

    elif 'A' in key_value:
         print(key_value)

    elif 'B' in key_value:
        print(key_value)

    elif 'C' in key_value:
         print(key_value)

# dict1=dict({'Name: ': 'Ramesh', 'Age: ' : 45, 'Role: ':'Application Developer'})
# length=len(key_value)
# print(key_value)




        
# for x in a:
#     #print(a[x])
#     if 'a' or 'b' or 'c' in a[x]:
#         print(a[x])
#     else:
#         print('None of the values have a or b or c.') 

# name='Rohit'

# if 'y' in name:
#     print('Found')
# else:
#     print('not found')