try:
    with open("Shaolin.txt", "x") as foyl:
        print("File Created succesfully!")
except:
    print("File already exist")

with open("Shaolin.txt", "w") as foyl:
    foyl.write("Wassap mga ka wonders!")
