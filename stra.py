import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd



def profile_window(): #функция для личного профиля
    home = tk.Tk() # создание домашней страницы личного профиля
    home.title("Добро пожаловать!")
    home.geometry("900x700")
    home.resizable(width=FALSE, height=FALSE)
    home['bg'] = 'white'
    image = PhotoImage(
        file=r"/home/arkadi/PycharmProjects/recomendation-book-system/resource/image/perepis.png")
    user_avatar = Label(home, image=image) #место аватарки для пользователя
    user_avatar.place(x=20, y=20)
    button_input = Button(home, text='Выбрать фотку', bg='gold', font='Arial 9')#, command=lambda: #open_file())
    button_input.place(x=75, y=280)
    avatar_name = Label(home, text='Возраст', font='Arial 18', bg='gold', fg='black', padx=30)
    avatar_name.place(x=300, y=30)
    text_login = Label(home, text='Введенное имя', font='Arial 18', bg='gold', fg='black', padx=30)
    text_login.place(x=300, y=100)
    button_input1 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input1.place(x=300, y=200)
    button_input2 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input2.place(x=300, y=250)
    button_input2 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input2.place(x=300, y=300)
    button_input4 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input4.place(x=550, y=200)
    button_input4 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input4.place(x=550, y=250)
    button_input6 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=1)
    button_input6.place(x=550, y=300)
    button_forgot = Button(home, text='Подобрать книги', bg='gold', font='Arial 18')
    button_forgot.place(x=420, y=350)
    # list_for_image = []#создание ссылки для фотографии

    # def open_file():
    #     filetypes = (("Изображение", "*.png"),)#задаем формат
    #     my_file = fd.askopenfilename(title="Открыть файл", filetypes=filetypes)#открываем файл для чтения
    #     for m in my_file:#копируем выбранный файл
    #         shutil.copyfile(my_file,
    #                         r"/home/arkadi/PycharmProjects/recomendation-book-system/resource/image/перепись.png")
    #         break
    #     image_path = r"/home/arkadi/PycharmProjects/recomendation-book-system/resource/image/перепись.png"
    #     img = Image.open(image_path)
    #     new_image = img.resize((250, 250))#задаем размеры
    #     new_image.save(
    #         r"/home/arkadi/PycharmProjects/recomendation-book-system/resource/image/перепись.png")
    #     user_avatar.destroy()#удаляем прошлую фотку
    #     imagea = PhotoImage(
    #         file=r"/home/arkadi/PycharmProjects/recomendation-book-system/resource/image/перепись.png")
    #     list_for_image.append(imagea)
    #     avatara = Label(home, image=imagea)
    #     avatara.place(x=20, y=20)

    home.mainloop()

profile_window()