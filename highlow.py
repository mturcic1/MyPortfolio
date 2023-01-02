import random

number = int(random.randint(1,100))
attempt_num = 1
attempt = int(input("Guess "+str(attempt_num)+": "))
while number != attempt and attempt_num <= 10:
    if attempt > number:
        print("Guess " + str(attempt_num) + ": " + str(attempt))
        print("Clue: lower")
        attempt = int(input("Guess " + str(attempt_num) + ": "))
        attempt_num += 1
    elif attempt < number:
        print("Guess " + str(attempt_num) + ": " + str(attempt))
        print("Clue: higher")
        attempt = int(input("Guess " + str(attempt_num) + ": "))
        attempt_num += 1

if number == attempt and attempt_num<=10:
    print("You win!")
elif attempt_num>10:
    print("You lose!")