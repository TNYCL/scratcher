import shutil
import os
import input


def duplicateFolder(project_name, author):
    pname = input.project_name
    src = "project_template"
    dest = "projects/" + pname
    behavior = dest + "/" + pname + " BP"
    resource = dest + "/" + pname + " RP"
    try:
        shutil.copytree(src, dest)
        os.rename(dest + "/BP", behavior)
        os.rename(dest + "/RP", resource)
    except FileExistsError as error:
        print("This project template already created.")


