from tkinter import *

root = Tk()  # создаем окно
root.title('Авторизация')  # Заголовок окна
root.geometry('900x700')  # Размеры окна
root.resizable(width=FALSE, height=FALSE)  # Если надо будет ограничить растяжение.
root['bg'] = 'gold'  # цвет окна внутри
image = PhotoImage(file="../resource/image/book.png")
label = Label(root, image=image)
label.place(x=0, y=0)

def registration():
    text = Label(root, text='Добро пожаловать!', font='Arial 30', bg='gold', fg='black')
    text.place(x=280, y=20)
    text_patronymic = Label(text='Введите логин:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_patronymic.place(x=350, y=230)
    register_lodin = Entry()
    register_lodin.place(x=400, y=270)
    text_log = Label(text='Введите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_log.place(x=340, y=315)
    register_log = Entry(show='*')
    register_log.place(x=400, y=355)
    button_register = Button(text='Войти', bg='gold', font='Arial 13')
    button_register.place(x=432, y=400)
    button_register = Button(text='Забыли пароль?', bg='gold', font='Arial 13')
    button_register.place(x=392, y=460)

registration()
root.mainloop()