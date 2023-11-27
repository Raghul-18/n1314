import os

def convert_case(input_str):
    upper_case_str = input_str.upper()
    lower_case_str = input_str.lower()

    print(f"Original String: {input_str}")
    print(f"Uppercase: {upper_case_str}")
    print(f"Lowercase: {lower_case_str}")

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    pid = os.fork()

    if pid == 0:
        convert_case(user_input)
    else:
        os.wait()
