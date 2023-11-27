import os

def sort_numbers(numbers):
    numbers.sort()
    print(f"Sorted numbers: {numbers}")

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    numbers = []

    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    pid = os.fork()

    if pid == 0:
        sort_numbers(numbers)
    else:
        os.wait()
