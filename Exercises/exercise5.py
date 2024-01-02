member = input("Add a new member: ")

file = open(f"../files/subfiles/members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")
with open(f"../files/subfiles/members.txt", "w") as file:
    file.writelines(existing_members)
print(existing_members)
