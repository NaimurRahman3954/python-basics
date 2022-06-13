import random as r
# thus we won't have to write 'random' over and over again. Here 'random is a library.

secretAge = r.randint(20, 30)
flag = True


def game(guessedAge, secretAge):
    if guessedAge < secretAge:
        return "too low"
    elif guessedAge > secretAge:
        return "too high"
    else:
        return "CORRECT!"


guessedAge = 0

for i in range(5):
    print("Guess my age, Homie! You have "+str(5-i)+" guesses left")
    guessed = input()
    guessedAge = int(guessed)
    answer = game(guessedAge, secretAge)
    print(answer)
