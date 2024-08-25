# Define the quiz data
quiz_data = {
    "What is the capital of France?": {
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    "What is 2 + 2?": {
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C"
    }
}

def run_quiz(quiz):
    score = 0
    total_questions = len(quiz)

    for question, data in quiz.items():
        print(question)
        for option in data["options"]:
            print(option)

        # Get the user's answer
        user_answer = input("Choose the correct option (A, B, C, D): ").upper()

        # Check the answer
        if user_answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {data['answer']}.\n")

    # Print the final score
    print(f"Your final score is {score} out of {total_questions}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz(quiz_data)