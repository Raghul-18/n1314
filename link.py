class Block:
    def __init__(self, block_number):
        self.block_number = block_number
        self.next_block = None

def allocate_file(blocks, block_size, file_name, file_size):
    required_blocks = (file_size + block_size - 1) // block_size  
    allocated_blocks = []
    for i in range(len(blocks)):
        if not blocks[i]: 
            start_block = i
            end_block = start_block + required_blocks - 1
            if end_block < len(blocks) and all(not blocks[j] for j in range(start_block, end_block + 1)):
                for j in range(start_block, end_block + 1):
                    blocks[j] = file_name
                    allocated_blocks.append(j)
                break
    return allocated_blocks

def display_allocation(blocks):
    for i, block in enumerate(blocks):
        if block:
            print(f"Block {i}: {block}")
        else:
            print(f"Block {i}: Free")

def main():
    total_blocks = int(input("Enter the total number of blocks: "))
    block_size = int(input("Enter the block size: "))
    # Initialize the list of blocks as None, indicating free blocks
    blocks = [None] * total_blocks
    while True:
        file_name = input("Enter the file name (or 'exit' to finish): ")
        if file_name.lower() == 'exit':
            break
        file_size = int(input(f"Enter the size of {file_name} in bytes: "))
        allocated_blocks = allocate_file(blocks, block_size, file_name, file_size)
        if allocated_blocks:
            print(f"Allocated {file_name} to blocks: {allocated_blocks}")
        else:
            print(f"Not enough space to allocate {file_name}")
    print("\nFile Allocation Table:")
    display_allocation(blocks)
    free_blocks = [i for i, block in enumerate(blocks) if not block]
    print("\nFree Blocks: ", free_blocks)

if __name__ == "__main__":
    main()
