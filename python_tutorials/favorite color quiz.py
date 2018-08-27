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
# Finish the rest of this if/elif/else block!
# YOUR CODE HERE

result = max([red, white, pink, green])

if result == red:
    print("You picked " + choice1 + ". Your favorite season is Fall!")
# Finish the rest of this if/elif/else block!
# YOUR CODE HERE
