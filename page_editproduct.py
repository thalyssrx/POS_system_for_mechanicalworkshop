import flet as ft 

def page_editproduct():
      a = ft.Row(
         expand=True,
         spacing=0,
         controls=[
            ft.Column(
               expand = 98,
               spacing = 0,
               controls=[
                  ft.Container(
                     expand=5,
                     bgcolor='red'
                  ),
                  ft.TextField(

                  ),
                  ft.Container(
                     expand=5,
                     bgcolor='red'
                  )     
               ]
            )
            ]
      )

      return a