FILEPATH = "Files/todo.txt"


def get_todos(filename=FILEPATH):
    """Read a text file and return a list of to-do items."""
    with open(filename, 'r') as file_local:
        todos1 = file_local.readlines()
    return todos1


def write_todos(list1, filename=FILEPATH):
    """Open a text file and write a list of to-do items."""
    with open(filename, 'w') as file:
        file.writelines(list1)


if __name__ == "__main__":
    print(get_todos())