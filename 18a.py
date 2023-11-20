files = {}

while True:
    print("\n\n1.Create File\n2.Delete File\n3.Search File \n4.Display Files\n5.Display file content\n6.Exit")
    ch = int(input("Enter your choice:"))
    
    if ch == 1:
        fname = input("\nEnter the name of the file:")
        content = input("Enter file contents:")
        files[fname] = content
    elif ch == 2:
        f = input("\nEnter the name of the file:")
        if f in files:
            del files[f]
            print("File", f, "found and deleted")
        else:
            print("File", f, "not found")
    elif ch == 3:
        f = input("\nEnter the name of the file:")
        if f in files:
            print("File", f, "found")
        else:
            print("File", f, "not found")
    elif ch == 4:
        if len(files) == 0:
            print("\nDirectory Empty")
        else:
            print("\nThe Files are:")
            for i in files:
                print(i, end="\n")
    elif ch == 5:
        f = input("\nEnter the name of the file:")
        if f in files:
            print("Content:")
            print(files[f])
        else:
            print("File not found")
    elif ch == 6:
        break
    else:
        print("Invalid option!!")
