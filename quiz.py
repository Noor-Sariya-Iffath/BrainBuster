import requests
import random
import html

def fetch_questions(category=9, difficulty='easy', amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

def generate_quiz():
    questions = fetch_questions()
    score = 0

    print("Welcome to the Automatic Quiz! Type 'exit' at any time to end the quiz.")
    for item in questions:
        question = html.unescape(item["question"])
        print(question)
        options = item["incorrect_answers"] + [item["correct_answer"]]
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"{chr(97 + i)}) {option}")

        answer = input("Your answer: ").strip().lower()
        
        # Check if the user wants to exit the quiz
        if answer == 'exit':
            print("Thank you for playing! Your final score is:", score)
            return  # Exit the function to end the quiz

        correct_answer = item["correct_answer"].lower()
        if options[ord(answer) - 97].lower() == correct_answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")

    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    generate_quiz()
