import tkinter as tk
from tkinter import *
from tkinter import messagebox
from stra import stranica
from crypto.cipher import password_encryption
from database.db import save_database, database_dict, check_user
from entity.user import User
import re
import string


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
    window2['bg'] = 'gold'
    window2.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
    text = Label(window2, text='Добро пожаловать!', font='Arial 30', bg='gold', fg='black')
    text.place(x=280, y=20)
    text_login = Label(window2, text='Введите логин:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_login.place(x=350, y=230)
    authorization_login_entry = Entry(window2)
    authorization_login_entry.place(x=400, y=270)
    authorization_password = Label(window2, text='Введите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    authorization_password.place(x=340, y=315)
    authorization_password_entry = Entry(window2, show='*')
    authorization_password_entry.place(x=400, y=355)
    button_input = Button(window2, text='Войти', bg='gold', font='Arial 13', command=lambda: bulk())
    button_input.place(x=432, y=400)
    button_forgot = Button(window2, text='Забыли пароль?', bg='gold', font='Arial 13')
    button_forgot.place(x=392, y=460)

    def bulk():
        if check_user(authorization_login_entry.get(), authorization_password_entry.get()):
            window2.destroy()
            stranica()
        else:
            messagebox.showerror("Error", "Wrong login or password!")


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
    text_repeat_password = Label(text='Повторите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_repeat_password.place(x=328, y=485)
    entry_repeat_password = Entry(show='*')
    entry_repeat_password.place(x=400, y=525)
    button_register = Button(text='Зарегистрироваться!', bg='gold', font='Arial 13', command=lambda: validate())
    button_register.place(x=370, y=565)
    button1 = tk.Button(text="Уже есть аккаунт!", bg='gold', font='Arial 13', command=click_button)
    button1.place(x=385, y=610)
    def validate():
        while True:
            validate_firstname = entry_firstname.get()
            if len(validate_firstname) < 1:
                messagebox.showerror("Ошибка", "Слишком короткое имя")
                break
            if not re.search('^[A-Z, a-z]*$', validate_firstname):
                messagebox.showerror("Ошибка", "Имя должно содержать только английские буквы!")
                break
            if re.search('[0-9]', validate_firstname):
                messagebox.showerror("Ошибка", "Имя не должно содержать цифры!")
                break
            if re.search('[A-Z]', validate_firstname[0:1]) is None:
                messagebox.showerror("Ошибка", "Имя должно начинаться с большой буквы!")
                break
            validate_lastname = entry_lastname.get()
            if len(validate_lastname) < 1:
                messagebox.showerror("Ошибка", "Слишком короткая фамилия")
                break
            if not re.search("^[A-Z, a-z]*$", validate_lastname):
                messagebox.showerror("Ошибка", "Фамилия должна содержать только английские буквы!")
                break
            if re.search('[0-9]', validate_lastname):
                messagebox.showerror("Ошибка", "Фамилия не должна содержать цифры!")
                break
            if re.search('[A-Z]', validate_lastname[0:1]) is None:
                messagebox.showerror("Ошибка", "Фамилия должна начинаться с большой буквы!")
                break
            validate_patronymic = entry_patronymic.get()
            if len(validate_patronymic) < 1:
                messagebox.showerror("Ошибка", "Слишком короткое отчество")
                break
            if not re.search("^[A-Z, a-z]*$", validate_patronymic):
                messagebox.showerror("Ошибка", "Отчество должно содержать только английские буквы!")
                break
            if re.search('[0-9]', validate_patronymic):
                messagebox.showerror("Ошибка", "Отчество не должно содержать цифры!")
                break
            if re.search('[A-Z]', validate_patronymic[0:1]) is None:
                messagebox.showerror("Ошибка", "Отчество должно начинаться с большой буквы!")
                break
            validate_login = entry_login.get()
            if len(validate_login) < 6:
                messagebox.showerror("Ошибка", "Логин должен содержать не менее 6 символов!")
                break
            if not re.search('[0-9]', validate_login):
                messagebox.showerror("Ошибка", "Логин должен содержать минимум 1 цифру!")
                break
            validate_password = entry_password.get()
            validate_password_repeat = entry_repeat_password.get()
            if len(validate_password) < 8:
                messagebox.showerror("Ошибка", "Пароль должен содержать не менее 8 символов!")
                break
            if validate_password != validate_password_repeat:
                messagebox.showerror("Ошибка", "Пароли должны совпадать!")
                break
            else:
                log_pass()
                messagebox.showinfo("Успешно", "Вы успешно зарегистрировались!")
                break
    def log_pass():
        if entry_password.get() == entry_repeat_password.get():
            firstname = entry_firstname.get()
            lastname = entry_lastname.get()
            patronymic = entry_patronymic.get()
            login = entry_login.get()
            password = entry_password.get()
            cipher_password = password_encryption(password)
            per = User(firstname, lastname, patronymic, login, cipher_password)
            save_database(per)




    tk.mainloop()


register()
