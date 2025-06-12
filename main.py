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
      
      match page.route:
         case "/inicio":
               page.controls[0].controls.__delitem__(1)
               page.controls[0].controls.append(page_init())
         case "/produtos":
            page.controls[0].controls.__delitem__(1)
            page.controls[0].controls.append(page_produtos(page))
         case "/teste":
            page.controls[0].controls.__delitem__(1)
            page.controls[0].controls.append(page_teste())
      page.update()

   page.on_route_change = route_change 
   
   page.add(ft.Row(
      controls=[sidebar(page),page_init()],
      expand=True,
      spacing=0,
      alignment=ft.MainAxisAlignment.START)
      )
    

if __name__ == "__main__": 
    ft.app(target=main,assets_dir='Assets',view=ft.AppView.FLET_APP)