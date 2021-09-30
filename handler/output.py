from util import uuid
import shutil
import os
import json
import codecs
from util import file

def runoutput():
    manifest()
    text()
    installer()

def duplicatefolder(project_name, author="TNYCL"):
    global pname
    global pauthor
    global behavior
    global resource
    global dest
    pname = project_name
    pauthor = author
    src = "template"
    dest = os.getcwd() + "/projects/" + pname + "/"
    behavior = dest + pname + " BP/"
    resource = dest + pname + " RP/"
    try:
        shutil.copytree(src, dest)
        os.rename(dest + "/BP", behavior)
        os.rename(dest + "/RP", resource)
        runoutput()
    except FileExistsError:
        print("This project template already have.")
        file.openfolder(dest)
        exit()


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
    except Exception as err:
        print(err)
        print("ERROR: in manifest() function. (Error #1)")
        exit()


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
            edited_files = codecs.open(rp, "w", "utf-8")
            edited_files.writelines(data)
            edited_files.close()
    except Exception as err:
        print(err)
        print("ERROR: in text() function. (Error #2)")
        exit()

def installer():
    try:
        installer = dest + 'install.bat'
        with codecs.open(installer, "a", "utf-8") as file:
            data = file
            data.write('@echo off\n')
            data.write('title\n')
            data.write('cls\n')
            data.write('echo A | xcopy "%CD%\{} BP" "%UserProfile%\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\{} BP" /s /e /I\n'.format(pname, pname))
            data.write('echo A | xcopy "%CD%\{} RP" "%UserProfile%\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_resource_packs\{} RP" /s /e /I\n'.format(pname, pname))
            data.write('cls\n')
            data.write('echo Install completed.\n')
            data.write('PAUSE')
    except Exception as err:
        print(err)
        print('ERROR: in installer() function. (Error #4)')
        exit()
