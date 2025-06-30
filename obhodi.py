from os import startfile
import tkinter as tk
from tkinter import messagebox

class Main:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Obxodi")
        self.__root.geometry("350x350")
        self.__root.iconbitmap(r'icons\logo.ico')

        self.__render_grafics()

        self.__root.mainloop()

    def __render_grafics(self):
        self.__start_inter = tk.Frame(self.__root)


        self.__conn_status = tk.StringVar()
        self.__conn_status.set('Обход не включён!\nНажмите кнопку ниже чтобы его включить.')
        self.is_yt = tk.IntVar()


        self.__main_text = tk.Label(self.__root, text='Obhodi!', font='system 30')
        self.__conn_status_label = tk.Label(self.__root, textvariable=self.__conn_status, font='system', pady=10)
        self.__start_btn = tk.Button(self.__start_inter, text='Разблокиовать Discord', font='system 20', command=self.__activate)
        self.yt_check = tk.Checkbutton(self.__start_inter, text='Также разблокировать Youtube', font='system 10', variable=self.is_yt)



        self.__main_text.pack(side='top')
        self.__conn_status_label.pack(side='top')
        self.__start_inter.pack(side='top')
        self.__start_btn.pack(side='top')
        self.yt_check.pack(side='top')

    def start_ds(self):
        startfile(r'prog\discord.bat')

    def start_ds_yt(self):
        startfile(r'prog\discord_youtube.bat')

    def __activate(self):
        try:
            if self.is_yt.get() == 1:
                self.start_ds_yt()
                var = 'Youtube + Discord'
            else:
                self.start_ds()
                var = 'Discord'
            
            self.__conn_status.set('Выбран вариант:' + var + '\nЕсли вы хотите изменить вариант или иотключить\nобход, закройте приложение.')
            messagebox.showinfo('Успешно!', 'Вы выбрали вариант:' + var + '\nЕсли вы хотите изменить вариант или иотключить обход, закройте приложение.')

        except Exception as e:
            messagebox.showwarning('Произошла ошибка', e)



if __name__ == '__main__':
    obhodi = Main()