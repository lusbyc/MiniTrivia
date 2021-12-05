#Week 3 Homework: Mini Trivia

print('''Welcome to Trivia! 

Tonight we'll be focusing on 3 categories: 
    [1] Sports
    [2] Science
    [3] Pop Culture
    ''')

science_question = "Name the scientist who invented blood plasma: "
science_answer = "Charles Drew"
sports_question = "Name the first African American to play in Major League Baseball: "
sports_answer = "Jackie Robinson"
pop_question = "Name the music icon referred to as the King of Pop: "
pop_answer = "Michael Jackson"

user_category_choice = int(input("Please enter the number that corresponds to your category of choice: "))

if not (user_category_choice == 1 or user_category_choice == 2 or user_category_choice == 3):
    print('That is not a valid option.')
elif user_category_choice == 1:
    print(f"You've selected Sports. Here's your sports trivia question.")
    sports_response = input(f"{sports_question}")
    print(f"Your answer is: {sports_response}")
    if sports_response.lower() == sports_answer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
elif user_category_choice == 2:
    print(f"You've selected Science. Here's your science trivia question.")
    science_response = input(f"{science_question}")
    print(f"Your answer is: {science_response}")
    if science_response.lower() == science_answer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
else:
    print(f"You've selected Pop Culture. Here's your pop culture trivia question.")
    pop_culture_response = input(f"{pop_question}")
    print(f"Your answer is: {pop_culture_response}")
    if pop_culture_response.lower() == pop_answer.lower():
        print("That's correct!")
    else:
        print("I'm sorry. That's incorrect.")
