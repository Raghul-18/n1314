def get_input_matrix(rows, cols, prompt):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(prompt.format(i + 1)).split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def bankers_algorithm(m, n, alloc, maximum, avail):
    f = [0] * n
    ans = []
    need = [[maximum[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    for _ in range(n):
        for i in range(n):
            if f[i] == 0:
                if all(need[i][j] <= avail[j] for j in range(m)):
                    ans.append(i)
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    return ans

def main():
    m = int(input("Enter resource number: "))
    n = int(input("Enter number of processes: "))

    alloc_prompt = "Enter allocation matrix for process {}: "
    alloc = get_input_matrix(n, m, alloc_prompt)

    max_prompt = "Enter maximum matrix for process {}: "
    maximum = get_input_matrix(n, m, max_prompt)

    avail = list(map(int, input("Enter available resources: ").split()))

    safe_sequence = bankers_algorithm(m, n, alloc, maximum, avail)

    print("\nThe following is the need matrix:")
    print_matrix([[maximum[i][j] - alloc[i][j] for j in range(m)] for i in range(n)])

    print("\nFollowing is the SAFE Sequence:")
    print(" P", end="")
    for i in range(len(safe_sequence) - 1):
        print(safe_sequence[i], " -> P", sep="", end="")
    print(safe_sequence[-1])

if __name__ == "__main__":
    main()
