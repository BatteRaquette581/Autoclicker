from pynput.mouse import Controller
from pynput.mouse import Button as button
from keyboard import is_pressed
from time import sleep
from tkinter import *
tk = Tk()
bg = "#46615F"
tk["bg"] = bg
tk.geometry("700x700")
tk.minsize(700, 700)
tk.maxsize(700, 700)
tk.title("Autoclicker")
cps = 0
mouse = Controller()


def click():
    mouse.press(button.left)
    sleep(0.5 / cps)
    mouse.release(button.left)
    sleep(0.5 / cps)


can_click = False
autoclick = False


def _autoclicker():
    global autoclick
    global can_click
    while autoclick:
        if can_click:
            click()
        if is_pressed("alt+a"):
            can_click = not can_click
            while is_pressed("alt+a"):
                continue
        if is_pressed("alt+q"):
            autoclick = False


def fetch_cps(widget):
    global cps
    cps = int(widget.get("1.0", "end-1c"))


def autoclicker(widget):
    global autoclick
    global can_click
    autoclick = True
    can_click = False
    fetch_cps(widget)
    _autoclicker()


def stop_autoclick():
    global autoclick
    autoclick = False


info_content = (
    "Alt+A to start/stop the autoclicker. (when initialized)",
    "Alt+Q to uninitialize the autoclicker. (when initialized)"
)
info = Label(
    tk,
    text="\n".join(info_content),
    font=("Arial", 16)
)
info["bg"] = bg
cps_label = Label(
    tk,
    text="CPS: ",
    font=("Arial", 16)
)
cps_label["bg"] = bg
cps_box = Text(
    tk,
    width=5,
    height=2,
    font=("Arial", 16),
)
start = Button(
    tk,
    text="Initialize Autoclicker",
    font=("Arial", 16),
    command=lambda: autoclicker(cps_box)
)
info.pack()
cps_label.pack()
cps_box.pack()
start.pack()
tk.mainloop()
