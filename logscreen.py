from flet import *

def login(log:Page):
    log.title = 'Login'
    log.window.title_bar_hidden = True
    log.window.width =250
    log.window.height = 400
    log.window.resizable = False
    log.window.center()
    log.window.always_on_top = True
    log.bgcolor=colors.WHITE
    log.padding = 0
    
    
   
    
    DragArea = WindowDragArea(
        Container(
        margin=0,padding=0),height=139,expand=True,maximizable=False)
        
    Colums_Text = WindowDragArea(
        Container(
        margin=0,padding=0),height=113, width=25,maximizable=False )  
    
    Text_Inputs=Column(
        alignment=MainAxisAlignment.CENTER,width=190,height=105,controls=([
            TextField('',width=200,focused_border_color=colors.BLACK,fill_color=colors.WHITE,label='Nome',label_style=TextStyle(color=colors.BLACK)),
            TextField('',width=200,focused_border_color=colors.BLACK,fill_color=colors.WHITE,label='Senha',label_style=TextStyle(color=colors.BLACK))
            ])
    )
    Row_Colums_Text = Row(spacing=0,controls=[
                Colums_Text,Text_Inputs,Colums_Text
            ])
    
    Full_View_Colum= Column(
        spacing=0,controls=([DragArea,Row_Colums_Text,DragArea])
    )

    log.add(Full_View_Colum)
    
app(login)