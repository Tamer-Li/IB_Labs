import tkinter as tk
from tkinter import ttk, messagebox

from db.db import pull, DB_PATH
from config.config import check_license_and_device_id, get_uuid_device
from auth.auth import register, auth_user


def authenticate_user(login, password):
    if auth_user(
        login,
        password,
        DB_PATH
    ):
        messagebox.showinfo("Успех", "Авторизация успешна!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")


def register_user(
        first_name,
        second_name,
        middle_name,
        login, email,
        phone,
        password
):
    address_registry = get_uuid_device()
    if register(
            first_name,
            second_name,
            middle_name,
            login, email,
            phone,
            password,
            address_registry,
            DB_PATH
    ):
        messagebox.showinfo("Успех", "Пользователь успешно зарегистрирован!")
    else:
        messagebox.showerror(
            "Ошибка",
            "Пользователь с таким логином или email уже существует."
        )


def registration_tab(tab):
    ttk.Label(tab, text="Имя:").grid(row=0, column=0, padx=10, pady=5)
    first_name_entry = ttk.Entry(tab)
    first_name_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Фамилия:").grid(row=1, column=0, padx=10, pady=5)
    second_name_entry = ttk.Entry(tab)
    second_name_entry.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Отчество:").grid(row=2, column=0, padx=10, pady=5)
    middle_name_entry = ttk.Entry(tab)
    middle_name_entry.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Логин:").grid(row=3, column=0, padx=10, pady=5)
    login_entry = ttk.Entry(tab)
    login_entry.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Email:").grid(row=4, column=0, padx=10, pady=5)
    email_entry = ttk.Entry(tab)
    email_entry.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Телефон:").grid(row=5, column=0, padx=10, pady=5)
    phone_entry = ttk.Entry(tab)
    phone_entry.grid(row=5, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Пароль:").grid(row=6, column=0, padx=10, pady=5)
    password_entry = ttk.Entry(tab, show="*")
    password_entry.grid(row=6, column=1, padx=10, pady=5)

    ttk.Button(tab, text="Зарегистрироваться", command=lambda: register_user(
        first_name_entry.get(),
        second_name_entry.get(),
        middle_name_entry.get(),
        login_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        password_entry.get(),
    )).grid(row=8, column=0, columnspan=2, pady=10)


def authentication_tab(tab):
    ttk.Label(tab, text="Логин:").grid(row=0, column=0, padx=10, pady=5)
    login_entry = ttk.Entry(tab)
    login_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(tab, text="Пароль:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = ttk.Entry(tab, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(tab, text="Войти", command=lambda: authenticate_user(
        login_entry.get(),
        password_entry.get()
    )).grid(row=2, column=0, columnspan=2, pady=10)


def main():
    chekc = check_license_and_device_id(get_uuid_device())
    if chekc is None:
        messagebox.showerror("Ошибка", "Файл config.json не найден.")
    elif chekc is False:
        messagebox.showerror(
            "Отказ",
            "Доступ запрещен. Проверьте лицензию и UUID устройства."
        )
        return
    pull()

    root = tk.Tk()
    root.title("Регистрация и аутентификация")
    root.geometry("400x400")

    tab_control = ttk.Notebook(root)

    registration_tab_frame = ttk.Frame(tab_control)
    authentication_tab_frame = ttk.Frame(tab_control)

    tab_control.add(registration_tab_frame, text="Регистрация")
    tab_control.add(authentication_tab_frame, text="Аутентификация")

    tab_control.pack(expand=1, fill="both")

    registration_tab(registration_tab_frame)
    authentication_tab(authentication_tab_frame)

    root.mainloop()


if __name__ == "__main__":
    main()
