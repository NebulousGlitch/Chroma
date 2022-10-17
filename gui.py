import tkinter as tk
from PIL import ImageTk, Image

labelVisible = False
root = tk.Tk()
image1 = Image.open("./assets/images/greenbackground.png")
test = ImageTk.PhotoImage(image1)

label = tk.Label(image=test, bg='white')

root.overrideredirect(True)
root.lift()
root.configure(background='white')
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")


def activate_mic_indicator():
    global labelVisible
    if not labelVisible:
        label.pack()
        labelVisible = True
    else:
        label.pack_forget()
        labelVisible = False


class GUI:

    def initialize(self):
        root.mainloop()
