import os

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

if __name__ == "__main__":
    num = int(input("Enter a number to check if it's even or odd: "))

    pid = os.fork()

    if pid == 0:
        check_even_odd(num)
    else:
        os.wait()
