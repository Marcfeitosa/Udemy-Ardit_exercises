def greet(message):
    new_message = message.capitalize()
    print("hey Hey")
    return new_message

user_entry = input("What greeting do you want? ")
greeting = greet(user_entry)

print(greeting)

print(len(greeting))