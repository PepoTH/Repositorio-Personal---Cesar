import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 600
    page.padding = 30
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window_center()


    def valid(e):
        if(len(e.control.value) > 1):
            e.control.value = e.control.value[0]
            e.control.update()

        if(e.control == txt1): txt2.focus()
        if(e.control == txt2): txt3.focus()
        if(e.control == txt3): txt4.focus()

        if("".join([txt1.value,txt2.value,txt3.value,txt4.value]) == "2004"):
            print("Correct")

    txt1 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt2 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt3 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    txt4 = ft.TextField(width=40,height=50,text_size=20,content_padding=10,text_align = "center",on_change=valid)
    
    row = ft.Row([
        txt1,
        txt2,txt3,txt4
    ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(ft.Container(ft.Column(
        [
            ft.Text("Login",size=30),
            ft.Text("Ingrese el codigo"),
            row
        ],alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )))

ft.app(target=main)