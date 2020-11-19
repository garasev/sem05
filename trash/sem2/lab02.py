# Гарасев Н.А. ИУ7-22Б
# Программа подсчета времени сортировки

from tkinter import*
from tkinter import messagebox
from math import*
from time import*
from random import*
import numpy as np
#from numpy import*
# *****************************************************************************
# Переменные
# Info
infoprog = 'Программа для подсчета времени сортировки\
 разных массивов.'
infome = 'Гарасев Н.А. ИУ7-22Б'
titprog = 'О Программе'
titme = 'Об Авторе'
# *****************************************************************************
# Функции

def insertion_binary(li):
    start = clock()
    for i in range(1, len(li)):
        l, r = -1, i
        key = li[i]
        while l < r-1:
            mid = (r+l)//2
            if key < li[mid]:
                r = mid
            else:
                l = mid
        for j in range(i, r, -1):
            li[j] = li[j-1]
        li[r] = key
    finish = clock()
    return finish - start
def ss(arr, k):
    start = clock()
    if k == 1:
        np.sort(arr, kind = 'quicksort')
    if k == 2:
        np.sort(arr, kind = 'mergesort')
    if k == 3:
        np.sort(arr, kind = 'heapsort')    
    finish = clock()
    return finish - start
def time_sort(arr):
    start = clock()
    arr.sort()
    finish = clock()
    return finish - start

def proverka():
    arr = display_proverka.get()
    arr = arr.split()
    res = ''
    if 0<len(arr)<11:
        try:
            for i in range(len(arr)):
                if "." in arr[i]:
                    arr[i] = float(arr[i])
                else:
                    arr[i] = int(arr[i])
            insertion_binary(arr)
            for i in range(len(arr)):
                arr[i] = str(arr[i])
                res += (arr[i] + ' ')
            messagebox.showinfo(' Результат теста ', ' Отсортированный '+
                                    'массив:' + res)
        except ValueError:
            messagebox.showinfo(' Ошибка ', ' Введите корректные значения ')
    display_proverka.delete(0, END)

def main_process(st, k):
    label01.place(x = 15, y = 200)
    label02.place(x = 12, y = 250)
    label03.place(x = 5, y = 300)
    label04.place(x = 15, y = 350)
    n = int(st)
    list1 = [random()*2*10**9-10**9 for i in range(n)]
    list2 = list1
    t = insertion_binary(list1)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 200, width = 90)
    t = insertion_binary(list1)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 250, width = 90)
    list1.reverse()
    t = insertion_binary(list1)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 300, width = 90)
    t = time_sort(list2)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 350, width = 90)

def zachita(st, k):
    label05.place(x = 5, y = 200)
    label06.place(x = 5, y = 250)
    label07.place(x = 5, y = 300)
    n = int(st)
    list1 = [random()*2*10**9-10**9 for i in range(n)]
    list2 = list1
    list3 = list1
    t = ss(list1, 1)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 200, width = 90)
    t = ss(list2, 2)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 250, width = 90)
    t = ss(list3, 3)
    t = round(t, 6)
    t = str(t)
    label = Label(text = t, font = 'Arial 14')
    label.place(x = (150 + k*100), y = 300, width = 90)
    
def start():
    len1 = display1.get()
    len2 = display2.get()
    len3 = display3.get()
    if len(len1) > 0 :
        try:
            main_process(len1,1)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')
    if len(len2) > 0 :
        try:
            main_process(len2,2)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')
    if len(len3) > 0 :
        try:
            main_process(len3,3)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')

def start_zachita():
    len1 = display1.get()
    len2 = display2.get()
    len3 = display3.get()
    if len(len1) > 0 :
        try:
            zachita(len1,1)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')
    if len(len2) > 0 :
        try:
            zachita(len2,2)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')
    if len(len3) > 0 :
        try:
            zachita(len3,3)
        except ValueError:
            messagebox.showerror(' Error ', ' Некорректный ввод ')

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
window.title('Сортировщик Лаба №2')
window.resizable(False, False)
# Menu
mainmenu = Menu(window)
window.config(menu = mainmenu)
# Справка
infomenu = Menu(mainmenu, tearoff = 0)
infomenu.add_command(label = 'О Программе', command = info(1))
infomenu.add_command(label = 'Об Авторе', command = info(2))
# Соединение menu
mainmenu.add_cascade(label = 'Справка', menu = infomenu)
# Кнопки
# Кнопка запускающая тестирование сортировки
button_t = Button(window, text = ' TEST ',
                   font = 'Arial 14', command = proverka,
                   bg = 'orange', fg = 'black')
# Кнопка запуска времени сортировки
button_start = Button(window, text = ' START ',
                   font = 'Arial 14', command = start,
                   bg = 'orange', fg = 'black')
button_zachita = Button(window, text = ' ZACHITA ',
                   font = 'Arial 14', command = start_zachita,
                   bg = 'orange', fg = 'black')
# Поля
labelarr = Label (text = ' Введите длины массивов:',
                  font = 'Arial 14')
# Поле тестирования
labeltest = Label (text = 'Введите от 1 до 10 элементов\n'+
                   'для тестирования сортировки:', justify=LEFT )
# Поля таблиццы
label00 = Label (text = ' МАССИВЫ ',
                  font = 'Arial 14')
label01 = Label (text = ' Случайный ',
                  font = 'Arial 14')
label02 = Label (text = ' Отсортированный ',
                  font = 'Arial 14')
label03 = Label (text = ' Отсортированный \nв обратном порядке ',
                  font = 'Arial 14')
label04 = Label (text = ' Ф-ия sort ',
                  font = 'Arial 14')
label05 = Label (text = ' NUMPY quicksort ',
                  font = 'Arial 14')
label06 = Label (text = ' NUMPY mergesort ',
                  font = 'Arial 14')
label07 = Label (text = ' NUMPY heapsort',
                  font = 'Arial 14')
# Поля ввода
display_proverka = Entry(font = 'Arial 14')
display1 = Entry(font = 'Arial 14')
display2 = Entry(font = 'Arial 14')
display3 = Entry(font = 'Arial 14')
# *****************************************************************************
# Размещение виджетов
# Тестирование
labeltest.place(x = 5, y = 5)
display_proverka.place(x = 5, y = 50)
button_t.place(x = 250, y = 45)
# Основная программа
labelarr.place(x = 5, y = 100)
label00.place(x = 50, y = 150)

display1.place(x = 250, y = 100, width = 90)
display2.place(x = 350, y = 100, width = 90)
display3.place(x = 450, y = 100, width = 90)
button_start.place(x = 5, y = 400, width = 600)
button_zachita.place(x = 5, y = 500, width = 600)
window.mainloop()
