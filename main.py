#Week 3 Homework: Mini Trivia

print('''Welcome to Trivia! 

Tonight we'll be focusing on 3 categories: 
    [1] Sports
    [2] Science
    [3] Pop Culture
    ''')

scienceQuestion = "Name the scientist who invented blood plasma: "
scienceAnswer = "Charles Drew"
sportsQuestion = "Name the first African American to play in Major League Baseball: "
sportsAnswer = "Jackie Robinson"
popQuestion = "Name the music icon referred to as the King of Pop: "
popAnswer = "Michael Jackson"

userCategoryChoice = int(input("Please enter the number that corresponds to your category of choice: "))

if not (userCategoryChoice == 1 or userCategoryChoice == 2 or userCategoryChoice == 3):
    print('That is not a valid option.')
elif userCategoryChoice == 1:
    print(f"You've selected Sports. Here's your sports trivia question.")
    sportsResponse = input(f"{sportsQuestion}")
    print(f"Your answer is: {sportsResponse}")
    if sportsResponse.lower() == sportsAnswer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
elif userCategoryChoice == 2:
    print(f"You've selected Science. Here's your science trivia question.")
    scienceResponse = input(f"{scienceQuestion}")
    print(f"Your answer is: {scienceResponse}")
    if scienceResponse.lower() == scienceAnswer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
else:
    print(f"You've selected Pop Culture. Here's your pop culture trivia question.")
    popCultureResponse = input(f"{popQuestion}")
    print(f"Your answer is: {popCultureResponse}")
    if popCultureResponse.lower() == popAnswer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
