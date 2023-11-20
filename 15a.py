def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * m
    for i in range(m):
        for j in range(n):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print(" Process No. Process Size Block no.")
    for i in range(m):
        print(f" {i + 1}\t\t{processSize[i]}\t\t", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blocksize = [int(input(f"Enter the size of block {i + 1}: ")) for i in range(int(input("Enter the number of blocks: ")))]
    processSize = [int(input(f"Enter the size of process {i + 1}: ")) for i in range(int(input("Enter the number of processes: ")))]
    
    firstFit(blocksize, len(processSize), processSize, len(blocksize))
