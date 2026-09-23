import flet as ft
from db_variables import *


def table(searchbarentry = '',actualactivecheckbox = 'Descrição'):

   def listview_onscroll(e):
      print(e.pixels)

   # Use a fixed width for each column (optional for alignment)
   cell_width = 100
   cell_height = 50
   cell_padding = 4

   # Function to generate one row
   def build_row(row_index: int) -> ft.Container:
      return ft.Container(
         content=ft.Row(
               controls=[
                  ft.Container(
                     content=ft.Text(f"R{row_index + 1}C{col_index + 1}"),
                     width=cell_width,
                     height= cell_height,
                     padding=cell_padding
                  )
                  for col_index in range(15)
               ],
               spacing=0,
               wrap=False,
         ),
         padding=ft.padding.symmetric(vertical=2),
      )

   # Generate all rows
   rows = [build_row(i) for i in range(6000)]

   # Optional header row
   header = ft.Row(
      controls=[
         ft.Container(
               content=ft.Text(f"Col {i + 1}"),
               width=cell_width,
               padding=cell_padding
         )
         for i in range(15)
      ],
      spacing=0,
      wrap=False,
   )

   # Wrap with Column so header stays on top
   tab = ft.Column(
            controls=[
                header,
                lv:= ft.ListView(
                    controls=rows,
                    spacing=0,
                    auto_scroll=False,
                    expand=True,
                    on_scroll=listview_onscroll,
                    first_item_prototype=True,
                    build_controls_on_demand=True
                ),
            ],
            expand=95,
        )
   rows.clear()
   return tab
    

    # def batches(iterable, batch_size):
    #     iterator = iter(iterable)
    #     while batch := list(islice(iterator, batch_size)):
    #         yield batch

    # for batch in batches(rows, 200):
    #     lv.controls.extend(batch)
    #     lv.update()
    #     await asyncio.sleep(10)

def oldtable(searchbarentry = '',actualactivecheckbox = 'Descrição'):
   if database.is_connected():
      print('banco de dados conectado')
   
   databasecursor = database.cursor(buffered=True)
   
   def generate_columns():
      getprodutoscolumnumber = "select column_name from information_schema.columns where table_schema = 'pdv_oficina' and table_name = 'produtos' order by ordinal_position;"
      databasecursor.execute(getprodutoscolumnumber)   
      fetchcolumnnanes = databasecursor.fetchall()
      columns = []
      for tuple in fetchcolumnnanes:
         columns.append(ft.DataColumn(ft.Text(value= tuple[0],color='black')))
      
      return columns

   table = ft.DataTable(
      expand=100,
      bgcolor= ft.Colors.GREY_300,
      columns=generate_columns(),
      rows=[],
      data_row_min_height=24,
      data_row_max_height=30,
      border= ft.border.all(1,"black"),
      vertical_lines= ft.BorderSide(1,'black'),
   )

   if searchbarentry == '':
      query = (f"select * from produtos")
   else:
      operator = ''
      if actualactivecheckbox == 'Descrição':
         operatorcount =searchbarentry.count('%')
         if operatorcount%2 == 0:
            operator = '%'
         else:
            operator = ''
      
      query = (f"select * from produtos where {actualactivecheckbox} like '{searchbarentry}{operator}'")
      print(query)
   databasecursor.execute(query)
   query = databasecursor.fetchmany(100)
   for tuple in query:
      table.rows.append(ft.DataRow(color='white',cells=[
         ft.DataCell(ft.Text(tuple[0],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[1],color='red',weight='bold')),
         ft.DataCell(ft.Text(f"R$ {tuple[2]}",color='red',weight='bold')),
         ft.DataCell(ft.Text(f"R$ {tuple[3]}",color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[4],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[5],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[6],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[7],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[8],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[9],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[10],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[11],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[12],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[13],color='red',weight='bold')),
         ft.DataCell(ft.Text(tuple[14],color='red',weight='bold'))
      ]))

   rowtablewlistview = ft.ListView(
      controls=[ft.Row([table], 
      scroll= ft.ScrollMode.ALWAYS)],
      expand=95
      )
      
   return rowtablewlistview  