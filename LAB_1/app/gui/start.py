import flet as ft

from app.config.settings import settings
from app.config.config import config


def main(page: ft.Page):
    if not config.check_license_and_device_id(settings.get_device_id):
        return 

    page.title = "Аутентификация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username = ft.TextField(label="Имя пользователя")
    password = ft.TextField(label="Пароль", password=True, can_reveal_password=True)

    def login_click(e):
        if not username.value:
            username.error_text = "Пожалуйста, введите имя пользователя"
            page.update()
        elif not password.value:
            password.error_text = "Пожалуйста, введите пароль"
            page.update()
        elif check_user(username.value, password.value):
            page.clean()
            page.add(ft.Text(f"Добро пожаловать, {username.value}!"))
        else:
            page.add(ft.Text("Неверный логин или пароль"))

    def register_click(e):
        if not username.value:
            username.error_text = "Пожалуйста, введите имя пользователя"
            page.update()
        elif not password.value:
            password.error_text = "Пожалуйста, введите пароль"
            page.update()
        else:
            add_user(username.value, password.value)
            page.clean()
            page.add(ft.Text(f"Пользователь {username.value} зарегистрирован!"))

    page.add(
        username,
        password,
        ft.ElevatedButton("Войти", on_click=login_click),
        ft.ElevatedButton("Зарегистрироваться", on_click=register_click),
    )


ft.app(target=main)
