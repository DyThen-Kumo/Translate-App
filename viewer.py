from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import googletrans

## Use print(googletrans.LANGUAGES) to see more language supported (in another program) or run file language.py.
dic = {'Vietnamese':'vi', 'English':'en', 'Japanese':'ja'}
trans = googletrans.Translator()

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
lang_in = ttk.Combobox(root, values=["Vietnamese", "English", "Japanese"], background="#FEEBE7", width=12)
lang_in.place(relx=0.3, y=75, anchor='center')
lang_in.set('Vietnamese')
lang_out = ttk.Combobox(root, values=["Vietnamese", "English", "Japanese"], background="#FEEBE7", width=12)
lang_out.place(relx=0.7, y=75, anchor='center')
lang_out.set('English')

## Input
box_in = Text(root, width=250, height=7, font=('Arial',15), background='#FEEBE7')
box_in.pack(padx=50, pady=30)

## Button bellow
button_frame = Frame(root).pack(side='bottom')
def clear():
    box_in.delete(1.0,END)
    box_out.delete(1.0,END)

def translate():
    box_out.delete(1.0,END)
    input = box_in.get(1.0, END)
    temp = trans.translate(input, src=dic[lang_in.get()], dest=dic[lang_out.get()])
    output = temp.text
    box_out.insert(END, output)

clear_button = Button(button_frame, text='CLEAR', font=('ROBOTO',10), bg='#030303', fg='#FFFFFF', command=clear)
clear_button.place(relx=0.6, y=300, anchor='center')
trans_button = Button(button_frame, text='TRANSLATE', font=('ROBOTO',10), bg='#030303', fg='#FFFFFF',command=translate)
trans_button.place(relx=0.4, y=300, anchor='center')

## Output
box_out = Text(root, width=250, height=7, font=('Arial',15), background="#FEEBE7")
box_out.pack(padx=50, pady=50)

## Focus
focus = Label(root, text="*App will take a few seconds.", fg="#000000", bd=0, background="#FEEBE7")
focus.config(font=('Courier',8,'italic'))
focus.pack(pady=10)

root.mainloop()