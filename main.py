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
    messagebox.showinfo("Info", """"This program will automatically click on the selected icon of your choice.
                        1) Specify the waiting time in seconds (default is 5 seconds).
                        2) Select an image (.jpeg, .jpg, .png).
                        3) Switch to the desired tab.
                        4) The program will perform a click."**""")


message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="center")

main_menu = Menu()
main_menu.add_cascade(label="Start", command=autostart)
main_menu.add_cascade(label="Time", command=time_waiting)
main_menu.add_cascade(label="Info", command=info)
root.config(menu=main_menu)

root.mainloop()
