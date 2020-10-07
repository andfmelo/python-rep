import random

random_integer = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

list_of_guesses = [0]

while True:

    guess = int(input("Enter a value between 1 and 100: "))
    list_of_guesses.append(guess)
        
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Try again!")
        #The continue statement in Python returns the control to the beginning of the 
        #while loop. The continue statement rejects all the remaining statements in the 
        #current iteration of the loop and moves the control back to the top of the loop.
        continue 
        
    elif list_of_guesses[-1] == random_integer:
        print("CONGRATULATIONS, YOU GUESSED IT IN ONLY {} GUESSES".format(len(list_of_guesses)-1))
        break
    
    elif abs(list_of_guesses[-1] - random_integer) <= 5:
        print("WARMER!")
        
    elif abs(list_of_guesses[-1] - random_integer) > 15:
        print("COLDER!")
     
     
    elif abs(list_of_guesses[-1] - random_integer) <= 10:
        print("WARM!")
        
    elif abs(list_of_guesses[-1] - random_integer) > 10:
        print("COLD!")
        
