from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def display():
    messagebox.showinfo("Yandex.Taxi profitability", x)


root = Tk()
root.title("Yandex.Taxi profitability")
root.geometry("300x250")
messagebox.showinfo("Yandex.Taxi profitability",
                    'Привет эта программа предназначена для высчитывания выгодности поездки на Yandex.Taxi')
km = simpledialog.askinteger("КМ", "Сколько км хочешь проехать?")
pricekm = simpledialog.askinteger("Цена КМ", "Сколько стоит 1 км?")
price = simpledialog.askinteger("Цена Подачи", "Сколько стоит подача?")

if km <= 2: km = 0
b = (km * pricekm) + price
if b > 35: x=w= ('Езжай на iTaxi, YT стоит-', b)
else: x=q=('Езжай на Yandex.taxi поездака будет стоить-',b)


message_button = Button(text="Посчитать", command=display)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
