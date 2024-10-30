from flet_multi_page import *
import flet as ft
from logscreen import login

loginstart = subPage(target=login)
def main(page:ft.Page):
    page.title = "teste"
    page.padding = 0
    page.window.maximized= False
    page.window.resizable = False
   
    menubar = ft.Row([ft.MenuBar(
        
        style=ft.MenuStyle(
            padding=1,alignment=ft.alignment.top_right),
        controls=[
            ft.SubmenuButton(
                ft.Text('Produtos'),
                controls=[
                    ft.SubmenuButton(
                        ft.Text('Cadastro')
                    )
                ]
            ),
            ft.SubmenuButton(
                ft.Text('uuu'),
                controls=[
                    ft.SubmenuButton(
                        ft.Text('Cadastro')
                    )
                ]
            ),
            ft.IconButton(
                icon=ft.icons.ABC, height= 40
            )
        ]
    )
    ],width=ft.Window.width,height=40)



    page.add(ft.ElevatedButton("start new page"))
    page.update()


if __name__ == "__main__":
    loginstart.start()
    ft.app(target=main)