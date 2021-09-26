import output

project_name = input("Project Name: ")
author = input("Author: ")

try:
    output.duplicatefolder(project_name, author)
except KeyError as error:
    print("Wrong template file values.")
