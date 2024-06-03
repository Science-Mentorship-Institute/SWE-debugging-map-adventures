from exercise1 import main as e1
from exercise2 import main as e2
import sys

EXERCISES = [
    e1,
    e2,
]

def main():
    # Take exercise number as argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <exercise_number>")
        return
    else:
        exercise_number = int(sys.argv[1])
        if exercise_number < 1 or exercise_number > len(EXERCISES):
            print("Invalid exercise number")
            return
        EXERCISES[exercise_number - 1].main()


if __name__ == '__main__':
    main()
