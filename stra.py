import tkinter as tk
from tkinter import *
from tkinter import messagebox



def stranica():
    home1 = tk.Tk()
    home1.title("Главная страница")
    home1.geometry("900x700")
    home1.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
    home1['bg'] = 'gold'  # цвет окна внутри
    button_forgot = Button(home1, text='Забыли пароль?', bg='gold', font='Arial 13')
    button_forgot.place(x=392, y=460)