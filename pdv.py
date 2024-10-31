from flet_multi_page import *
import flet as ft
from logscreen import login


loginwindow = subPage(target=login)


def main(page:ft.Page):
    page.title = "PDV"
    page.padding = 0
    page.window.maximized= True
    page.window.resizable = False
    page.bgcolor=ft.colors.WHITE
   
    login_icon_menubar = ft.IconButton(
        content= ft.Image(src="Icons/user.png",width=24,height=24,color=page.bgcolor),width=40,height=40,right=5)
    
    menubar = ft.Row([ft.MenuBar(
        expand=True,style=ft.MenuStyle(
            padding=0,alignment=ft.alignment.top_right,shape=ft.RoundedRectangleBorder(radius=0)),
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
            )
        ])]
        ,height=40,expand=True)
    
    
    
    page.add(ft.Stack([menubar,login_icon_menubar]))
    
    


if __name__ == "__main__":
    
    ft.app(target=main,assets_dir='Assets')