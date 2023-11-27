import os

def generate_fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    print(f"Fibonacci series up to {n} terms: {fib_series}")

if __name__ == "__main__":
    terms = int(input("Enter the number of terms for the Fibonacci series: "))

    pid = os.fork()

    if pid == 0:
        generate_fibonacci(terms)
    else:
        os.wait()
