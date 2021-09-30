from os import path
import os
import ssl
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

zip_url = "https://cdn.tnycl.com/scratcher/template.zip"
template_exist = path.exists(os.getcwd() + "/template")

def download(extract_to='./template'):
    if template_exist == False:
        print('Template folder not exist, downloading.')
        try:
            context = ssl._create_unverified_context()
            http_response = urlopen(zip_url, context=context)
            print('ZIP Exctracting...')
            zipfile = ZipFile(BytesIO(http_response.read()))
            zipfile.extractall(path=extract_to)
            print('Template folder successfully created.')
            return True
        except Exception as err:
            print(err)
            print('ERROR: in download() function. (Error #3)')
            exit()
    return True

