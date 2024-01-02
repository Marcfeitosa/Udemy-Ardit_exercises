files = ["a.txt", "b.txt", "c.txt"]

for i in files:
    with open(i, 'r') as file:
        lines = file.readlines()
        for j in lines:
            print(j.strip())
