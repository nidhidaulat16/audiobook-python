from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import pyttsx3
import PyPDF2
import slidebook1
import slidebook2
import slidebook3

def main():
 class Slide_home:
    def __init__(self,root):
        self.root=root
        self.root.title("SlideBook")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        
        self.bg=ImageTk.PhotoImage(file="images/slide_home/slide_home.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        title=Label(text='S L I D E    B O O K',font=("britannic bold",44,"bold"),bg="black",fg="white").place(x=300,y=15)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(image=self.backbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=50,y=20)
        
        self.slide1img=ImageTk.PhotoImage(file="images/slide_home/slide1img.png")
        slide1btn=Button(image=self.slide1img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.slide1).place(x=100,y=150,height=440,width=280)
        s1=Label(text='Tenali Raman\nStories',font=("britannic bold",30,"bold"),bg="black",fg="white").place(x=80,y=620)
        
        self.slide2img=ImageTk.PhotoImage(file="images/slide_home/slide2img.png")
        slide2btn=Button(image=self.slide2img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.slide2).place(x=500,y=150,height=430,width=280)
        s2=Label(text='Akbar Birbal',font=("britannic bold",30,"bold"),bg="black",fg="white").place(x=500,y=620)
        
        self.slide3img=ImageTk.PhotoImage(file="images/slide_home/slide3img.png")
        slide3btn=Button(image=self.slide3img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.slide3).place(x=900,y=150,height=430,width=280)
        s3=Label(text='Panchatantra',font=("britannic bold",30,"bold"),bg="black",fg="white").place(x=900,y=620)    
    
    def slide1(self):
        self.root.destroy()
        slidebook1.main()
    
    def slide2(self):
        self.root.destroy()
        slidebook2.main()

    def slide3(self):
        self.root.destroy()
        slidebook3.main()
    
    def back(self):
        self.root.destroy()
        import home
        home.main()
 
 root=Tk()
 obj=Slide_home(root)
 root.mainloop()

if __name__=="__main__":
    main()