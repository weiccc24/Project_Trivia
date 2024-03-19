#trivia game for nucamp project 1

#A tuple to store my questions, there are 10 questions for now
questions = ("Where was tea invented?: ", 
             "About what percentage of the adult human body is made of water?: ", 
             "The world's first successful vaccine was developed to treat which disease?: ",
             "What spirit is used in making a Tom Collins?: ",
             "Which of the following languages has the longest alphabet?: ",
             "Which city is home to the Brandenburg Gate?: ",
             "The speed of a computer mouse is measured in what units?: ",
             "How can you tell the age of a horse?: ",
             "In 2022, what was the most profitable company in the world?",
             "How many miles is a full marathon?")

#4 options to each of the question
options = (("A. England", "B. USA", "C. India", "D. China"),
           ("A. 10%", "B. 50%", "C. 60%", "D. 90%"),
           ("A. Smallpox", "B. Hepatitis A", "C. Influenza", "D. HPV"),
           ("A. Vodka", "B. Rum", "C. Gin", "D. Whisky"),
           ("A. Russian", "B. Greek", "C. Arabic", "D. Spain"),
           ("A. Vienna", "B. Zurich", "C. Paris", "D. Berlin"),
           ("A. Inches", "B. Centimeters", "C. Mickeys", "D. Paws"),
           ("A. The length of its tail", "B. The quality of its hooves", "C. The clarity in its eyes", "D. The line on its teeth"),
           ("A. Apple", "B. Boeing", "C. Microsoft", "D. Amazon"),
           ("A. 13.1", "B. 20", "C. 26.2", "D. 42"))

answer_list = ("D", "C", "A", "C", "A", "D", "C", "D", "A", "C")
question_index = 0
player_guesses = []
score = 0

#print out question and options for the question
for question in questions:
    print("\n" + question)
    for option in options[question_index]:
        print(option)
    while True:
        player_guess = input("Enter your guess (A, B, C, D): ").upper()
        if player_guess in set("ABCD"):
            player_guesses.append(player_guess)
            break
        else:
            print("Enter only 'A', 'B', 'C' or 'D': ")
    
#prompt user for their guess and check whether the guess is the correct answer
    # player_guess = input("Enter your guess (A, B, C, D): ").upper()
    # player_guesses.append(player_guess)
    if player_guess == answer_list[question_index]:
        score += 100
        print("Correct!")

    else:
        print("Sorry that was incorrect...")
        print("The correct answer is", answer_list[question_index])

    print("Your current score is", score)
    question_index += 1

print("\nYou have answered all the questions.")
print("Your final score is", score)
