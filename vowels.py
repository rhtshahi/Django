#----------------------Progtam to count vowels of user input string----------------------#

x=input('Enter any word: ')#taking user input
y=[i for i in x if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U')]#condition to take vowels as list
#print(y)
v=len(y)#length of list
#print(v)

if v==1:
    print('There is 1 vowel.')
else:
    print('There are ',v,' vowels.')
