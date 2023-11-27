import os

def calculate_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial of {num} is: {result}")

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))

    pid = os.fork()

    if pid == 0:
        calculate_factorial(number)
    else:
        os.wait()
