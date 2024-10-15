from flet import *


def main(page:Page):
    page.title = "teste"
    page.padding = 0
    
    a = Container(
        margin=0,
        padding=1,
        alignment=alignment.center,
        bgcolor=colors.GREY_600,
        width=80,
        height=40,
        border_radius=0,
        content= SubmenuButton(
            content=Text('Produtos'),
            controls=[
                SubmenuButton(
                    content=Text('a')
                )
                ]
            )
        )      
    
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
                width=100,
                style=ButtonStyle(
                    bgcolor=colors.GREY_500),
                controls=[
                    SubmenuButton(
                        Text('Cadastro')
                    )
                ]
            ),
            SubmenuButton(
                Text('cuuuu'),
                width=100,style=ButtonStyle(
                    bgcolor=colors.GREY_500),
                controls=[
                    SubmenuButton(
                        Text('Cadastro')
                    )
                ]
            )
            
        ]
    )
    TopRow = Row([menubar])
    
    page.add(TopRow)

app(main)