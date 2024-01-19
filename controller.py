from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import googletrans

## Get all languages which is supported
languages_origin = googletrans.LANGUAGES
languages_value = list(languages_origin.values())
languages = dict() # Swap key, value
for key, value in languages_origin.items():
    languages[value] = key

## Translator
trans = googletrans.Translator()

def clear(box_in, box_out):
    box_in.delete(1.0,END)
    box_out.delete(1.0,END)

def translate(box_in, box_out, lang_in, lang_out):
    box_out.delete(1.0,END)
    input = box_in.get(1.0, END)
    temp = trans.translate(input, src=lang_in, dest=lang_out)
    output = temp.text
    box_out.insert(END, output)