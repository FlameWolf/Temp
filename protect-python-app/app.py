def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python program.")

def add_numbers(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    greet_user(name)

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

main()