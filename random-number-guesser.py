# Programming Concepts
# "Random Number"

# Call in the random function
import random

# Set up our initial guess counter at 0
guess = 0

# Set up the random number under variable "random"
random = random.randint(1, 20)

# Start by telling the user what we're thinking
print "I am thinking of a number between 1 and 20.\n"

# Begin the loop. Since there's no end to this loop,
# as long as the user keeps guessing incorrectly,
# it will never stop. By changing the loop to state that
# after so many guesses, it ends, we can break the loop after
# the user has guessed 'x' times.
while guess >= 0:
    # Prompt the user to input their guess as an integer
    attempt = int(input("What number do you think it is? "))
    
    # Have every input add to our guess value
    guess = guess + 1
    
    # If out input is less than the randomly generated number, display an error and have the user try again.
    if attempt < random:
        print "Too low. Try again.\n"

    # If out input is greater than the randomly generated number, display an error and have the user try again.
    if attempt > random:
        print "Too high. Try again.\n"
    
    # And if the input is correct, break out of the loop.
    if attempt == random:
        break

# Because of an error with concatenates, we convert the interger to a string.
guess = str(guess)
random = str(random)

# And display the congratulatory message, along with the correct number, and the attempts it took to guess it.
print "\nCongratulations! You guessed the correct number!"
print " The correct number was: " + random
print " Number of attempts it took: " + guess
