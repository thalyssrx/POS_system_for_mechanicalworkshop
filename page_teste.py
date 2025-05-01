import flet as ft

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