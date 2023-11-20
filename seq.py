class SequentialFileAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.blocks_occupied = [0] * total_blocks

    def allocate_file(self, file_name, file_size, block_size):
        # Calculate the number of blocks needed for the file
        num_blocks_needed = (file_size + block_size - 1) // block_size

        # Find consecutive blocks for the file
        start_block = -1
        consecutive_blocks = 0

        for i in range(self.total_blocks):
            if self.blocks_occupied[i] == 0:
                if consecutive_blocks == 0:
                    start_block = i
                consecutive_blocks += 1

                if consecutive_blocks == num_blocks_needed:
                    # Allocate blocks for the file
                    for j in range(start_block, start_block + num_blocks_needed):
                        self.blocks_occupied[j] = 1

                    print(f"File '{file_name}' allocated starting from block {start_block}")
                    return
            else:
                consecutive_blocks = 0

        print(f"Not enough consecutive blocks available for file '{file_name}'")

    def display_allocation(self):
        print("Block Allocation:")
        for i in range(self.total_blocks):
            print(f"Block {i}: {'Occupied' if self.blocks_occupied[i] == 1 else 'Free'}")


# Example usage with user input
total_blocks = int(input("Enter the total number of blocks: "))
block_size = int(input("Enter the size of each block: "))
file_allocation_system = SequentialFileAllocation(total_blocks)

file_allocation_system.allocate_file("File1", 3, block_size)
file_allocation_system.allocate_file("File2", 2, block_size)
file_allocation_system.allocate_file("File3", 7, block_size)
file_allocation_system.display_allocation()
