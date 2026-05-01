import os
os.system("cls")

while True:
    print("--- ANG DIARY NG PANGET ---\n")
    print("1. Create")
    print("2. Append")
    print("3. Read")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter numbers only")
        continue
    match choice:
        case 1:
            try:
                filename = input("Enter the filename (example: test.txt): ")
                with open(filename, "x") as file:
                    texts = input("Write contents: ")
                    file.write(texts)
                print("File Created successfully")
            except:
                print("File already exists")
        case 2:
            try:
                filename = input("Enter the filename you want to append to: ")
                if not os.path.exists(filename):
                    print("ANG FILE DOL DILI GA EXIST. PLEASE HIMO SAG FILE UNA.")
                else:
                    with open(filename, "a") as file:
                        contents = input("Write contents: ")
                        file.write(contents)
                    print("Added contents successfully!")
            except:
                print("DILI GA EXIST ANG FILE OY...")
        case 3:
                with open(filename, "r") as file:
                    contents = file.readlines()
                    print("\n",contents)
        case 4:
            with open(filename, "r") as file:   
                pass
        case 5:
            print("Delete")
        case 6:
            print("Exiting....")
            break
        case _:
            print("Please choose 1-6.")
