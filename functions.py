FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """read text from a file and return the list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """take a list as an input and a file path then put list content to the file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
