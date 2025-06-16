from flet_multi_page import *
import flet as ft
from db_variables import *

from sidebar import sidebar
from pages.page_inicio import page_init
from pages.page_produtos import page_produtos
from pages.page_teste import page_teste




if database.is_connected():
   print('banco de dados conectado')

def main(page:ft.Page):
   page.title = "PDV"
   page.window.title_bar_hidden=False
   page.padding = 0
   page.window.maximized= True
   page.window.resizable = False
   page.bgcolor=ft.Colors.WHITE
   

   def route_change(route):
      page.views.clear()

      match page.route:
         case "/":
            page.go("/inicio")
         case "/inicio":
            page.views.append(ft.View(
               "/inicio",
               [ft.Row(
                  controls=[sidebar(page),page_init()],
                  expand=True,
                  spacing=0,
                  alignment=ft.MainAxisAlignment.START)],
               padding=0,
               bgcolor=ft.Colors.WHITE
            ))
         case "/produtos":
            page.views.append(ft.View(
               "/produtos",
               [ft.Row(
                  controls=[sidebar(page),page_produtos(page)],
                  expand=True,
                  spacing=0,
                  alignment=ft.MainAxisAlignment.START)],
               padding=0,
               bgcolor=ft.Colors.WHITE
            ))
         case "/teste":
            page.views.append(ft.View(
               "/teste",
               [ft.Row(
                  controls=[sidebar(page),page_teste()],
                  expand=True,
                  spacing=0,
                  alignment=ft.MainAxisAlignment.START)],
               padding=0,
               bgcolor=ft.Colors.WHITE
            ))
      page.update()
      
   def view_pop(view):
      page.views.pop()
      top_view = page.views[-1]
      page.go(top_view.route)

   page.on_route_change = route_change 
   page.on_view_pop = view_pop
   
   page.go('/inicio')
    

if __name__ == "__main__": 
    ft.app(target=main,assets_dir='Assets',view=ft.AppView.FLET_APP)