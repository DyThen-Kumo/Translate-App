from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from controller import *

## TK window
root = Tk()
root.title("Kumo Translator")
root.geometry("500x640")
root.iconbitmap(r"img+font\Kumo-circle.ico")

## Set background
background = Image.open(r"img+font\background.jpg")
render = ImageTk.PhotoImage(background)
img = Label(root, image=render)
img.place(x=0, y=0)

## Tittle
name = Label(root, text="KUMO TRANSLATE", fg="#000000", bd=0, background="#FEEBE7")
name.config(font=('Courier',30,'bold'))
name.pack(padx=10, pady=10)

## Set language
lang_in = ttk.Combobox(root, values=languages_value, background="#FEEBE7", width=12)
lang_in.place(relx=0.3, y=75, anchor='center')
lang_in.set('english')
lang_out = ttk.Combobox(root, values=languages_value, background="#FEEBE7", width=12)
lang_out.place(relx=0.7, y=75, anchor='center')
lang_out.set('vietnamese')

## Input
box_in = Text(root, width=250, height=7, font=('Arial',15), background='#FEEBE7')
box_in.pack(padx=50, pady=30)

## Output
box_out = Text(root, width=250, height=7, font=('Arial',15), background="#FEEBE7")
box_out.pack(padx=50, pady=50)

## Button bellow
button_frame = Frame(root).pack(side='bottom')

upload_button = Button(button_frame, text='UPLOAD IMAGE', font=('ROBOTO',10), bg='#030303', fg='#FFFFFF')
upload_button.config(command=lambda: upload_image(box_in=box_in))
upload_button.place(relx=0.7, y=300, anchor='center')

clear_button = Button(button_frame, text='CLEAR', font=('ROBOTO',10), bg='#030303', fg='#FFFFFF')
clear_button.config(command=lambda: clear(box_in=box_in, box_out=box_out))
clear_button.place(relx=0.5, y=300, anchor='center')

trans_button = Button(button_frame, text='TRANSLATE', font=('ROBOTO',10), bg='#030303', fg='#FFFFFF')
trans_button.config(command= lambda: translate(box_in=box_in, box_out=box_out, lang_in=languages[lang_in.get()], lang_out=languages[lang_out.get()]))
trans_button.place(relx=0.3, y=300, anchor='center')


## Focus
focus = Label(root, text="*App will take a few seconds.", fg="#000000", bd=0, background="#FEEBE7")
focus.config(font=('Courier',8,'italic'))
focus.pack(pady=10)

root.mainloop()