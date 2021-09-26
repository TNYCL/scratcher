from handler import output

def runtask():
    project_name = input("Project Name: ")
    author = input("Author: ")
    try:
        output.duplicatefolder(project_name, author)
    except KeyError as err:
        print(err)
        print("Wrong template file values.")
