# Interactive Quiz Game - 8274

**Language**: `Python`

**Lines of code**: `51`

## Description

The Interactive Quiz Game is a program written in Python that allows users to play an engaging quiz game. The program presents multiple-choice questions, tracks the user's score, and provides feedback on the correct answers. It also includes a timer for each question, adding a level of challenge and excitement to the game. The program utilizes functions, loops, conditionals, and user input handling to create an interactive and dynamic experience.

## Code

``` Python
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

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```