import sys
import json


def count_questions(data: dict):
    question_count = 0
    for round_data in data["game"]["rounds"]:
        question_count += len(round_data["questions"])
    print(f"Total number of questions: {question_count}")


def print_right_answers(data: dict):
    correct_answers = []
    for round_data in data["game"]["rounds"]:
        for question in round_data["questions"]:
            correct_answers.append(question["correct_answer"])
    print(f"Correct answers: {correct_answers}")


def print_max_answer_time(data: dict):
    max_time = 0
    for round_data in data["game"]["rounds"]:
        for question in round_data["questions"]:
            max_time = max(max_time, question.get("time_to_answer", 0))
    print(f"Maximum answer time: {max_time}")


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 4.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
