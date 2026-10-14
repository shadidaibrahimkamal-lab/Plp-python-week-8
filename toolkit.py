import random


# Welcome message for the user before they choose a tool.
print("Welcome to the Personal Mini-Toolkit! Choose a tool to get started.")


# Number guessing tool: picks a hidden number and gives hints until the user guesses correctly.
def number_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("\nLet's play the number guessing game!")
    print("I am thinking of a number between 1 and 20.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Great job! You guessed the number in {attempts} attempts.")
            break


# To-do list tool: stores tasks in a list and allows the user to add or complete items.
def todo_list():
    tasks = []

    print("\nWelcome to your to-do list.")
    print("Type 'done' when you want to finish managing your list.")

    while True:
        action = input("Add a task or type 'done': ").strip()

        if action.lower() == "done":
            if not tasks:
                print("Your to-do list is empty right now.")
            else:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            break

        if action:
            tasks.append(action)
            print(f"Added: {action}")
        else:
            print("Please enter a task before continuing.")


# Calculator tool: performs simple arithmetic with user-selected numbers and operation.
def simple_calculator():
    print("\nSimple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("That operation is not supported.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")


# Name formatter tool: cleans up a name and displays it in a neat, friendly format.
def name_formatter():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if not first_name or not last_name:
        print("Please provide both names.")
        return

    formatted_name = f"{first_name.title()} {last_name.title()}"
    print(f"Your formatted name is: {formatted_name}")


# Main menu loop that keeps the toolkit running until the user chooses to quit.
def main():
    while True:
        print("\n=== Personal Mini-Toolkit ===")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thanks for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
