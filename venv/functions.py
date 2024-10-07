# Throught the program we are using file todos.txt file so we are making this file as the default file.
def get_todos(filepath='todos.txt'):
    """ This function returns a list of all todo items from a text file. this is called doc string."""
    with open(filepath, 'r') as local_file:
        todos_local=local_file.readlines()
        return todos_local

def write_todos(todos_local,filepath='todos.txt'):
    """This function writes the list into the text file. we can print this doc
    string using print(help(write_todos)) """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_local)

#print(__name__)
if __name__ == '__main__':
    print('Hello')