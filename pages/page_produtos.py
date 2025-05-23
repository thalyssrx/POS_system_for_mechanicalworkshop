import flet as ft
import mysql.connector
from db_variables import *

def produtosview(page:ft.Page):
      
      def searchbar():
         
         def searchbar_onchange(e):
            page.controls[0].controls[1].controls[1].controls[3] = table(e.control.value)
            
            databasecursor = database.cursor(buffered=True)
            
            query = (f"select * from produtos where {actualactivecheckbox} like '{e.control.value}'")
            print(query,"-searchbaronchange")

            databasecursor.execute(query)
            result = databasecursor.fetchall()
             
            databasecursor.close()
            page.update()

         searchbar = ft.SearchBar(
            bar_shape=ft.RoundedRectangleBorder(),
            bar_border_side=ft.BorderSide(20,'black',10),
            bar_bgcolor='white',
            bar_overlay_color='white',
            bar_text_style=ft.TextStyle(color='black'),
            divider_color='red',
            on_change   = searchbar_onchange
         )
         return searchbar

      def checkboxlocalizar():   
         
         def actualactivecheckbox():
            global actualactivecheckbox
            if Codigobarras.value == True:
               actualactivecheckbox = "`Código de Barras`"
            if Nome.value == True:
               actualactivecheckbox = 'Descrição'
            if Codigo.value == True:
               actualactivecheckbox = 'Código_Interno'
            return actualactivecheckbox

         def checkboxlocalizar_onchange(e):
            match e.control.label:
               case 'Código de Barras':
                  Nome.value = False
                  Codigo.value = False
                  
               case 'Nome':
                  Codigobarras.value = False
                  Codigo.value = False
                  
               case 'Código':
                  Codigobarras.value = False
                  Nome.value = False
                  

            actualactivecheckbox()
            page.update()
         
              
         Codigobarras = ft.Checkbox(label='Código de Barras',on_change=checkboxlocalizar_onchange)
         Nome = ft.Checkbox(label='Nome',on_change=checkboxlocalizar_onchange,value=True)
         Codigo = ft.Checkbox(label='Código',on_change=checkboxlocalizar_onchange)

         actualactivecheckbox()

         CheckBoxsLocalizar = ft.Row(
            spacing=0,
            expand=True,
            controls=[
               Codigobarras,
               Nome,
               Codigo
            ]
         )
         
         return CheckBoxsLocalizar      

      def table(searchbarentry = ''):
         
         def get_columns_names():
            getprodutoscolumnumber = "select column_name from information_schema.columns where table_schema = 'pdv_oficina' and table_name = 'produtos' order by ordinal_position;"
            databasecursor.execute(getprodutoscolumnumber)   
            fetchcolumnnanes = databasecursor.fetchall()
            excluded_colum_names = []  #lista de nomes das colunas que o programa não vai mostrar 
            columns_names = []
            for i in fetchcolumnnanes:
               if i[0] in excluded_colum_names:
                  print(i[0])
               else:
                  columns_names.extend(i)
            
            return columns_names
         
         def get_columns():
            columns = []
            for c in get_columns_names():
               columns.append(ft.DataColumn(ft.Text(value= c,color='black')))
            
            return columns

         def generate_rows():
            colum_names = str(get_columns_names())
            for char in colum_names:
               if char == "[":
                  colum_names = colum_names.replace(char,"")
               if char == "]":
                  colum_names = colum_names.replace(char,"")
            
            print(colum_names)
            databasecursor = database.cursor(buffered=True)
            if searchbarentry == '':
               query = (f"select {colum_names} from produtos")
            else:
               query =(f"select {colum_names} from produtos where {actualactivecheckbox} like '{searchbarentry}'")
            print(query)
            databasecursor.execute(query)
            result = databasecursor.fetchall()
            
            rows=[]
            for row in result:
               
               cells = []
               for field in row:
                  
                  cells.append(ft.DataCell(ft.Text(field)))
               rows.append(ft.DataRow(cells=cells))
            
            databasecursor.close()
         
            return rows

         table = ft.DataTable(
            expand=100,
            columns=get_columns(),
            rows=generate_rows(),
            data_row_max_height=48,
            border= ft.border.all(1,"black"),
            vertical_lines= ft.BorderSide(1,'black'),
         )
         
         rowtablewlistview = ft.ListView(
            controls=[ft.Row([table], 
            scroll= ft.ScrollMode.ALWAYS)],
            expand=95
            )
         
         return rowtablewlistview      
      
      
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
                           content= searchbar()
                        ),
                        ft.Column(
                           expand=2,
                           spacing = 0,
                           controls=[
                              ft.Text(
                                 color='black',
                                 value ='Localizar por:',
                                 ),
                                 checkboxlocalizar()
                              
                           ]
                        )
                     ]
                  ),
                  table(),
                  ft.Container(bgcolor='white',expand=5)
               ],
            )
         ]
      )
   
      return produtosview