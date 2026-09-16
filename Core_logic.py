import random
import time


PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog while the sun sets slowly behind the mountains.",
    "Practice makes a person better every single day, one small step after another toward mastery.",
    "Technology keeps changing how people work, learn, communicate, and connect across the whole world.",
    "A calm mind and steady hands are the real secrets behind fast and accurate typing skills.",
    "Success is not an accident, it is built through consistent effort, patience, and daily discipline.",
    "Reading widely and typing regularly both help sharpen the brain and improve overall focus.",
    "Every expert was once a beginner who simply refused to give up after early mistakes.",
    "Good habits are hard to build but easy to live with once they finally take hold.",
]


def get_random_paragraph():
    return random.choice(PARAGRAPHS)


def calculate_accuracy(target, typed):
    correct = 0

    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct += 1

    if len(typed) == 0:
        return 100

    accuracy = int((correct / len(typed)) * 100)

    return accuracy


def calculate_wpm(typed, elapsed_time):
    if elapsed_time <= 0:
        return 0

    words = len(typed.split())

    wpm = int((words / elapsed_time) * 60)

    return wpm


def calculate_result(target, typed, elapsed_time):

    accuracy = calculate_accuracy(target, typed)

    wpm = calculate_wpm(typed, elapsed_time)

    return wpm, accuracy