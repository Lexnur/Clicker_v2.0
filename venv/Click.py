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

push = int(input('Введи кол-во кликов:\n'))
pause = float(input('Введи интервал между кликами в интервале от 0.05 до 1 сек.\n'))
stop = int(input('Введи время для остановки после нажатий: ... сек.\n'))
time.sleep(1)
print('Press the keys: "Ctrl + Q"')


i = 0
while True:
    if i < push:
        i += 1
        if isClicking:
            mouse.double_click(button='left') # Выбор кнопки мышки
            time.sleep(pause) # Задержка после каждого нажатия
    else:
        time.sleep(stop) # Для передышки после определенного количество нажатий
        i = 0






