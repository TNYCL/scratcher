import shutil
import os
import json

pname = ""
pauthor = ""

def duplicateFolder(project_name, author="TNYCL"):
    global pauthor
    global behavior
    global resource
    global dest

    pname = project_name
    pauthor = author
    src = "project_template"
    dest = os.getcwd() + "/projects/" + pname
    behavior = dest + "/" + pname + " BP"
    resource = dest + "/" + pname + " RP"

    try:
        shutil.copytree(src, dest)
        os.rename(dest + "/BP", behavior)
        os.rename(dest + "/RP", resource)
        manifest()
    except FileExistsError as error:
        print("This project template already created.")

def manifest():
    
