from tkinter import * 
import customtkinter
import regex 
from PIL import Image, ImageTk
root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
#source code body will come in here
#geometry will decide the dimensions of the main widget
root.geometry("900x600")
# min/max size will determine min or max size of the widget
root.minsize(900, 600)
root.maxsize(900, 600)
# to add/edit the title we use
root.title("IssueMailer")
# to add a text we use label and then we pack the label
# welcome=Label(text="Welcome to IssueMailer",background="black",fg="white",padx=100,pady=100,font="garamond-regular 50",borderwidth=5,relief=SUNKEN)
# welcome.pack()
# PhotoImage is used to add required photos but you have to use label after PhotoImage
image = Image.open("second.png")
width, height = 1130, 750 
resized_image = image.resize((width, height), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)
label = Label(root, image=photo)
label.pack()

root.mainloop()