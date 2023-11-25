import os
def dir_project():

    print(os.getcwd())

def dir_libdir():

    print(os.path.dirname(__file__))


def dir_filedir(file):
    print(os.path.dirname(file))