#-----Program to check palindrome string------#

x=input("Enter any word: ")#Takes user input
y=x[::-1]#reverse the user entered word

#conditions
if x==y:
    print('The word you entered is palindrome.')

else:
    print('It is not palindrome.')