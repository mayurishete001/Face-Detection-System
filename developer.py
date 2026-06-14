from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI face recognition system")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg='white',fg="#480B61")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img_top=Image.open('developerimage.jpg')
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_label,bd=2,bg='white')
        main_frame.place(x=50,y=0,width=500,height=600)

        img1=Image.open('mayuriimg.jpeg')
        img1=img1.resize((200,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(main_frame,image=self.photoimg1)
        f_label.place(x=300,y=0,width=200,height=200)  
        
        dep_label=Label(main_frame,text="Hello my name is,Mayuri",font=("times new roman",20,"bold"),fg="Purple")
        dep_label.place(x=0,y=5)
        dep_label=Label(main_frame,text="I am python Developer",font=("times new roman",20,"bold"),fg="Fuchsia")
        dep_label.place(x=0,y=40)


        img2=Image.open('devpage.jpg')
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(main_frame,image=self.photoimg2)
        f_label.place(x=0,y=210,width=500,height=390)  
if __name__=='__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()               