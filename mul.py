import multiprocessing

def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(digit) ** order for digit in str(num))

def check_armstrong_parallel(num):
    return num, is_armstrong(num)

if __name__ == "__main__":
    num_to_check = 153
    num_processes = 4

    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(check_armstrong_parallel, range(num_to_check, num_to_check + num_processes))
    pool.close()
    pool.join()

    for num, is_armstrong_num in results:
        print(f"{num} is Armstrong: {is_armstrong_num}")
