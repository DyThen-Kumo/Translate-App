from tkinter import *
from PIL import Image, ImageTk
import googletrans

trans = googletrans.Translator()

## Tạo TK window
root = Tk()
root.title("Translator by Kumo")
root.geometry("500x640")
root.iconbitmap(r"img+font\Kumo-circle.ico")

## Set background
background = Image.open(r"img+font\background.png")
render = ImageTk.PhotoImage(background)
img = Label(root, image=render)
img.place(x=0, y=0)

## Tittle
name = Label(root, text="KUMO TRANSLATE", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=('Courier',30,'bold'))
name.pack(pady=10)

## Input
box_in = Text(root, width=30, height=8, font=('ROBOTO',15))
box_in.pack(pady=20)

## Button bellow
button_frame = Frame(root).pack(side='bottom')
def clear():
    box_in.delete(1.0,END)
    box_out.delete(1.0,END)

def translate():
    input = box_in.get(1.0, END)
    temp = trans.translate(input, src="vi", dest="en")
    output = temp.text
    box_out.insert(END, output)

clear_button = Button(button_frame, text='CLEAR', font=('Arial',10), bg='#030303', fg='#FFFFFF', command=clear)
clear_button.place(x=300, y=300)
trans_button = Button(button_frame, text='TRANSLATE', font=('Arial',10), bg='#030303', fg='#FFFFFF',command=translate)
trans_button.place(x=120, y=300)

## Output
box_out = Text(root, width=30, height=8, font=('ROBOTO',15))
box_out.pack(pady=50)

## Focus
name = Label(root, text="*This app will translate Vietnamese to English.", fg="white", bd=0, bg="#03152D")
name.config(font=('Courier', 8, 'italic'))
name.pack()

root.mainloop()