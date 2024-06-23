import flet as ft


def main(page: ft.Page):

    page.title = "Say hello!"
    page.horizontal_alignment = "center"
    user_name = ft.TextField(label="Entrer votre nom", width=300)
    print_name_column = ft.Column()

    def call_hello(e):
        if not user_name.value:
            user_name.error_text = "Vous avez oublier de mettre votre nom"
            page.update()
        else:
            page.clean()
            print_name_column.controls.append(
                ft.Text(f"Hello {user_name.value}"))
            page.add(print_name_column)

    page.add(
        user_name,
        ft.ElevatedButton("Ici!!", on_click=call_hello),

    )


ft.app(main)
