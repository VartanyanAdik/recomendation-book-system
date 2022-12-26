import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog as fd, filedialog
from tkinter.filedialog import *
import fileinput
from PIL import Image



def avatar():
    home = tk.Tk()
    home.title("Добро пожаловать!")
    home.geometry("900x700")
    home.resizable(width=FALSE, height=FALSE)
    home['bg'] = 'white'
    button_forgot = Button(home, text='Подобрать книги', bg='gold', font='Arial 18')
    button_forgot.place(x=440, y=400)
    image = PhotoImage(
        file=r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image\Background.png")
    avatarka = Label(home, image=image)
    avatarka.place(x=20, y=20)
    button_input = Button(home, text='Выбрать фотку', bg='gold', font='Arial 9', command=lambda: open_file())
    button_input.place(x=75, y=160)
    avatar_name = Label(home, text='Возраст', font='Arial 18', bg='gold', fg='black', padx=30)
    avatar_name.place(x=240, y=30)
    text_login = Label(home, text='Введенное имя', font='Arial 18', bg='gold', fg='black', padx=30)
    text_login.place(x=240, y=100)
    button_input1 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input1.place(x=250, y=200)
    button_input2 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input2.place(x=250, y=300)
    button_input3 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input3.place(x=450, y=300)
    button_input4 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input4.place(x=650, y=300)
    button_input5 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input5.place(x=650, y=200)
    button_input6 = Button(home, text='Выберите жанр книги!', bg='gold', font='Arial 13', height=2)
    button_input6.place(x=450, y=200)
    l=[]


    def open_file():
        filetypes = (("Изображение", "*.png"),)
        my_file = fd.askopenfilename(title="Открыть файл", filetypes=filetypes)
        for m in my_file:
            shutil.copyfile(my_file, r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image\перепись.png.")
            break
        image_path = r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image\перепись.png."
        img = Image.open(image_path)
        new_image = img.resize((200, 385))
        new_image.save(r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image\перепись.png.")
        avatarka.destroy()
        imagea = PhotoImage(
            file=r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image\перепись.png.")
        l.append(imagea)
        avatara = Label(home, image=imagea)
        avatara.place(x=20, y=20)






    # def open_file():
    #     filepath = filedialog.askopenfile(initialdir=r"C:\\Users\\Arkady Vartanyan\\PycharmProjects\\Main",
    #                                           title="Open file okay?",
    #                                           filetypes=(("image", "*.png"),
    #                                                      ("all files", "*.*")))
    #     file = open(filepath)
    #     os.replace(filepath, r"C:\Users\Arkady Vartanyan\PycharmProjects\recomendation-book-system\resource\image")
    #     file.close()




    home.mainloop()
avatar()

