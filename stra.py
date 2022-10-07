import tkinter as tk
from tkinter import *
from tkinter import messagebox



def stranica():
    window1 = tk.Tk()
    window1.title("Регистрация")
    window1.geometry("900x700")
    window1.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
    window1['bg'] = 'gold'  # цвет окна внутри