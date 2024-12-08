import os

import flet as ft

from archive import extract_archive, create_archive
from config import create_env
from models import welcome, filename, password, success, failed

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_NAME = 'security_model'


def main(page: ft.Page):
    page.title = "Архиватор"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 700

    def restart(e):
        page.clean()
        page.add(
            ft.Column(
                controls=[
                    welcome,
                    filename,
                    password,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Распокавать",
                                on_click=click_archive
                            ),
                            ft.ElevatedButton(text="Сжать", on_click=on_zip)
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    restart_button = ft.ElevatedButton(text="Еще раз", on_click=restart)

    def click_archive(e):
        page.clean()
        if extract_archive(filename.value, password.value):
            page.clean()
            page.add(
                success
            )

            data = {
                "APP_PATH": filename.value,
                "PASSWORD": password.value,
                "PLACE_APP": ".",
                "CONFIG_PATH": "../config.json",
                "DB_SCRIPTS": "./app/db/pull.sql"
            }

            create_env(data=data)
        else:
            page.clean()
            page.add(
                failed,
                restart_button
            )

    def on_zip(e):
        if create_archive(
            archive_name=os.path.join(BASE_DIR, ARCHIVE_NAME),
            password=password.value,
            files_to_archive=os.path.join(BASE_DIR, filename.value)
        ):
            page.clean()
            page.add(
                success,
                restart_button,
            )

        else:
            page.clean()
            page.add(
                failed,
                restart_button
            )

    start_page = ft.Column(
            controls=[
                welcome,
                filename,
                password,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Распокавать",
                            on_click=click_archive
                        ),
                        ft.ElevatedButton(text="Сжать", on_click=on_zip)
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    page.add(
        start_page
    )


if __name__ == "__main__":
    ft.app(target=main)
