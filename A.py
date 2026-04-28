while True:
    print("1. Create")
    print("2. Append")
    print("3. Read")
    print("4. Update")
    print("5. Delete")
    print("6. Exit)
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter numbers only")

    match choice:
        case 1:
            try:
                filename = input("Enter the filename (example: test.txt): ")
                with open(filename, "x") as file:
                    texts = input("Write contents: ")
                    file.write(texts)
                print("File Created succesfully")
            except:
                print("File already exist")
        case 2:
            with open (filename, "a") as file:
                contents = input("Write contents: ")
                file.write(contents)
            print("Added contents successfuly!")
        case 3:
             with open(filename, "r") as file:
                contents = file.readlines()
                print("\n",contents)
        case 4:
            with open(filename, "r") as file:
                
        case 5:
            print("Delete")
        case 6:
            break





