import keyboard
import mouse
import time


isClicking = False


def clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Не работает')
    else:
        isClicking = True
        print('Работает')

keyboard.add_hotkey('Ctrl + Q', clicker) # Комбинации клавиш для активации 'кликера'

while True:
    if isClicking:
        mouse.double_click(button='left') # Выбор кнопки мышки
        time.sleep(0.01) # Задержка после каждого нажатия



