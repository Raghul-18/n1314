def fifo_page_replacement(frames, reference_string):
    page_faults = 0
    hits = 0
    page_table = []
    for page in reference_string:
        if page not in page_table:
            if len(page_table) < frames:
                page_table.append(page)
            else:
                page_table.pop(0)
                page_table.append(page)
                page_faults += 1
        else:
            hits += 1
        print(f"Frame Table: {page_table}")
    return page_faults, hits


def main():
    frames = int(input("Enter the number of frames: "))
    reference_string = list(map(int, input("Enter the reference string, space-separated: ").split()))
    page_faults, hits = fifo_page_replacement(frames, reference_string)
    total_references = len(reference_string)
    hit_ratio = hits / total_references
    fault_ratio = page_faults / total_references
    print(f"Total Page Faults using FIFO: {page_faults}")
    print(f"Total Hits using FIFO: {hits}")
    print(f"Hit Ratio: {hit_ratio:.2%}")
    print(f"Fault Ratio: {fault_ratio:.2%}")

if __name__ == "__main__":
    main()
