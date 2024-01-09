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

i = 0
while True:
    if i < 990:
        i += 1
        if isClicking:
            mouse.double_click(button='left') # Выбор кнопки мышки
            time.sleep(0.05) # Задержка после каждого нажатия
    else:
        time.sleep(600) # Для передышки после определенного количество нажатий
        i = 0






