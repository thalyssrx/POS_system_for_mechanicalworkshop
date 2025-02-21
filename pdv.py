from flet_multi_page import *
import flet as ft
from logscreen import login
import mysql.connector

loginwindow = subPage(target=login)

database = mysql.connector.connect(host = 'localhost',user ='root',database ='pdv_oficina',password = 'Superindy11.')         
databasecursor = database.cursor()

if database.is_connected():
   print('banco de dados conectado')
  
def getcolumninfo():
   getprodutoscolumnumber = "select column_name from information_schema.columns where table_schema = 'pdv_oficina' and table_name = 'produtos' order by ordinal_position;"
   databasecursor.execute(getprodutoscolumnumber)   
   fetchcolumnnanes = databasecursor.fetchall()
   resultado = []
   for i in fetchcolumnnanes:
      resultado.extend(i)
   
   return resultado
   
print(getcolumninfo())

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

   def page_inicio():
      inicioview = ft.Column(
         controls=[
         ft.Container(
            expand=5,bgcolor='red'
         ),ft.Text(
            value="INICIO",size=20,color=ft.Colors.BLACK,
            weight=ft.FontWeight.W_600,expand=5,bgcolor='yellow'
         ),ft.Container(bgcolor='red',expand=5)],
         spacing=0,expand=90)
      return inicioview  
   def page_produtos():
      def table():
         
         def onselectrow():
            match page.platform:
               case  ft.PagePlatform.ANDROID:
                  pass
               case ft.PagePlatform.WINDOWS:
                  pass
         def ontapcell():
            match page.platform:
               case  ft.PagePlatform.ANDROID:
                  pass
               case ft.PagePlatform.WINDOWS:
                  pass

         def generate_columns():
            columns_names = getcolumninfo()
            columns = []
            for c in range(len(getcolumninfo())):
                  columns.append(ft.DataColumn(ft.Text(columns_names[c],color='black')))
            
            return columns

         def generate_rows():
            rows = []
            rowcount = 0
            for row in range(20):
               cells = []
               for _ in range(len(getcolumninfo())):
                  if  _%len(getcolumninfo())== 0:
                     rowcount = str(rowcount)
                     cells.append(ft.DataCell(ft.Text('ND'+rowcount),on_tap=ontapcell()))
                     rowcount = int(rowcount)
                     rowcount = rowcount+1
                  else:
                     cells.append(cells[-1])
               rows.append(ft.DataRow(cells=cells,on_select_changed= onselectrow()))
            return rows
         
         table = ft.DataTable(
            expand=100,
            columns=generate_columns(),
            rows=generate_rows(),
            data_row_max_height=48,
            border= ft.border.all(1,"black"),
            vertical_lines= ft.BorderSide(1,'black'),

            )
         
         
         return table

      rowtablewlistview = ft.ListView([ft.Row([table()], scroll= ft.ScrollMode.ALWAYS)],expand=95)

      produtosview = ft.Column(
      controls=[
      ft.Container(
         expand=5,bgcolor='red'
      ),ft.Text(
         value="PRODUTOS",size=20,color=ft.Colors.BLACK,
         weight=ft.FontWeight.W_600,expand=5,bgcolor='yellow'
      ),rowtablewlistview
      ,ft.Container(bgcolor='red',expand=5)],
      spacing=0,expand=90)
   
      return produtosview
   def page_teste():
      testeview = ft.Column(
         controls=[
         ft.Container(
            expand=5,bgcolor='red'
         ),ft.Text(
            value="TESTE",size=20,color=ft.Colors.BLACK,
            weight=ft.FontWeight.W_600,expand=5,bgcolor='yellow'
         ),ft.Container(bgcolor='red',expand=5)],
         spacing=0,expand=90)
      
      return testeview
   

   def route_change(route):
      match page.route:
         case "/inicio":
            view.controls.__delitem__(1)
            view.controls.append(page_inicio())
         case "/produtos":
            view.controls.__delitem__(1)
            view.controls.append(page_produtos())
         case "/teste":
            view.controls.__delitem__(1)
            view.controls.append(page_teste())
      page.update()
         
   page.on_route_change = route_change 
   
   view = ft.Row(controls=[sidebar(),page_inicio()],expand=True,spacing=0,alignment=ft.MainAxisAlignment.START)
   page.add(view)
    

if __name__ == "__main__": 
    ft.app(target=main,assets_dir='Assets',view=ft.AppView.WEB_BROWSER)