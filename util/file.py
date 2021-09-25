import tkinter as tk
import shutil
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

data = json.load(open(file_path))

project_name = data['name']
project_desc = data['desc']
author = data['author']