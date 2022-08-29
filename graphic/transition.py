import tkinter as tk
from tkinter import *

from database.Db import save_database
from entity.user import User

window = tk.Tk()
window.title("Регистрация")
window.geometry("900x700")
window.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
window['bg'] = 'gold'  # цвет окна внутри
image = PhotoImage(file="../resource/image/entry.png")
label = Label(window, image=image)
label.place(x=0, y=0)


def click_button():
    window.destroy()
    window2 = tk.Tk()
    window2.title("Авторизация")
    window2.geometry("900x700")
    window2.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
    text = Label(window2, text='Добро пожаловать!', font='Arial 30', bg='gold', fg='black')
    text.place(x=280, y=20)
    text_patronymic = Label(window2, text='Введите логин:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_patronymic.place(x=350, y=230)
    register_lodin = Entry(window2)
    register_lodin.place(x=400, y=270)
    text_log = Label(window2, text='Введите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_log.place(x=340, y=315)
    register_log = Entry(window2, show='*')
    register_log.place(x=400, y=355)
    button_register = Button(window2, text='Войти', bg='gold', font='Arial 13')
    button_register.place(x=432, y=400)
    button_register = Button(window2, text='Забыли пароль?', bg='gold', font='Arial 13')
    button_register.place(x=392, y=460)


def register():
    text = Label(window, text='Для входа в систему-зарегистритуйтесь!', font='Arial 30', bg='gold', fg='black')
    text.place(x=70, y=0)
    text_firstname = Label(window, text='Введите ваше имя:', font='Arial 18', bg='gold', fg='black')
    text_firstname.place(x=350, y=60)
    entry_firstname = Entry()
    entry_firstname.place(x=400, y=100)
    text_lastname = Label(window, text='Введите вашу фамилию:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_lastname.place(x=290, y=145)
    entry_lastname = Entry()
    entry_lastname.place(x=400, y=185)
    text_patronymic = Label(window, text='Введите ваше отчество:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_patronymic.place(x=295, y=230)
    entry_patronymic = Entry()
    entry_patronymic.place(x=400, y=270)
    text_log = Label(window, text='Введите логин ниже:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_log.place(x=320, y=315)
    entry_login = Entry()
    entry_login.place(x=400, y=355)
    text_password = Label(window, text='Придумайте пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_password.place(x=320, y=400)
    entry_password = Entry(show='*')
    entry_password.place(x=400, y=440)
    text_repeatpassword = Label(text='Повторите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_repeatpassword.place(x=328, y=485)
    entry_repeatpassword = Entry(show='*')
    entry_repeatpassword.place(x=400, y=525)
    button_register = Button(text='Зарегистрироваться!', bg='gold', font='Arial 13', command=lambda: log_pass())
    button_register.place(x=370, y=565)
    button1 = tk.Button(text="Уже есть аккаунт!", bg='gold', font='Arial 13', command=click_button)
    button1.place(x=385, y=610)

    def log_pass():
        if entry_password.get() == entry_repeatpassword.get():
            firstname = entry_firstname.get()
            lastname = entry_lastname.get()
            patronymic = entry_patronymic.get()
            login = entry_login.get()
            password = entry_password.get()
            per = User(firstname, lastname, patronymic, login, password)
            save_database(per)

    tk.mainloop()


register()
