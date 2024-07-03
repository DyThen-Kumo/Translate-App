from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import googletrans

## Get all languages which is supported
languages_origin = googletrans.LANGUAGES
languages_value = list(languages_origin.values())
languages = dict() # Swap key, value
for key, value in languages_origin.items():
    languages[value] = key

## Translator
trans = googletrans.Translator()
## ORC Predict
# Khởi tạo mô hình và processor từ Hugging Face
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

def clear(box_in, box_out):
    box_in.delete(1.0,END)
    box_out.delete(1.0,END)

def translate(box_in, box_out, lang_in, lang_out):
    box_out.delete(1.0,END)
    input = box_in.get(1.0, END)
    temp = trans.translate(input, src=lang_in, dest=lang_out)
    output = temp.text
    box_out.insert(END, output)

def upload_image(box_in):
    # Mở hộp thoại chọn tệp và lấy đường dẫn tệp
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if file_path:
        # Mở ảnh bằng PIL        
        img = Image.open(file_path).convert("RGB")       
        # Nhận dạng văn bản
        pixel_values = processor(images=img, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        recognized_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # # Chuyển đổi ảnh để sử dụng trong Tkinter
        # img_tk = ImageTk.PhotoImage(img)
        
        box_in.delete('1.0', END)  # Xóa nội dung hiện tại trong box_in
        box_in.insert(END, recognized_text)  # Chèn string tệp ảnh vào box_in
        # # Tạo hoặc cập nhật Label để hiển thị ảnh
        # if label.img:
        #     label.config(image=img_tk)
        #     label.img = img_tk  # Giữ tham chiếu đến đối tượng ảnh để ngăn bị thu hồi bộ nhớ
        # else:
        #     label.img = img_tk
        #     label.config(image=img_tk)