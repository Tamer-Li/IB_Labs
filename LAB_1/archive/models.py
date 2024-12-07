import flet as ft


welcome = ft.Text(value="Добро пожаловать в Архиватор", size=30, italic=True)

success = ft.Text(value="Успешно")
failed = ft.Text(value="Ошибка!\nПроверьте ENV файл")

filename = ft.TextField(label="Архив")
password = ft.TextField(
    label="Пароль",
    password=True,
    can_reveal_password=True
)
