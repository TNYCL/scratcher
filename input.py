import tkinter as tk
from tkinter import filedialog
import output
import json

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

print("File successfully selected, converting.")

try:
    data = json.load(open(file_path))
    project_name = data["name"]
    author = data["author"]
    output.duplicate(project_name, author)
except KeyError as error:
    print("Wrong template file values.")
