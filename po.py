import os

def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        pid = os.fork()
        
        if pid == 0:
            check_odd_even(number)
        elif pid > 0:
            os.wait()
        else:
            print("Failed to fork a new process.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
