from util import uuid
import shutil
import os
import json
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
    except FileExistsError:
        print("This project template already have.")
        file.openfolder(dest)

def manifest():
    bp_manifest = behavior + "manifest.json"
    rp_manifest = resource + "manifest.json"
    with open(bp_manifest) as file:
        data = json.load(file)
        data["header"]["uuid"] = str(uuid.header)
        data["modules"][0]["uuid"] = str(uuid.modules1)
        data["dependencies"][0]["uuid"] = str(uuid.dependencies)
        data["metadata"]["authors"][0] = pauthor
        json.dump(data, open(bp_manifest, "w"), indent=4)
    with open(rp_manifest) as file:
        data = json.load(file)
        data["dependencies"][0]["uuid"] = str(uuid.header)
        data["modules"][0]["uuid"] = str(uuid.modules2)
        data["header"]["uuid"] = str(uuid.dependencies)
        data["metadata"]["authors"][0] = pauthor
        json.dump(data, open(rp_manifest, "w"), indent=4)
