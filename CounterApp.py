import flet as ft


def main(page: ft.page):
    page.title = "Icon Button"
    page.theme_mode = "light"
    text_number = ft.TextField(value="0", text_align="center", width=100)
    page.vertical_alignment = "center"

    def plus_click(e):
        text_number.value = int(text_number.value)+1
        page.update()

    def moins_click(e):
        text_number.value = int(text_number.value)-1
        page.update()
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=moins_click),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment="center"
        )
    )


ft.app(target=main)
