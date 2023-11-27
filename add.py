import os

def add_two_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    num1 = float(input("Enter the first real number: "))
    num2 = float(input("Enter the second real number: "))

    pid = os.fork()

    if pid == 0:
        add_two_numbers(num1, num2)
    else:
        os.wait()
