import os

def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    num = input("Enter a number to check if it's a palindrome: ")

    pid = os.fork()

    if pid == 0:
        if is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
    else:
        os.wait()
