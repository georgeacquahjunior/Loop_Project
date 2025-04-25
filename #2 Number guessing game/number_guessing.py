# NUMBER GUESSING GAME (LIMITED TRIES)

# Goal: Generate a random number and let the user guess it within a limited number of attempts.
# Success Criteria: Loop exits when user guesses correctly or attempts run out.
# Stretch Goal: Provide “too high” or “too low” hints.
import random as r

print ('--------- NUMBER GUESSING GAME WITH (3) LIMITED TRIES --------')

#Generate a random number
random_num = r.randint(1, 10)

print(random_num) # sample check

number_of_try = 0
while number_of_try < 3:
    # Give 3 attempts
    # Allow user to guess
    # Check the input against the random number
    user_guess = int(input('What number can you think of between (1 to 10): '))
    if user_guess == random_num:
        print('Well done. Guessed right.😊👌')
        break
    else:
        print(f'Wrong guess. {2 - number_of_try} attempt more.')
    number_of_try = number_of_try + 1
