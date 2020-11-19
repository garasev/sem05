# Гарасев Н.А. ИУ7-22Б
# Программа перевода чисел из десятичной
# системы счисления в четвертичную и обратно.

from tkinter import*
from tkinter import messagebox
from math import*
# *****************************************************************************
# Переменные
# Координаты для кнопок
sx = 30
sy = 150
dx = 100
dy = 100
# Задержка нажатия клавиши
flash = 100
# Кол-во знако после запятой
eps=6
# Текст вспомогательных кнопок
BS = 'C'
DT = '.'
SWP = '↔'
TR = 'Перевести'
MIN = '-'
# Флаг точки
DTF = 0
# Label
label_10_4 = '10сс → 4 сс'
label_4_10 = '4 cc → 10cc'
# Info
infoprog = 'Программа перевода чисел из десятичной\
 системы счисления в четвертичную и обратно.'
infome = 'Гарасев Н.А. ИУ7-22Б'
titprog = 'О Программе'
titme = 'Об Авторе'
# *****************************************************************************
# Все использованные функции
# Перевод дробной части (10 -> 4)
def trans_part_1(part1):
    rez = ''
    part1 = float('0.'+part1)
    for i in range(eps):
        part1 *= 4
        rez += str(trunc(part1))
        part1 -= trunc(part1)
    return rez.rstrip('0')
# Функция кнопки перевода
def key_TR():
    outputentry.config(state = NORMAL)
    outputentry.delete(0,len(outputentry.get()))
    # Разделение на целую и дробную часть
    min_flag = 0
    part = inputentry.get().split('.')
    if inputentry.get() != '':
        if inputentry.get()[0] == '-':
            part[0] = int(part[0][1:])
            min_flag = 1
        else:
            part[0] = int(part[0])
        
    part0 = ''
    part1 = ''
    if min_flag == 1:
        outputentry.insert(END,'-')
    # Проверка, в какую сторону перевод
    if currentlabel['text'] == label_10_4 and inputentry.get() != '':
        while part[0]>0:
            part0 += str(part[0]%4)
            part[0] //= 4
        part0 = part0[::-1]
        if part0 == '':
            part0 = '0'
        outputentry.insert(END,str(part0))
        if len(part)>1:
            part1 = trans_part_1(part[1])
            outputentry.insert(END,('.'+str(part1)))
        outputentry.config(state = DISABLED)
    elif currentlabel['text'] == label_4_10 and inputentry.get() != '':
        mp = 1
        part0 = 0
        while part[0]>0:
            part0 += mp*(part[0]%10)
            mp *= 4
            part[0] //=10
        mp = 1/4
        if part0 == '':
            part0 = '0'
        if len(part)>1:
            part[1] = part[1][::-1]
            part[1] = int(part[1])
            part1 = 0
            while part[1]>0:
                part1 += (part[1]%10)*mp
                mp /= 4
                part[1] //= 10
            part0 += part1
        outputentry.insert(END,str(part0))
    outputentry.config(state = DISABLED)
# Функция ввода с помощью кнопок
def key(i):
    # Локальная ф-ия для функций с параметром
    def k():
        # Изменение состояния поля
        inputentry.config(state = NORMAL)
        # Ввод в соответстие с системой счисления
        if inputentry.get() == '0':
            inputentry.delete(0,len(inputentry.get()))
        if currentlabel['text'] == label_10_4 and len(inputentry.get()) < 8:
            inputentry.insert(END,str(i))
        elif int(i)<4 and len(inputentry.get()) < 8:
            inputentry.insert(END,str(i))
        # Изменение состояния поля    
        inputentry.config(state = DISABLED)
    return k
# Функция кнопки BackSpace
def key_BS():
    global DTF
    outputentry.config(state = NORMAL)
    outputentry.delete(0,len(inputentry.get()))
    outputentry.config(state = DISABLED)
    inputentry.config(state = NORMAL)
    if inputentry.get() != '' :
        if inputentry.get()[-1] == '.':
            DTF = 0
        inputentry.delete(len(inputentry.get())-1)
    inputentry.config(state = DISABLED)
# Функция точки
def key_DT():
    global DTF
    inputentry.config(state = NORMAL)
    if DTF == 0 and len(inputentry.get()) < 8:
        if inputentry.get() == '' or inputentry.get() == '-':
            inputentry.insert(END, '0')
        inputentry.insert(END, '.')
        DTF = 1
    inputentry.config(state = DISABLED)
# Функция меняющая сторону перевода
def key_SWP():
    global DTF
    if currentlabel['text'] == label_10_4:
        currentlabel.config(text = label_4_10)
    else:
        currentlabel.config(text = label_10_4)
    inputentry.config(state = NORMAL)
    inputentry.delete(0,len(inputentry.get()))
    inputentry.config(state = DISABLED)
    outputentry.config(state = NORMAL)
    outputentry.delete(0,len(outputentry.get()))
    outputentry.config(state = DISABLED)
    DTF = 0
#
def key_MIN():
    inputentry.config(state = NORMAL)
    if inputentry.get() == '':
        inputentry.insert(END, '-')    
    inputentry.config(state = DISABLED)
# Функция для нажатия цифры с клавиатуры 
def keyp(i):
    def kp(event):
        # Изменение состояния кнопки
        Buttons[i].config(state = ACTIVE)
        # Актиация функии кнопки
        Buttons[i].invoke()
        # Изменение состояния кнопки
        window.after(flash, lambda: Buttons[i].config(state = NORMAL))
    return kp
# Функция для нажатия BackSpace с клавиатуры 
def keyp_BS(event):
    button_bs.config(state = ACTIVE)
    button_bs.invoke()
    window.after(flash, lambda: button_bs.config(state = NORMAL))
# Функция для нажатия точки с клавиатуры     
def keyp_DT(event):
    button_dt.config(state = ACTIVE)
    button_dt.invoke()
    window.after(flash, lambda: button_dt.config(state = NORMAL))
# Функция для смены стороны перевода с клавиатуры (Space)    
def keyp_SWP(event):
    button_swp.config(state = ACTIVE)
    button_swp.invoke()
    window.after(flash, lambda: button_swp.config(state = NORMAL))
# Функция для кнопки "Перевести" c клаввиатуры (Enter)    
def keyp_TR(event):
    button_tr.config(state = ACTIVE)
    button_tr.invoke()
    window.after(flash, lambda: button_tr.config(state = NORMAL))
# ф-ия кнопки минус
def keyp_MIN(event):
    button_min.config(state = ACTIVE)
    button_min.invoke()
    window.after(flash, lambda: button_min.config(state = NORMAL))
# Функция очистки полей для меню
def clear(i):
    def cl():
        if i == 1:
            inputentry.config(state = NORMAL)
            inputentry.delete(0,len(inputentry.get()))
            inputentry.config(state = DISABLED)
        elif i == 2:
            outputentry.config(state = NORMAL)
            outputentry.delete(0,len(outputentry.get()))
            outputentry.config(state = DISABLED)
        elif i == 3:
            inputentry.config(state = NORMAL)
            inputentry.delete(0,len(inputentry.get()))
            inputentry.config(state = DISABLED)
            outputentry.config(state = NORMAL)
            outputentry.delete(0,len(outputentry.get()))
            outputentry.config(state = DISABLED)
    return cl
# Функция для меню: информаия
def info(i):
    def inf():
        if i == 1:
            messagebox.showinfo(titprog, infoprog)
        elif i == 2:
            messagebox.showinfo(titme, infome)
    return inf
# *****************************************************************************
# Виджеты
# Окно программы
window = Tk()
window.geometry('610x560')
window.title('Калькулятор Лаба №1')
window.resizable(False, False)
# Menu
mainmenu = Menu(window)
window.config(menu = mainmenu)
# Первая вкладка
clearmenu = Menu(mainmenu, tearoff = 0)
clearmenu.add_command(label = 'Очистить ВВОД', command = clear(1))
clearmenu.add_command(label = 'Очистить ВЫВОД', command = clear(2))
clearmenu.add_command(label = 'Очистить ВСЕ', command = clear(3))
# Справка
infomenu = Menu(mainmenu, tearoff = 0)
infomenu.add_command(label = 'О Программе', command = info(1))
infomenu.add_command(label = 'Об Авторе', command = info(2))
# Соединение menu
mainmenu.add_cascade(label = 'Очистка', menu = clearmenu)
mainmenu.add_cascade(label = 'Справка', menu = infomenu)
# Кнопки цифр
Buttons = {}
for i in range(10):
    Buttons.update({i : Button(window, text = str(i),
                               font = 'Arial 20',
                               bg = 'grey', fg = 'black')})
# Кнопка BackSpace
button_bs = Button(window, text = BS,
                   font = 'Arial 20',
                   bg = 'orange', fg = 'black')
# Кнопка точки
button_dt = Button(window, text = DT,
                   font = 'Arial 40',
                   bg = 'orange', fg = 'black')
# Кнопка смены перевода
button_swp = Button(window, text = SWP,
                     font = 'Arial 15',
                     bg = 'orange', fg = 'black')
# Кнопка перевода
button_tr = Button(window, text = TR,
                   font = 'Arial 20',
                   bg = 'orange', fg = 'black')
# Кнопка минуса
button_min = Button(window, text = MIN,
                   font = 'Arial 40',
                   bg = 'orange', fg = 'black')
# Label
currentlabel = Label(window, text = label_10_4,  font = 'Arial 30')
# Entry
inputentry = Entry(window, state = DISABLED,
                   font='Arial 30', fg = 'black')
outputentry = Entry(window, state = DISABLED,
                    font='Arial 30', fg = 'black')
# *****************************************************************************
# Размещение виджетов
# Кнопки цифр
for i in range(1,10):
    Buttons[i].place(x = sx+((i-1)%3)*dx , y = sy+((i-1)//3)*dy,
                     height = 80, width = 80)
Buttons[0].place(x = sx+1*dx , y = sy+3*dy,
                 height = 80, width = 80)
# Кнопка BackSpace
button_bs.place(x = sx+3*dx, y = sy,
                height = 80, width = 160)
# Кнопка точки
button_tr.place(x = sx+3*dx, y = sy+dy,
                height = 80, width = 160)
# Кнопка смены перевода
button_dt.place(x = sx+3*dx, y = sy+3*dy,
                height = 80, width = 80)
# Кнопка перевода
button_swp.place(x = sx+2.5*dx, y = sy-dy+15,
                height = 50, width = 50)
# Кнопка минуса
button_min.place(x = sx+3*dx, y = sy+2*dy,
                height = 80, width = 160)
# Label
currentlabel.place(x = sx+1.58*dx, y = 0)
# Entry
inputentry.place(x = sx, y = sy-dy,
                 height = 80, width = 240)
outputentry.place(x = sx + 310, y = sy-dy,
                  height = 80, width = 240)
# *****************************************************************************
# Функции кнопок
# Кнопки цифр
for i in range(10):
    Buttons[i].config(command = key(str(i)))
    window.bind(str(i), keyp(i))
# Кнопка BackSpace
button_bs.config(command = key_BS)
window.bind('<BackSpace>', keyp_BS)
# Кнопка точки
button_dt.config(command = key_DT)
window.bind('.', keyp_DT)
# Кнопка смены перевода
button_swp.config(command = key_SWP)
window.bind('<space>', keyp_SWP)
# Кнопка перевода
button_tr.config(command = key_TR)
window.bind('<Return>', keyp_TR)
# Кнопка минуса
button_min.config(command = key_MIN)
window.bind('-', keyp_MIN)


window.mainloop()
