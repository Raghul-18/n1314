import os

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    return total == number

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's an Armstrong number: "))

    pid = os.fork()

    if pid == 0:
        if is_armstrong_number(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    else:
        os.wait()
