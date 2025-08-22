import numpy as np

questions = {"A. What is the name of USA current president?": "1. Trump, 2. Obama, 3. Hasina, 4. Clinton",
            "B. How many hours a day?": "1. 24 hours, 2. 20 hours, 3. 16 hours, 4. 21 hours",
            "C. In which age frontal lobe develops in human?": "1. 25 Years, 2. 18 Years, 3. 30 Years, 4. 40 Years",
            "D. What is the easiest programming language?": "1. Python, 2. Java, 3. C#, 4. GO",
            "E. What is the colour of sky?": "1. Blue, 2. Purple, 3. Red, 4. Yellow"}

answers = ["1", "1", "1", "1", "1"]

print("***********************")
print("Welcome to Trivia Game")
print("***********************")
print("Here are your questions")
print()

score_list = []

for i, (question, option) in enumerate(questions.items()):
    print(question)
    print(option)
    x = input(f"Insert Your answer (1/2/3/4): ")

    if x == answers[i]:
        print("✅ Correct!")
        score_list.append(1)
    else:
        print("❌ Wrong!\n")
        score_list.append(0)

total = np.sum(score_list)

print()
print("***********************")
print(f"Your total score is {total}/{len(questions)}")
print()
print("***********************")


print("Thank you for playing!")
