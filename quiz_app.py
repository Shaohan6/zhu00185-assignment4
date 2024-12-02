# Import the quiz data from the quiz_data.py file
from quiz_data import quiz_data


def run_quiz():
    """
    Function to run the quiz.
    It iterates through each question, displays options, takes user input,
    and calculates the final score.
    """
    print("Welcome to the General Knowledge Quiz!")
    print("Answer the following questions by selecting the correct option number.\n")

    score = 0  # Initialize score

    # Loop through each question in the quiz data
    for index, question in enumerate(quiz_data):
        print(f"Question {index + 1}: {question['question']}")

        # Display the options with numbers for selection
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        # Get user input for the answer
        while True:
            try:
                user_choice = int(input("Enter your choice (1/2/3/4): "))
                if 1 <= user_choice <= len(question['options']):
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check if the answer is correct
        if question['options'][user_choice - 1] == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

    # Display the final score
    print(f"You completed the quiz! Your final score is: {score}/{len(quiz_data)}")


if __name__ == "__main__":
    # Run the quiz when the script is executed
    run_quiz()
