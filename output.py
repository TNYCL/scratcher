from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
from util import uuid
import shutil
import os
import json
import codecs
from util import file

def duplicatefolder(project_name, author="TNYCL"):
    global pname
    global pauthor
    global behavior
    global resource
    global dest
    pname = project_name
    pauthor = author
    src = "project_template"
    dest = os.getcwd() + "/projects/" + pname + "/"
    behavior = dest + pname + " BP/"
    resource = dest + pname + " RP/"
    try:
        shutil.copytree(src, dest)
        os.rename(dest + "/BP", behavior)
        os.rename(dest + "/RP", resource)
        manifest()
        text()
    except FileExistsError:
        print("This project template already have.")
        file.openfolder(dest)

def manifest():
    try:
        bp = behavior + "manifest.json"
        rp = resource + "manifest.json"
        with open(bp) as file:
            data = json.load(file)
            data["header"]["uuid"] = str(uuid.header)
            data["modules"][0]["uuid"] = str(uuid.modules1)
            data["dependencies"][0]["uuid"] = str(uuid.dependencies)
            data["metadata"]["authors"][0] = pauthor
            json.dump(data, open(bp, "w"), indent=4)
        with open(rp) as file:
            data = json.load(file)
            data["dependencies"][0]["uuid"] = str(uuid.header)
            data["modules"][0]["uuid"] = str(uuid.modules2)
            data["header"]["uuid"] = str(uuid.dependencies)
            data["metadata"]["authors"][0] = pauthor
            json.dump(data, open(rp, "w"), indent=4)
    except JSONEncoder and Exception as error:
        print('ERROR: in manifest() function. (Error #1)')

def text():
    try:
        bp = behavior + "texts/en_US.lang"
        rp = resource + "texts/en_US.lang"
        with codecs.open(bp, "a", "utf-8") as file:
            data = file
            data.write("pack.name=§e{} BP\n".format(pname))
            data.write("pack.description=§6by {}\n".format(pauthor))
            data.close()
        with codecs.open(rp, "r", "utf-8") as file:
            data = file.readlines()
            data[0] = "pack.name=§e{} RP\n".format(pname)
            data[1] = "pack.description=§6by {}\n".format(pauthor)
            edited_files = codecs.open(rp, 'w', 'utf-8')
            edited_files.writelines(data)
            edited_files.close()
    except Exception:
        print('ERROR: in text() function. (Error #2)')
        
        
