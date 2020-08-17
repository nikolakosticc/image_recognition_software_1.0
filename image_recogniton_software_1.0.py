import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL
import os
import time


#Set up the program

root = tkinter.Tk()
root.title("Image Recognition Software")
root.geometry("1400x600")
root.resizable(width=False, height=False)
root.configure(bg="#fff")


#Set temporary None value

Image_Name_Label = None
DDMS_Label = None
Time_elapsed_Label = None
my_image_label = None
Image_Dimensions_Label = None
Image_Size_Label = None


#Functions

def close_window():
    response = messagebox.askquestion("Exit the Program", "Do you really want to exit the program?")
    if response == 'yes':
        root.destroy()
    else:
        pass


def show_info():
    global my_image
    global DDMS_Label
    global Time_elapsed_Label
    global my_image_label
    global Image_Dimensions_Label
    global Image_Size_Label
    start_time = time.time()

    fileName = filedialog.askopenfilename(filetypes = (("png files", "*.png"), ("All Files", "*.*")))
    Image_Name_Label = Label(root, text="", font=("Calibri", 13), fg="#000", bg="#fff")
    Image_Name_Label.place(x=610, y=193)
    Image_Name_Label.configure(text = fileName)


    #DDSM Label

    DDMS_Label = Label(root, text="DDSM", font=("Calibri", 13), bg="#fff")
    DDMS_Label.place(x=610, y=163)


    #Time elapsed Label

    Time_elapsed = time.time() - start_time, "seconds"
    Time_elapsed_Label = Label(root, text=(Time_elapsed), font=("Calibri", 13), fg="#000", bg="#fff")
    Time_elapsed_Label.place(x=610, y=283)


    #Image

    size = 128, 128

    my_image = ImageTk.PhotoImage(Image.open(fileName))
    my_image_label = Label(image=my_image)
    my_image_label.place(x=58, y=77)


    #Image Dimensions Label

    image_dimensions = PIL.Image.open(fileName)
    image_dimensions_raw = str(image_dimensions.size[0]) + " x " + str(image_dimensions.size[1]) + " pixels"

    Image_Dimensions_Label = Label(root, text="", font=("Calibri", 13), fg="#000", bg="#fff")
    Image_Dimensions_Label.place(x=610, y=223)
    Image_Dimensions_Label.configure(text = image_dimensions_raw)


    #Image Size Label

    Image_Size_KB = float(os.stat(fileName).st_size)
    Image_Size_MB = Image_Size_KB / 1048576, "MB(s)"

    Image_Size_Label = Label(root, text="", font=("Calibri", 13), fg="#000", bg="#fff")
    Image_Size_Label.place(x=610, y=252)
    Image_Size_Label.configure(text = Image_Size_MB)



def clear():
    global Image_Name_Label
    global DDMS_Label
    global Time_elapsed_Label
    global my_image_label
    global Image_Dimensions_Label
    global Image_Size_Label
    DDMS_Label.destroy()
    Time_elapsed_Label.destroy()
    #Image_Name_Label.destroy()
    my_image_label.destroy()
    Image_Dimensions_Label.destroy()
    Image_Size_Label.destroy()


#Intro Label

MRS_Project_Label = Label(root, text="MRS Project", font=("Calibri", 20), bg="#fff")
MRS_Project_Label.place(x=630, y=60)


#Other Labels

Image_Source_Label = Label(root, text="Image Soruce : ", font=("Calibri bold", 15), bg="#fff")
Image_Source_Label.place(x=480, y=160)

Image_Name_Labell = Label(root, text="Image Name : ", font=("Calibri bold", 15), bg="#fff")
Image_Name_Labell.place(x=480, y=190)

Image_Dimensions_Label_Text = Label(root, text="Dimensions : ", font=("Calibri bold", 15), bg="#fff")
Image_Dimensions_Label_Text.place(x=480, y=220)

Image_Size_Label_Text = Label(root, text="Size : ", font=("Calibri bold", 15), bg="#fff")
Image_Size_Label_Text.place(x=480, y=250)

Time_elapsed_Label_Text = Label(root, text="Time elapsed : ", font=("Calibri bold", 15), bg="#fff")
Time_elapsed_Label_Text.place(x=480, y=280)


#Logo

img = ImageTk.PhotoImage(Image.open("Logo.png"))
panel = Label(root, image = img)
panel.place(x=1200, y=20)


#Buttons

Image_Label = Label(root, text="Image", font=("Calibri", 15), width=37, height=16, fg="#fff", bg="#1a68c7")
Image_Label.place(x=52, y=65)

Selected_Image_Button = Button(root, text="Select Image", font=("Calibri", 15), width=15, fg="#fff", bg="#1a68c7", command=show_info)
Selected_Image_Button.place(x=422, y=500)

Clear_Button = Button(root, text="Clear", font=("Calibri", 15), width=15, fg="#fff", bg="#1a68c7", command=clear)
Clear_Button.place(x=622, y=500)

Exit_Button = Button(root, text="Exit", font=("Calibri", 15), width=15, fg="#fff", bg="#1a68c7", command=close_window)
Exit_Button.place(x=822, y=500)


#Root Mainloop

root.mainloop()
