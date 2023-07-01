import functions
import time

todos = []
now = time.strftime("%Y-%b-%d %a %H:%M:%S")
print(f"date: {now}")
while True:

    user_action = input("Enter add, edit, show , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todos = functions.get_todos()

        todo = user_action[4:]
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('edit'):
        try:

            todos = functions.get_todos()
            index = int(user_action[5:]) - 1
            todos[index] = input("enter updated task: ") + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("not a valid action.")
            continue

    elif user_action.startswith('complete'):

        try:

            todos = functions.get_todos()
            index = int(user_action[8:])
            index = index - 1

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from todo list"
            print(message)
        except IndexError:
            print("index out of range.")
            continue
        except ValueError:
            print("not a valid action.")
            continue

    elif user_action.startswith('show'):

        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")
print("bye")




