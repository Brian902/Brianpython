
questions = (
            "What year did pluto got cut-out as a planet?: ",
            "Which color is considered to have all the colors in the world?: ",
            "Who became the first ever man to solve quantum physics?: ",
            "Who among the answers is not an avenger?: ",
            "How many pounds does Thor's hammer weigh?: "
)

options = (
          ("A.2009", "B.2005", "C2024.", "D.2011"),
          ("A.Blue", "B.Pink", "C.Yellow", "D.White"),
          ("A.Adam", "B.Aquis", "C.Apollo", "D.Elon Musk"),
          ("A.Superman", "B.Batman", "C.Flash", "D.John Wick"),
          ("A.19", "B.41", "C.30", "D.20")
)

answers =("A", "B", "D", "B", "C")

assert len(questions) == len(options) == len(answers), "lengths of questions, options, and answers must be the same."
guesses = []

score = 0
question_num = 0

print("Welcome to the Quiz app")
print("Answer each question by entering A, B, C, or D.")

for question_num, question in enumerate(questions):
    print("\n-------------")
    print(f"Question{question_num}:{question}")
            
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter(A,B,C,D):").upper()
                
        if guess not in ['A', 'B', 'C', 'D']:
            print("\n**********")
            print("Invalid choice. Please enter A, B, C, OR D. Try again.")
        else:
            break
        
        
    guesses.append(guess)
            
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1

print("-------------")
print("---RESULTS----")
print("-------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:  {score}%")
