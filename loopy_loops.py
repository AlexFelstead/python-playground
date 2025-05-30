name = "Eric"
for char in name:
    print("Give me a " + char + " !") 

print("\n...\n")

print("\nThe below should print all odd numbers from 1 through 31 on new lines:")
for i in range(1,32,2):
    print(i)

print("\n...\n")

print("\nThe below is iterating over a list and should print 1 2 3 on new lines:")
for num in [1,2,3]:
    print(num)

print("\n...\n")

for i in range(5): # this will not run the else statement as it breaks before as 3 is in range
    print(i)
    if i == 3:
        break
else:
    print("Completed without break")

print("\n...\n")

for i in range(5):
    print(i)
else: print("As the range is 5, this text will appear after 0 1 2 3 4 has been printed to terminal")

print("\n...\n")

from random import randint
fav_number = 77
guess_correct = False

while not guess_correct:
    guess = randint(0, 100)
    if guess == fav_number:
        print("You guessed right: 77!")
        guess_correct = True
    else:
        print(f"{guess} is wrong! Try again.")