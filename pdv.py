from flet import *
from logscreen import *

def main(page:Page):
    page.title = "teste"
    page.padding = 0
    page.window.maximized= True
    page.window.resizable = False
    menubar = MenuBar(
        expand=True,
        style=MenuStyle(
            alignment=alignment.top_left,
            shape=BeveledRectangleBorder(radius=border_radius.all(0)),
            padding=0
        ),
        controls=[
            SubmenuButton(
                Text('Produtos'),
                width=100,height=30,
                
                controls=[
                    SubmenuButton(
                        Text('Cadastro')
                    )
                ]
            ),
            SubmenuButton(
                Text('uuu'),
                width=100,height=30,
                
                controls=[
                    SubmenuButton(
                        Text('Cadastro')
                    )
                ]
            ),
            IconButton(
                icon=icons.ABC_OUTLINED,
                height=30
            )
        ]
    )

    page.add(Row([menubar]))


app(login)