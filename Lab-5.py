import tkinter as tk
from github import Github
import os

def get_repo_info():
    repo_name = repo_entry.get()
    g = Github()
    repo = g.get_repo(repo_name)
    repo_owner = repo.owner
    with open("repo_info.txt", "w") as f:
        f.write("Name: " + repo.name + "\n")
        f.write("Description: " + repo.description + "\n")
        f.write("Language: " + repo.language + "\n")
        f.write("URL: " + repo.html_url + "\n")
        f.write("Company: " + str(repo_owner.company) + "\n")
        f.write("Created at: " + str(repo_owner.created_at) + "\n")
        f.write("Email: " + str(repo_owner.email) + "\n")
        f.write("ID: " + str(repo_owner.id) + "\n")
        f.write("Name: " + repo_owner.name + "\n")
        f.write("URL: " + repo_owner.url + "\n")

root = tk.Tk()
root.title("Информация о репозитории Github")

repo_label = tk.Label(root, text="Введите имя репозитория:")
repo_label.pack()

repo_entry = tk.Entry(root)
repo_entry.pack()

get_info_button = tk.Button(root, text="Получить информацию", command=get_repo_info)
get_info_button.pack()

root.mainloop()
