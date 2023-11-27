import os

def print_file_with_line_count(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

        print(f"File: {filename}")
        print(f"Line count: {line_count}\n")

        for line_number, line in enumerate(lines, start=1):
            print(f"Line {line_number}: {line.strip()}")

if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")

    pid = os.fork()

    if pid == 0:
        print_file_with_line_count(file_name)
    else:
        os.wait()
