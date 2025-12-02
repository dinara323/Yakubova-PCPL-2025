from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
import time
import calendar
import datetime
import requests
import tkinter as tk
from pprint import pprint
from config import open_weather_token


a2 = Tk()
a2.title("Окно")
a2.geometry('400x250')
a2["bg"] = "#f7e9c6"


lbl = Label(a2, text="Электронный органайзер", font=("Caveas", 15), bg="#f7e9c6", fg="#702963")
lbl.grid(padx=82, pady=20)




def okno():
   root = Tk()
   root.title("Calculator")


   bttn_list = [
       "7", "8", "9", "+", "*",
       "4", "5", "6", "-", "/",
       "1", "2", "3", "=", "xⁿ",
       ".", "0", "±", "n!",
       "√2", "π", "sin", "cos",
       "(", ")", "С", "Exit",
   ]


   r = 1
   c = 0
   for i in bttn_list:
       rel = ""
       cmd = lambda x=i: calc(x)
       ttk.Button(root, text='\n' + i + '\n', command=cmd, width=10).grid(row=r, column=c)
       c += 1
       if c > 4:
           c = 0
           r += 1


   calc_entry = Entry(root, width=55)
   calc_entry.grid(row=0, column=0, columnspan=5)


   def calc(key):
       global memory
       if key == "=":
           str1 = "-+0123456789.*/)("
           if calc_entry.get()[0] not in str1:
               calc_entry.insert(END, "Первый символ не является числом")
               messagebox.showerror("Ошибка", "Некорректный ввод")


           try:
               result = eval(calc_entry.get())
               calc_entry.insert(END, "=" + str(result))
           except:
               calc_entry.insert(END, "Error!")
               messagebox.showerror("Ошибка")


       # очищение поля ввода
       elif key == "С":
           calc_entry.delete(0, END)


       # обработка нажатий
       elif key == "±":
           if "=" in calc_entry.get():
               calc_entry.delete(0, END)
           try:
               if calc_entry.get()[0] == "-":
                   calc_entry.delete(0)
               else:
                   calc_entry.insert(0, "-")
           except IndexError:
               pass


       elif key == "π":
           calc_entry.insert(END, math.pi)


       elif key == "Exit":
           root.after(1, root.destroy)
           sys.exit


       elif key == "xⁿ":
           calc_entry.insert(END, "**")


       elif key == "sin":
           calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
       elif key == "cos":
           calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))


       elif key == "(":
           calc_entry.insert(END, "(")
       elif key == ")":
           calc_entry.insert(END, ")")


       elif key == "n!":
           calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))


       elif key == "√2":
           calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))


       else:
           if "=" in calc_entry.get():
               calc_entry.delete(0, END)
           calc_entry.insert(END, key)


   root.mainloop()




def click1():
   def tema(theme):
       text_fild["bg"] = a_colors[theme]["text_bg"]
       text_fild["fg"] = a_colors[theme]["text_fg"]
       text_fild["insertbackground"] = a_colors[theme]["cursor"]
       text_fild["selectbackground"] = a_colors[theme]["select_bg"]


   def a_fonts(fontss):
       text_fild["font"] = fonts[fontss]["font"]


   def exit():
       answer = messagebox.askokcancel("Выход", "Вы точно хотите выйти?")
       if answer:
           roott.destroy()


   def bmi():
       def calculate_bmi():
           kg = int(weight_tf.get())
           m = int(height_tf.get()) / 100
           bmi = kg / (m * m)
           bmi = round(bmi, 1)


           if bmi < 18.5:
               messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
           elif (bmi > 18.5) and (bmi < 24.9):
               messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
           elif (bmi > 24.9) and (bmi < 29.9):
               messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
           else:
               messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')


       window = Tk()
       window.title('Калькулятор индекса массы тела (ИМТ)')
       window.geometry('400x300')


       frame = Frame(
           window,
           padx=10,
           pady=10
       )
       frame.pack(expand=True)


       height_lb = Label(
           frame,
           text="Введите свой рост (в см)  "
       )
       height_lb.grid(row=3, column=1)


       weight_lb = Label(
           frame,
           text="Введите свой вес (в кг)  ",
       )
       weight_lb.grid(row=4, column=1)


       height_tf = Entry(
           frame,
       )
       height_tf.grid(row=3, column=2, pady=5)


       weight_tf = Entry(
           frame,
       )
       weight_tf.grid(row=4, column=2, pady=5)


       cal_btn = Button(frame, text='Рассчитать ИМТ', command=calculate_bmi)
       cal_btn.grid(row=5, column=2)


       window.mainloop()


   def a():
       global month, year


       def back():
           global month
           global year
           month -= 1
           if month == 0:
               month = 12
               year -= 1
           fill()


       def next():
           global month, year
           month += 1
           if month == 13:
               month = 1
               year += 1
           fill()


       def fill():
           info_label["text"] = calendar.month_name[month] + ", " + str(year)
           month_days = calendar.monthrange(year, month)[1]
           if month == 1:
               back_month_days = calendar.monthrange(year - 1, 12)[1]
           else:
               back_month_days = calendar.monthrange(year, month - 1)[1]
           week_day = calendar.monthrange(year, month)[0]


           for n in range(month_days):
               days[n + week_day]["text"] = n + 1
               days[n + week_day]["fg"] = "black"
               if year == now.year and month == now.month and n == now.day:
                   days[week_day]["bg"] = "#add6ff"
                   days[n + week_day]["bg"] = "#c5cce3"
               else:
                   days[n + week_day]["bg"] = "#c5cce3"


           for n in range(week_day):
               days[week_day - n - 1]["text"] = back_month_days - n
               days[week_day - n - 1]["fg"] = "#c5cce3"
               days[week_day - n - 1]["bg"] = "#f3f3f3"
           for n in range(6 * 7 - month_days - week_day):
               days[week_day + month_days + n]["text"] = n + 1
               days[week_day + month_days + n]["fg"] = "#c5cce3"
               days[week_day + month_days + n]["bg"] = "#f3f3f3"


       root6 = Tk()
       root6.title("Календарь")
       days = []
       now = datetime.datetime.now()
       year = now.year
       month = now.month


       back_button = Button(root6, text="<", command=back)
       back_button.grid(row=0, column=0, sticky=NSEW)
       next_button = Button(root6, text=">", command=next)
       next_button.grid(row=0, column=6, sticky=NSEW)
       info_label = Label(root6, text="0", width=1, height=1, font="Arial 16 bold", fg="blue")
       info_label.grid(row=0, column=1, columnspan=5, sticky=NSEW)


       for n in range(7):
           lbl = Label(root6, text=calendar.day_abbr[n], width=1, height=1, fg="darkblue")
           lbl.grid(row=1, column=n, sticky=NSEW)


       for row in range(6):
           for col in range(7):
               lbl = Label(root6, text="0", width=4, height=2)
               lbl.grid(row=row + 2, column=col, sticky=NSEW)
               days.append(lbl)
       fill()
       root6.mainloop()


   roott = Tk()
   roott.title("Текстовый редактор")
   main_menu = Menu(roott)
   # Файл
   file = Menu(main_menu, tearoff=0)
   file.add_command(label="Календарь", command=a)
   file.add_command(label="ИМТ", command=bmi)
   file.add_separator()
   file.add_command(label="Закрыть", command=exit)
   roott.config(menu=file)


   # Вид
   a = Menu(main_menu, tearoff=0)
   a_sub = Menu(a, tearoff=0)
   font_sub = Menu(a, tearoff=0)
   a_sub.add_command(label="Темная", command=lambda: tema("dark"))
   a_sub.add_command(label="Светлая", command=lambda: tema("light"))
   a.add_cascade(label="Тема", menu=a_sub)


   font_sub.add_command(label="Arial", command=lambda: a_fonts("Arial"))
   font_sub.add_command(label="Comic Sans MS", command=lambda: a_fonts("CSMS"))
   font_sub.add_command(label="Times New Roman", command=lambda: a_fonts("TNR"))
   a.add_cascade(label="Шрифт...", menu=font_sub)
   roott.config(menu=a)


   # Добавление пунктов меню"
   main_menu.add_cascade(label="Меню", menu=file)
   main_menu.add_cascade(label="Вид", menu=a)
   roott.config(menu=main_menu)


   f_text = Frame(roott)
   f_text.pack(fill=BOTH, expand=1)


   a_colors = {
       "dark": {
           "text_bg": "#979aaa", "text_fg": "blue", "cursor": "brown", "select_bg": "#59bce3"
       },
       "light": {
           "text_bg": "white", "text_fg": "#8b60a3", "cursor": "#A5A5A5", "select_bg": "#c5d0e6"
       }
   }


   fonts = {
       "Arial": {
           "font": "Arial 14 bold"
       },
       "CSMS": {
           "font": ("Comic Sans MS", 14, "bold")
       },
       "TNR": {
           "font": ("Times New Roman", 14, "bold")
       }


   }


   text_fild = Text(f_text, bg="#979aaa", fg="blue", padx=10, pady=10, wrap=WORD,
                    insertbackground="brown",
                    selectbackground="#59bce3",
                    width=80,
                    spacing3=10)
   text_fild.pack(expand=1, fill=BOTH, side=LEFT)
   scroll = Scrollbar(f_text, command=text_fild.yview)
   scroll.pack(side=LEFT, fill=Y)
   text_fild.config(yscrollcommand=scroll.set)


   roott.mainloop()




def clock():
   Cl = Tk()
   Cl.title("Digital Clock")
   Cl.geometry("202x90")
   Cl.resizable(1, 1)
   text_font = ("Boulder", 28, "bold")
   background = "#f7e9c6"
   foreground = "#02ab9d"
   border_width = 25
   label = Label(Cl, font=text_font, bg=background, fg=foreground, bd=border_width)
   label.grid(row=0, column=1)


   def digital_clock():
       time_live = time.strftime("%H:%M:%S")
       label.config(text=time_live)
       label.after(200, digital_clock)


   digital_clock()
   Cl.mainloop()






def pogodaa():
   root4 = tk.Tk()
   root4.title("Погода")
   root4.geometry("400x240")


   def getTextInput():
       city = textExample.get("1.0", "end")
       code_to_smile = {
           "Clear": "Ясно \U00002600",
           "Clouds": "Облачно \U00002601",
           "Rain": "Дождь \U00002614",
           "Drizzle": "Дождь \U00002614",
           "Thunderstorm": "Гроза \U000026A1",
           "Snow": "Снег \U0001F328",
           "Mist": "Туман \U0001F32B"
       }


       try:
           r = requests.get(
               f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
           )
           data = r.json()
           # pprint(data)


           city = data["name"]
           cur_weather = data["main"]["temp"]


           weather_description = data["weather"][0]["main"]
           if weather_description in code_to_smile:
               wd = code_to_smile[weather_description]
           else:
               wd = "Посмотри в окно, не пойму что там за погода"


           humidity = data["main"]["humidity"]
           wind = data["wind"]["speed"]
           sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
           sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])


           messagebox.showinfo(f'Погода в городе {city}', f"{city}\n"
                               f'Погода: {cur_weather}С° {wd}\n'
                               f"Влажность: {humidity}%\nВетер: {wind} м/с\n"
                               f"Восход солнца: {sunrise_timestamp}\n"
                               f"Закат солнца: {sunset_timestamp}\n"
                               f"Хорошего дня!"


                               )


           # print(f"Погода в городе: {city}\nТемпература: {cur_weather}С° {wd}\n"
           # f"Влажность: {humidity}%\nВетер: {wind} м/с\n"
           # f"Восход солнца: {sunrise_timestamp}\n"
           # f"Закат солнца: {sunset_timestamp}\n"
           # f"Хорошего дня!"


           # )


       except Exception as ex:
           # print(ex)
           messagebox.showinfo('Ошибка', f'Проверьте название города')
           # print("Проверьте название города")


   textExample = tk.Text(root4, height=10)
   textExample.pack()
   btnRead = tk.Button(root4, height=1, width=10, text="Узнать погоду",
                       command=getTextInput)


   btnRead.pack()


   root4.mainloop()










kn = Button(a2, text="Калькулятор", bg="#4BBE90", fg="blue", font=("Caveas", 12), command=lambda: okno())
kn.place(x=90, y=55)


kn2 = Button(a2, text="Блокнот", bg="#4BBE90", fg="blue", font=("Caveas", 12), height=1, width=10,
            command=lambda: click1())
kn2.place(x=215, y=55)


kn3 = Button(a2, text="Часы", bg="#4BBE90", fg="blue", font=("Caveas", 12), height=1, width=10, command=lambda: clock())
kn3.place(x=93, y=115)


kn4 = Button(a2, text="Погода", bg="#4BBE90", fg="blue", font=("Caveas", 12), height=1, width=10, command=lambda: pogodaa())
kn4.place(x=215, y=115)


a2.mainloop()