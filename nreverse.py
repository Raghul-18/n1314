import os

def print_reverse_order(number):
    reversed_number = int(str(number)[::-1])
    print(f"Number in reverse order: {reversed_number}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    pid = os.fork()

    if pid == 0:
        print_reverse_order(num)
    else:
        os.wait()
