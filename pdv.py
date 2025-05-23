from flet_multi_page import *
import flet as ft
from db_variables import *

import pages.page_inicio
import pages.page_produtos
import pages.page_teste




if database.is_connected():
   print('banco de dados conectado')

def main(page:ft.Page):
   page.title = "PDV"
   page.window.title_bar_hidden=False
   page.padding = 0
   page.window.maximized= True
   page.window.resizable = False
   page.bgcolor=ft.Colors.WHITE
   
   def sidebar():
      
      match page.platform:
         case ft.PagePlatform.ANDROID:
            page.bottom_appbar = ft.BottomAppBar(
               bgcolor=ft.Colors.BLUE,
               shape=ft.NotchShape.CIRCULAR,
               content=ft.Row(
                  controls=[
                  ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                  ft.Container(expand=True),
                  ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                  ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE)]
            ))
            sidebar = ft.Container()
            return sidebar
         case ft.PagePlatform.WINDOWS:
               def bar_changepage(e):
                  index = e.control.selected_index
                  match index:
                     case 0:
                        e.page.go("/inicio")
                     case 1:
                        e.page.go("/produtos")
                     case 2:
                        e.page.go("/teste")
                  

               sidebar = ft.Column(
                  width=75,
                  controls=[
                  ft.NavigationRail(
                     bgcolor=ft.Colors.GREY_500,
                     selected_index=0,
                     expand=True,
                     label_type=ft.NavigationRailLabelType.ALL,
                     group_alignment=-1.0,indicator_shape=ft.RoundedRectangleBorder(radius=0),
                     destinations=[
                           ft.NavigationRailDestination(
                              icon=ft.Icons.STORE_SHARP,
                              label='Inicio',
                               
                           ),
                           ft.NavigationRailDestination(
                              icon=ft.Icons.STORE_SHARP,
                              label='Produtos',
                               
                           ),
                           ft.NavigationRailDestination(
                              icon=ft.Icons.STORE_SHARP,
                              label='Teste',
                              
                           )],
                      on_change= bar_changepage          
                      )
                  ])
               
                
               return sidebar

   def route_change(route):
      
      match page.route:
         case "/inicio":
               page.controls[0].controls.__delitem__(1)
               page.controls[0].controls.append(pages.page_inicio.page_init())
         case "/produtos":
            page.controls[0].controls.__delitem__(1)
            page.controls[0].controls.append(pages.page_produtos.produtosview(page))
         case "/teste":
            page.controls[0].controls.__delitem__(1)
            page.controls[0].controls.append(pages.page_teste.page_teste())
      page.update()

   page.on_route_change = route_change 
   
   page.add(ft.Row(
      controls=[sidebar(),pages.page_inicio.page_init()],
      expand=True,
      spacing=0,
      alignment=ft.MainAxisAlignment.START)
      )
    

if __name__ == "__main__": 
    ft.app(target=main,assets_dir='Assets',view=ft.AppView.FLET_APP)