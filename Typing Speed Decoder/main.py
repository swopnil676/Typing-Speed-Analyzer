import time

from Core_logic import (
    get_random_paragraph,
    calculate_result
)


def main():

    print("=" * 60)
    print("              TYPING SPEED TEST")
    print("=" * 60)

    # Get random paragraph
    target = get_random_paragraph()

    print("\nType the following paragraph:\n")
    print(target)

    print("\nStart typing!")

    # Start timer
    start_time = time.time()

    # Get user input
    typed = input("\n> ")

    # Stop timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Calculate WPM and accuracy
    wpm, accuracy = calculate_result(
        target,
        typed,
        elapsed_time
    )

    # Display result
    print("\n" + "=" * 60)
    print("                    RESULT")
    print("=" * 60)

    print(f"Time Taken : {elapsed_time:.2f} seconds")
    print(f"WPM        : {wpm}")
    print(f"Accuracy   : {accuracy}%")

    print("=" * 60)


if __name__ == "__main__":
    main()