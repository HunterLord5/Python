n = 26
print("Guess a number!" "\nYou have 5 chances to guess the exact number: ", end="\n")
count = 5

while count > 0:
    inp = int(input())
    if inp < n:
        print("Your no. is lesser, try again")
    elif inp > n:
        print("Your no. is greater, try again")
    else:
        print("Congrats!, you guessed the correct number")
        break
    count -= 1
    print("you left with", count, "guess")
    if count == 1:
        print("Game over!")
