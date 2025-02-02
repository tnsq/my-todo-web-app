FILEPATH="todos.txt"


import os

# def read_todos():
#     # Get the directory where functions.py is located
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     filepath = os.path.join(base_dir, 'todos.txt')
#
#     with open(filepath, 'r') as file:
#         return file.readlines()
def read_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
        todos_read=file.readlines()

    return todos_read # just changed name so that confusion na ho with main todos


def write_todos(todos_arg, filepath=FILEPATH):# yahan order dhyaan rakhna argument jiska default parameter nhi hai vo phele ayega yahan filepath k pass toh hai default parameter toh vo baad mein aayega 
    with open(filepath,'w') as file:
        file.writelines(todos_arg)  