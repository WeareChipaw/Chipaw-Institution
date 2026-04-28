try:
    with open("Shaolin.txt", "x") as foyl:
        print("File Created succesfully!")
except:
    print("File already exist")

with open("Shaolin.txt", "w") as foyl:
    foyl.write("Wassap mga ka wonders!")

with open("Shaolin.txt", "a") as foyl:
    foyl.write("\nDon't go there, mannnn.")

with open("Shaolin.txt", "r") as foyl:
    lines = foyl.readlines()
    print(lines)





