import flet as ft

from app.config.settings import settings
from app.config.config import config
from app.auth.auth import authenticate_user, registry_user


def main(page: ft.Page):
    if not config.check_license_and_device_id(settings.get_device_id):
        page.clean()

    page.title = "Аутентификация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = ft.TextField(label="Имя пользователя")
    password = ft.TextField(
        label="Пароль",
        password=True,
        can_reveal_password=True
    )

    def login_click(e):
        if not username.value:
            username.error_text = "Пожалуйста, введите имя пользователя"
            page.update()
        elif not password.value:
            password.error_text = "Пожалуйста, введите пароль"
            page.update()
        elif authenticate_user(username.value, password.value):
            page.clean()
            page.add(ft.Text(f"Добро пожаловать, {username.value}!"))
        else:
            page.add(ft.Text("Неверный логин или пароль"))

    def register_click(e):
        page.clean()

    page.add(
        username,
        password,
        ft.ElevatedButton("Войти", on_click=login_click),
        ft.ElevatedButton("Зарегистрироваться", on_click=register_click),
    )


ft.app(target=main)
