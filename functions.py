
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read the text file and return the
        list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    # default args must come after non default args.
    """ Write new to-do items in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return todos_arg


if __name__ == "__main__":
    print("Hello, from the functions library.")
