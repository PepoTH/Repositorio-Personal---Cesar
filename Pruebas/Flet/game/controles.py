import flet as ft
import time as t

def main(page: ft.Page):
    print('Inicio')
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 300
    page.padding = 0

    page.theme_mode = ft.ThemeMode.LIGHT

    def move(e):
        if(e.key == 'Arrow Left' and jugador.x >= 10):
                jugador.x -= 10
        elif(e.key == 'Arrow Right' and jugador.x <= page.window_width-40):
            jugador.x += 10
        elif(e.key == 'Arrow Up' and jugador.y >= 10):
            jugador.y -= 10
        elif(e.key == 'Arrow Down' and jugador.y <= page.window_height-80):
            jugador.y += 10

        page.update()

    jugador = ft.canvas.Rect(0,page.window_height-70,30,50)
    obj = ft.canvas.Circle(10,10,10)

    cv = ft.canvas.Canvas([
        jugador,obj
    ])

    page.on_keyboard_event = move

    page.add(cv)

    modeH = True
    modeV = True

    while(True):
        #Configuracion Horizontal
        if(modeH):
            if(obj.x >= 0 and obj.x <= page.window_width-20):
                obj.x += 10
            else:
                modeH = False
        else:
            if(obj.x == 0):
                modeH = True
            else:
                obj.x -= 10

        if(modeV):
            if(obj.y >= 0 and obj.y <= page.window_height-35):
                obj.y += 10
            else:
                modeV = False
        else:
            if(obj.y == 0):
                modeV = True
            else:
                obj.y -= 10
        
        t.sleep(0.03)
        print(obj.x)
        page.update()

ft.app(target=main)