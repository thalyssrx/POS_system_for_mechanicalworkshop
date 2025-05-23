import flet as ft

def sidebar(page):
      
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