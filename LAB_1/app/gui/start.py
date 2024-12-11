import flet as ft

from app.config.settings import settings
from app.config.config import config
from app.auth.auth import authenticate_user, registry_user
from app.db.dao import IdPcDAO

IdPcDAO.add(settings.get_device_id)

username = ft.TextField(label="Имя пользователя", width=300)
login = ft.TextField(label="Логин", width=300)
email = ft.TextField(label="Email", width=300)
password = ft.TextField(
    label="Пароль",
    password=True,
    can_reveal_password=True,
    width=300
)
confirm_password = ft.TextField(
    label="Подтвердите пароль",
    password=True,
    can_reveal_password=True,
    width=300
)


registry_page = ft.Column(
    controls=[
        ft.Text("Регистрация", size=30),
        username,
        login,
        email,
        password,
        confirm_password
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
)

error_message = ft.Text(color=ft.colors.RED, visible=False)


def main(page: ft.Page):
    if not config.check_license_and_device_id(settings.get_device_id):
        page.clean()

    page.title = "Аутентификация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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

    def register_in_model(e):
        id_device = IdPcDAO.find_by_address(settings.get_device_id)
        if id_device is None:
            error_message.visible = True
            return

        if registry_user(
            login.value,
            username.value,
            password.value,
            email.value,
            id_device
        ) is None:
            error_message.visible = True

        error_message.visible = False
        page.clean()
        page.add(
            ft.Text("Регистрация успешна!", size=20)
        )
        page.update()

    def register_click(e):
        page.clean()
        page.add(
            registry_page,
            ft.ElevatedButton("Регистрация", on_click=register_in_model)
        )

    page.add(
        username,
        password,
        ft.ElevatedButton("Войти", on_click=login_click),
        ft.ElevatedButton("Зарегистрироваться", on_click=register_click),
    )


ft.app(target=main)
