
import random


def highlow():
           
        number = random.randint(1,20) #change the numbers to whatever you want
        #create a counter
        counter = 0
        #create a while loop
        while True:
                #ask the user for a guess
                guess = int(input("Guess a number between 1 and 20: "))
                #increase the counter
                counter += 1
                #if the guess is correct
                if guess == number:
                        #print the number of guesses
                        print("You guessed it in", counter, "guesses, congratulations!")
                        #break the loop
                        break
                #if the guess is too high
                elif guess > number:
                        #print the number of guesses
                        print("Your guess is too high. Try again.")
                        print()
                #if the guess is too low
                elif guess < number:
                        #print the number of guesses
                        print("Your guess is too low. Try again.")
                        print()
                
                
                
                
                
#call the highlow function
highlow()

