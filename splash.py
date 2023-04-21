from tkinter import*
from PIL import ImageTk,Image
import os


splash_root = Tk()
image1 = Image.open("C:/Users/kruna/Desktop/SSIP/Implementation/Logo.jpg")
resize_image = image1.resize((450, 450))
test = ImageTk.PhotoImage(resize_image)

# Hide the title bar
# splash_root.overrideredirect(True)
splash_root.title("OCR baesd Marks Extractor")
splash_root.geometry("1920x1080")
splash_root.configure(background = "#FFFFFF")


splash_label = Label(splash_root, text="OCR based Marks Extractor", font=("Helvetica", 36), image=test)
splash_label.image=test
splash_label.place(relx=0.5, rely=0.5, anchor=CENTER)
# splash_label.pack(pady=60, padx=70)


def main_window():
	splash_root.destroy()
		

def open_new():
	os.startfile("C:/Users/kruna/Desktop/SSIP/Implementation/home.py")

# Splash Screen Timer
splash_root.after(2000, open_new)
splash_root.after(2000, main_window)

mainloop()
