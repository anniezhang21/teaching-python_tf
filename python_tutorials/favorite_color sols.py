# while loops
guessed = False
favorite_color = "green"
while not guessed:
    color = input("Guess my favorite color: ")
    if color == "green":
        print("You guessed right!")
        guessed = True
    else:
        print("You guessed wrong! Try again!")

# Try running the code above in PyCharm. What does it do?
# Can you change the code so that you can only guess 3 times? (Hint: Use a for loop)










# Favorite color quiz

choice1 = "red"
choice2 = "white"
choice3 = "pink"
choice4 = "green"

red = 0
white = 0
pink = 0
green = 0

print("What is your favorite color?")
print("1) Red \n2) White \n3) Pink \n4)Green")
ans = input("What is your choice? Enter 1, 2, 3, or 4.")

if ans == "1":
    red += 1
elif ans == "2":
    white += 1
elif ans == "3":
    pink += 1
else:
    green += 1

result = max([red, white, pink, green])

if result == red:
    print("You picked " + choice1 + ". Your favorite season is Fall!")
elif result == white:
    print("You picked " + choice2 + ". Your favorite season is Winter!")
elif result == pink:
    print("You picked " + choice3 + ". Your favorite season is Spring!")
else:
    print("You picked " + choice4 + ". Your favorite season is Summer!")
