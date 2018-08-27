# Common bugs:
#   1) input() always returns a string. e.g. Make sure you're using "1" instead of 1
#   2) Are you using if where you should be using elif? (Or vice versa)
#   3) Make sure everything is properly indented.

def buzzfeed():
    """ Simulate a buzzfeed style personality quiz.
    Quiz idea from "Order From Subway And We'll Give You A Netflix Original Show To Watch"
    Source: raechilling https://bzfd.it/2JdnKjG
    """
    # Pick the possible results you want!
    choice1 = "The Flash"
    choice2 = "The Crown"
    choice3 = "Stranger Things"
    choice4 = "Chef's Table"

    # Change these variable names to match yours!
    theFlash = 0
    theCrown = 0
    strangerThings = 0
    chefsTable = 0

    # Write some flavor text for your answers. Be more creative than me!
    flashText = "Follow Barry Allen's adventures!"
    crownText = "Highly recommend 10/10"
    strangerText = "Can you spot all the 80s references?"
    chefsText = "I've never actually seen this show."

    # Question 1
    print("Choose a breakfast item from Subway.")  # Note below: \n begins a new line.
    print("1) Bacon, egg, and cheese. \n2) Egg and cheese. \n3) Steak egg and cheese. \n4) Coffee.")
    ans1 = input("What is your choice? Enter 1, 2, 3, or 4: ")
    if ans1 == "1":
        theFlash += 1
    # Finish the rest of this if/elif/else suite!
    # YOUR CODE HERE
    elif ans1 == "2":
        theCrown += 1
    elif ans1 == "3":
        strangerThings += 1
    else:
        chefsTable += 1

    # Optional: Add additional questions!

    # Question 2
    # YOUR CODE HERE
    print("Choose a lunch item from Subway.")  # Note below: \n begins a new line.
    print("1) Spicy Italian Sandwich. \n2) Black Forest Ham Sandwich. \n3) Club Sandwich. \n4) Just a cookie.")
    ans2 = input("What is your choice? Enter 1, 2, 3, or 4: ")
    if ans2 == "1":
        theFlash += 1
    # Finish the rest of this if/elif/else suite!
    # YOUR CODE HERE
    elif ans2 == "2":
        theCrown += 1
    elif ans2 == "3":
        strangerThings += 1
    else:
        chefsTable += 1


    # Question 3
    # YOUR CODE HERE

    # Question 4
    # YOUR CODE HERE

    # Include all the possible choices, separated by commas.
    result = max([theFlash, theCrown, strangerThings, chefsTable])

    if result == theFlash:
        print("You should watch " + choice1 + ". " + flashText)  # The + operator is also used to concatenate strings.
    # Finish the rest of this if/elif/else clause!
    # YOUR CODE HERE
    elif result == theCrown:
        print("You should watch " + choice2 + ". " + crownText)
    elif result == strangerThings:
        print("You should watch " + choice3 + ". " + strangerText)
    else:
        print("You should watch " + choice4 + ". " + chefsText)

# The line of code below starts the quiz.
buzzfeed()
