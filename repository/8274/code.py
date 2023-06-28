import time

def ask_question(question, choices, correct_choice):
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_choice = int(input("Enter your answer (1-4): "))
    if user_choice == correct_choice:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def play_quiz(quiz):
    score = 0
    for question in quiz:
        print("\n" + "=" * 20)
        print("Time remaining: 10 seconds")
        print("=" * 20 + "\n")
        if ask_question(question["question"], question["choices"], question["correct_choice"]):
            score += 1
        time.sleep(1)  # Simulating time for user to read feedback

    print("\nQuiz completed!")
    print("Final score:", score, "/", len(quiz))

quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Paris", "Berlin", "Madrid"],
        "correct_choice": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_choice": 1
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "correct_choice": 1
    }
    # Add more questions here
]

print("Welcome to the Interactive Quiz Game!")
print("Try to answer as many questions correctly as possible within the time limit.")
input("Press Enter to start the quiz...")

play_quiz(quiz)
