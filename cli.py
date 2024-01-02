#from functions import get_todos, write_todos
from modules import functions
import time



now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            #striping the "\n" without any method
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("to complete an item you should type it's index.")
            continue

    elif user_action.startswith("exit"):
        print(f"Pending items:")
        for index, item in enumerate(todos):
            #striping the "\n" without any method
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
        break
    else:
        print('Comand is not valid')

print("Bye")

