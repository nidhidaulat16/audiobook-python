from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import pyttsx3
import PyPDF2
import ebook1
import ebook2
import ebook3


def main():
 class Slide_home:
    def __init__(self,root):
        self.root=root
        self.root.title("E-Book")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        
        self.bg=ImageTk.PhotoImage(file="images/ebook_home/ebook bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        title=Label(text='E  -  B O O K',font=("britannic bold",44,"bold"),bg="white",fg="black").place(x=470,y=45)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(image=self.backbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=50,y=20)
        
        self.slide1img=ImageTk.PhotoImage(file="images/ebook_home/ebook1.png")
        slide1btn=Button(image=self.slide1img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.ebk1).place(x=160,y=200,height=310,width=200)
        s1=Label(text='A Little\nJourney',font=("britannic bold",28,"bold"),bg="white",fg="black").place(x=160,y=550)
        
        self.slide2img=ImageTk.PhotoImage(file="images/ebook_home/ebook2.png")
        slide2btn=Button(image=self.slide2img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.ebk2).place(x=515,y=200,height=310,width=200)
        s2=Label(text='The Story\nOf An\nHour',font=("britannic bold",28,"bold"),bg="white",fg="black").place(x=510,y=550)
        
        self.slide3img=ImageTk.PhotoImage(file="images/ebook_home/ebook3.png")
        slide3btn=Button(image=self.slide3img,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.ebk3).place(x=870,y=200,height=310,width=200)
        s3=Label(text='Youth',font=("britannic bold",28,"bold"),bg="white",fg="black").place(x=900,y=550)    
    
    def ebk1(self):
        self.root.destroy()
        ebook1.main()

    def ebk2(self):
        self.root.destroy()
        ebook2.main()

    def ebk3(self):
        self.root.destroy()
        ebook3.main()
    
    def back(self):
        self.root.destroy()
        import home
        home.main()
 root=Tk()
 obj=Slide_home(root)
 root.mainloop()

if __name__=="__main__":
    main()