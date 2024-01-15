import time

# Taking input from the user
name = input("What is your name? ")
print("Hi, " + name + ". Good luck playing guessing game!!!")
time.sleep(1)

print("Start guessing....")
time.sleep(0.5)

word = "deranged"
guess = ''
turn = 8

while turn > 0:
    count = 0

    for char in word:
        if char in guess:
            print(char, end=" ")  # prints the next character in the same line
        else:
            print("_", end=" ")

            count += 1  # Increment count when a character is not guessed

    if count == 0:
        print("\nCongrats, You won")
        break

    guessed = input("\nguess a character: ")
    guess += guessed  # to concatenate the guessed character into the guess string

    if guessed not in word:
        turn -= 1
        print("Wrong guess...")
        print("You have", turn, "turns left.")

    if turn == 0:
        print("You lose.")
