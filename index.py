class IndexedFileAllocation:
    def __init__(self, total_blocks, block_size):
        self.total_blocks = total_blocks
        self.block_size = block_size
        self.blocks = [None] * total_blocks
        self.file_allocation_table = {}

    def allocate_file(self, file_name, file_size):
        if file_name in self.file_allocation_table:
            print(f"Error: File '{file_name}' already exists.")
            return

        # Find free blocks for the index table and data blocks
        index_block = self._find_free_block(1)
        data_blocks = self._find_free_block(file_size)

        if index_block is not None and data_blocks is not None:
            # Allocate the file in the file allocation table
            self.file_allocation_table[file_name] = (index_block, data_blocks)

            # Update the blocks to mark them as allocated
            self.blocks[index_block[0]] = file_name
            for block in data_blocks:
                self.blocks[block] = file_name

            print(f"Allocated {file_name} to blocks: {data_blocks}")

        else:
            print(f"Not enough space to allocate {file_name}")

    def deallocate_file(self, file_name):
        if file_name not in self.file_allocation_table:
            print(f"Error: File '{file_name}' not found.")
            return

        # Free the blocks allocated to the file
        index_block, data_blocks = self.file_allocation_table[file_name]
        self.blocks[index_block[0]] = None
        for block in data_blocks:
            self.blocks[block] = None

        # Remove the file from the file allocation table
        del self.file_allocation_table[file_name]
        print(f"Deallocated {file_name}")

    def display_allocation(self):
        print("\nFile Allocation Table:")
        for file_name, (index_block, data_blocks) in self.file_allocation_table.items():
            print(f"File: {file_name}, Index Block: {index_block}, Data Blocks: {data_blocks}")

        print("\nBlock Status:")
        for i, block in enumerate(self.blocks):
            if block is not None:
                print(f"Block {i}: {block}")
            else:
                print(f"Block {i}: Free")

    def _find_free_block(self, required_blocks=1):
        free_blocks = [i for i in range(self.total_blocks) if self.blocks[i] is None]

        if len(free_blocks) >= required_blocks:
            return free_blocks[:required_blocks]
        else:
            return None


def main():
    total_blocks = int(input("Enter the total number of blocks: "))
    block_size = int(input("Enter the size of each block: "))
    file_system = IndexedFileAllocation(total_blocks, block_size)

    while True:
        print("\n1. Allocate File\n2. Deallocate File\n3. Display Allocation\n4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            file_name = input("Enter the file name: ")
            file_size = int(input("Enter the size of the file (in blocks): "))
            file_system.allocate_file(file_name, file_size)

        elif choice == 2:
            file_name = input("Enter the file name to deallocate: ")
            file_system.deallocate_file(file_name)

        elif choice == 3:
            file_system.display_allocation()

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
