import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import zipfile
import os
import json
import uuid


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
START_JSON = '../config.json'


def path_to_file(path: str) -> str:
    return os.path.join(BASE_DIR, path)


def get_uuid_device() -> str:
    mac_address = str(uuid.getnode())
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, mac_address))


def create_config(num: str):
    CONFIG_FILE = path_to_file(START_JSON)
    if not os.path.isfile(CONFIG_FILE):
        default_config = {
            "i": 0,
            "id_device": get_uuid_device(),
            "license_number": num
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_config, f)


def compress_with_password():
    choice = messagebox.askyesno(
        "Выбор",
        "Вы хотите выбрать папку для архивации?"
    )
    if choice:
        folder = filedialog.askdirectory(title="Выберите папку для архивации")
        if not folder:
            return
        files = []
        for root, _, filenames in os.walk(folder):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    else:
        files = filedialog.askopenfilenames(
            title="Выберите файлы для архивации"
        )
        if not files:
            return

    output_zip = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("ZIP файлы", "*.zip")],
        title="Сохранить ZIP архив как"
    )
    if not output_zip:
        return

    password = tk.simpledialog.askstring(
        "Введите пароль",
        "Введите пароль для архивации:",
        show="*"
    )
    if not password:
        messagebox.showwarning("Ошибка", "Пароль не введен")
        return

    try:
        with zipfile.ZipFile(output_zip, "w") as zipf:
            for file in files:
                arcname = os.path.relpath(file, os.path.dirname(folder))
                zipf.setpassword(password.encode("utf-8"))
                zipf.write(file, arcname)
        messagebox.showinfo("Успех", "Файлы успешно заархивированы с паролем!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при архивации: {e}")


def decompress_with_password():
    archive = filedialog.askopenfilename(
        filetypes=[("ZIP файлы", "*.zip")],
        title="Выберите ZIP архив для распаковки"
    )
    if not archive:
        return

    output_dir = filedialog.askdirectory(title="Выберите папку для распаковки")
    if not output_dir:
        return

    password = tk.simpledialog.askstring(
        "Введите пароль",
        "Введите пароль для распаковки архива:",
        show="*"
    )
    if not password:
        messagebox.showwarning("Ошибка", "Пароль не введен")
        return

    try:
        with zipfile.ZipFile(archive, "r") as zipf:
            zipf.extractall(path=output_dir, pwd=password.encode("utf-8"))
        messagebox.showinfo("Успех", "Файлы успешно распакованы!")
        create_config(password.encode("utf-8"))
    except RuntimeError:
        messagebox.showerror("Ошибка", "Неверный пароль")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при распаковке: {e}")


root = tk.Tk()
root.title("Архиватор с паролем")
root.geometry("400x250")


style = ttk.Style(root)
style.configure("TButton", font=("Arial", 12))


label_title = ttk.Label(root, text="Архиватор с паролем", font=("Arial", 16))
label_title.pack(pady=20)

button_compress = ttk.Button(
    root,
    text="Архивировать с паролем",
    command=compress_with_password
)

button_compress.pack(pady=10)

button_decompress = ttk.Button(
    root,
    text="Распаковать с паролем",
    command=decompress_with_password
)
button_decompress.pack(pady=10)


root.mainloop()
