import flet as ft
from pages.table_produtos import table
from db_variables import *

def page_produtos(page:ft.Page):
   if database.is_connected():
      print('banco de dados conectado')

   def searchbar_onchange(e):
      produtosview.controls[1].controls[3] = table(e.control.value,actualactivecheckbox)

      page.update()

   def checkboxlocalizar_onchange(e):
      print(e.control)
      global actualactivecheckbox
      match e.control.label:
         case 'Código de Barras':
            CheckBoxsLocalizar.controls[1].value = False
            CheckBoxsLocalizar.controls[2].value = False
            actualactivecheckbox = "`Código de Barras`"

         case 'Nome':
            CheckBoxsLocalizar.controls[0].value = False
            CheckBoxsLocalizar.controls[2].value = False
            actualactivecheckbox = 'Descrição'
         case 'Código':
            CheckBoxsLocalizar.controls[0].value = False
            CheckBoxsLocalizar.controls[1].value = False
            actualactivecheckbox = 'Código_Interno'
      page.update()
      return actualactivecheckbox
   
   Searchbar = ft.SearchBar(
      bar_bgcolor='white',
      bar_overlay_color='white',
      bar_text_style=ft.TextStyle(color='black'),
      divider_color='red',
      on_change   = searchbar_onchange
   )

   CheckBoxsLocalizar = ft.Row(
   spacing=0,
   expand=True,
   controls=[
      ft.Checkbox(label='Código de Barras',on_change=checkboxlocalizar_onchange),
      ft.Checkbox(label='Nome',on_change=checkboxlocalizar_onchange,value=True),
      ft.Checkbox(label='Código',on_change=checkboxlocalizar_onchange)
   ]
)

   produtosview = ft.Row(
      spacing=0,
      expand=True,
      controls=[
         ft.Container(bgcolor='white',expand=2),
         ft.Column(
            spacing=0,
            expand=98,
            controls=[
               ft.Container(expand=5,bgcolor='white'),
               ft.Text(
                  value="PRODUTOS",size=20,color=ft.Colors.BLACK,
                  weight=ft.FontWeight.W_600,expand=5,bgcolor='white'
               ),
               ft.Row(
                  expand=8,
                  spacing=0,
                  controls=[
                     ft.Container(
                        expand=2,
                        padding=ft.Padding(0,10,10,10),
                        content= Searchbar
                     ),
                     ft.Column(
                        expand=2,
                        spacing = 0,
                        controls=[
                           ft.Text(
                              color='black',
                              value ='Localizar por:',
                              ),
                              CheckBoxsLocalizar
                           
                        ]
                     )
                  ]
               ),
               table(),
               ft.Container(bgcolor='white',expand=5)
            ],
         ),
         ft.Container(bgcolor='white',expand=2)
      ]
   )

   return produtosview