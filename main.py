import flet as ft
from backend.A_form import InputForm
 
 
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window.resizable = True
    page.add( 
        ft.Container(content=InputForm(page)), 
    )
  
    
ft.app(main)
       