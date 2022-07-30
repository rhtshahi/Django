#--------------------Hangman----------------------#

#Taking word as input to be guessed
word=input('Enter word to be guessed: ').upper()#converting to upper for easy comparision
#print(word)
hint=input('Hint:')
print(hint)
print('The word is of length %s.'%len(word))#displaying the length of word to be guessed

list_word=list(word)#converting user input string into list

print(list_word)#displaying typed word in order to check
#print(len(list_word))
#list_word.sort()
#print(list_word)

#creating empty list to store correctly user guessed characters
user_guess=[]

life=5#definning the number of wrong attempts

#--------------While loop with multiple conditions---------#
#program runs until the correcrt guess is made or life is remaining

while len(user_guess)!=len(list_word):

    if len(user_guess)!=len(list_word):
        
        #-----User can play until they have a life remaining-----#
        if life!=0:
            guess=input('Enter your guess: ').upper()#taking user input as guess in upper case
            print(guess)

            #---If user guessed a character correctly---#
            if guess in word:

                if guess not in user_guess:

                    counter=word.count(guess)#counting how many times the letter or character is being repeated

                    for i in range(0, counter):
                        user_guess.append(guess)#adding the correct guess n number of times
                        print(user_guess)

                else:
                    print('The word is already guessed!!!')#displaying this message if the letter is already guessed
            
            #-------If the character guessed is incorrect----#
            elif guess not in list_word:
                print('Incorrect!!!')
                life=life-1#decreasing life after each wrong guess
                print('You have %s Life remaining.'%life)#displaying the remaining life

                #-Condition when no life left-#
                if life==0:
                    print('')
                    print('Game Over!!!')
                    print('The correct word is %s.'%word)#displaying the correct word after end
                    break#ending loop after game is over
    
    #-------If user guesses every character in the word------#
    if len(user_guess)==len(list_word):
        print('')
        print('Correct')
        print('%s is the correct word.'%word)
        break#ending loop if correct word is guessed