def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        wstIdx = -1

        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j

        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]

    print("Process No. Process Size Block no.")
    for i in range(n):
        print(f"{i + 1}\t\t{processSize[i]}\t\t", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blocksize = [int(input(f"Enter the size of block {i + 1}: ")) for i in range(int(input("Enter the number of blocks: ")))]
    processSize = [int(input(f"Enter the size of process {i + 1}: ")) for i in range(int(input("Enter the number of processes: ")))]
    
    worstFit(blocksize, len(blocksize), processSize, len(processSize))
