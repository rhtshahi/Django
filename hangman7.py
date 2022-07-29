#------------------------------HANGMAN-------------------------#

#------------------------------Takes word to be guessed-----------------------#
name=input('Enter word(s) for someone to guess(Without Space): ').upper()
#print(name)
#name_list=[x for x in name]
#print(name_list)

#name_list_len=len(name_list)
#print(name_list_len)

#--Length of word to be guessed--#
name_length=len(name)
#print(name_length)

#---Empty list to store correctly guessed word--#
user_guess=[]

#---length of correctly guessed characters---#
guess_length=0

#-5 wrong attempts-#
life=5

i=0

print('It is a word with %s letters.'%name_length)

#---loop for taking user input n number of times---#
while i<name_length-1:
    #print('It is a word with %s letters.'%name_length)
    if life !=0:
        guess=input('Make a guess: ').upper()
        i=i+1

        if guess not in name:
            life=life-1
            print('Life Remaining: ', life)

            if life==0:
                print('Game Over!!!')
            

        elif guess in name:
            nth=name.index(guess)
            n=nth+1
            print('This letter is at place %s'%n)

            if guess not in user_guess:
                counter=name.count(guess)
                
                for i in range(0,counter):
                    user_guess.append(guess)
                    guess_length=len(user_guess)
                    print(user_guess)
                    #print(guess_length)
    if life!=0 and guess_length==name_length:
        print('CORRECT!!!')
        print('The word is: ',name)
        break