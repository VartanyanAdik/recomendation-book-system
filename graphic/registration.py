from tkinter import *
from tkinter import messagebox

root=Tk() #создаем окно
root.title('Авторизация')# Заголовок окна
root.geometry('900x700')# Размеры окна
root.resizable(width=FALSE, height=FALSE)# Если надо будет ограничить растяжение.
root['bg']='gold'# цвет окна внутри
image=PhotoImage(file="../resurs/image/book.png")
label=Label(root, image=image)
label.place(x=0, y=0)

def registration():
    text=Label(root, text='Для входа в систему-зарегистритуйтесь!', font='Arial 30', bg='gold', fg='black')
    text.place(x=70, y=0)
    text_firstname=Label(text='Введите ваше имя:', font='Arial 18', bg='gold', fg='black')
    text_firstname.place(x=350, y=60)
    register_lodin = Entry()
    register_lodin.place(x=400, y=100)
    text_lastname=Label(text='Введите вашу фамилию:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_lastname.place(x=290, y=145)
    register_lodin = Entry()
    register_lodin.place(x=400, y=185)
    text_patronymic = Label(text='Введите ваше отчество:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_patronymic.place(x=295, y=230)
    register_lodin = Entry()
    register_lodin.place(x=400, y=270)
    text_log = Label(text='Введите логин ниже:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_log.place(x=320, y=315)
    register_log = Entry()
    register_log.place(x=400, y=355)
    text_password = Label(text='Придумайте пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_password.place(x=320, y=400)
    register_password = Entry()
    register_password.place(x=400, y=440)
    text_repeatpassword = Label(text='Повторите пароль:', font='Arial 18', bg='gold', fg='black', padx=30)
    text_repeatpassword.place(x=328, y=485)
    register_repeatpassword = Entry(show='*')
    register_repeatpassword.place(x=400, y=525)
    button_register=Button(text='Зарегистрироваться!', bg='gold', font='Arial 13')
    button_register.place(x=370, y=565)





registration()


root.mainloop()

