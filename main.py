import pyautogui
from tkinter import Tk, StringVar, Entry, Menu, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image
import time

root = Tk()
root.title("Autostart")

time_settings = 5


def autostart():
    while True:
        original = Image.open(askopenfilename(filetypes=(("Images", "*.jpeg;*.jpg;*.png"),)))
        time.sleep(time_settings)
        try:
            x, y = pyautogui.locateCenterOnScreen(original)
            pyautogui.click(x, y)
        except Exception:
            continue


def time_waiting():
    data = message.get()
    time_settings = int(data)
    return time_settings


def info():
    messagebox.showinfo("Інформація", """Ця програма зробить автоматичне натискання по потрібній вам іконці, яку ви оберете.
    1) Вказуйте час очікування в секундах у полі (за дефолту 5 сек).
    2) Вказуєте зображення (.jpeg .jpg .png).
    3) Перемикаєтесь на потрібну вкладку.
    4) Програма робить клик.""")


message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

main_menu = Menu()
main_menu.add_cascade(label="Старт", command=autostart)
main_menu.add_cascade(label="Час", command=time_waiting)
main_menu.add_cascade(label="Інформація", command=info)
root.config(menu=main_menu)

root.mainloop()
