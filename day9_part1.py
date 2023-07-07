# Guessing Random Number

import random

number = random.randint(0, 10)
guess = int(input("I'm thinking about a number between 0 and 10. Can You guess it ? "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope. Try again: "))

print("You guessed it. I was thinking about", number)

# Another one Example

people = []

for x in range(1, 9):
    person = input("Enter Your Name: ")
    people.append(person)

index = random.randint(0, 7)
random_person = people[index]
print(people)
print("Picking up a Random Name:", random_person)


colors = ["red", "green", "blue", "yellow", "cyan", "pink"]

while True:
    color = colors[random.randint(0, len(colors)-1)]
    guess1 = input("I'm thinking about a color, can you guess it?")
    while True:
        if color == guess:
            break
        else:
            guess1 = input("Nope. Try again:")

    print("You guessed it i was thinking about", color)
