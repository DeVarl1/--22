# -- coding: utf-8 --
import os
from github import Github
import tkinter as tk
from tkinter import filedialog

def get_repo_info():
    repo_name = entry.get()
    g = Github()
    repo = g.get_repo(repo_name)
    repo_owner = repo.owner
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"),("All Files", "*.*")])
   
    with open(filepath, "w") as f:
        f.write("Company: " + str(repo_owner.company) + "\n")
        f.write("Created at: " + str(repo_owner.created_at) + "\n")
        f.write("Email: " + str(repo_owner.email) + "\n")
        f.write("ID: " + str(repo_owner.id) + "\n")
        f.write("Name: " + repo.name + "\n")
        f.write("URL: " + repo.html_url + "\n")
        if repo_owner.name is not None:
            f.write("Name: " + repo_owner.name + "\n")
        else:
            f.write("Name: N/A\n")
        f.write("URL: " + repo_owner.url + "\n")
    print("Информация о репозитории сохранена.")

root = tk.Tk()
root.title("Информация о репозитории Github")

label = tk.Label(root, text="Введите имя репозитория Github в формате автор/имя (например facebook/react):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Сохранить информацию о репозитории", command=get_repo_info)
button.pack()

root.mainloop()