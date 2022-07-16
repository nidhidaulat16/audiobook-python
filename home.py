from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import pyttsx3
import PyPDF2
import slide_home
import ebook_home
import pbook
import dbook
import slidebook1
import slidebook2
import slidebook3
import ebook1
import ebook2
import ebook3
import login

def main():
 class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        self.bg=ImageTk.PhotoImage(file="images/home/home bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(text='H O M E   P A G E',font=("britannic bold",44,"bold"),bg="white",fg="dark blue").place(x=350,y=15)
        tag=Label(text='Choose your way of reading!',font=("britannic bold",32,"bold"),bg="white",fg="dark red").place(x=300,y=200)
        
        self.logoutimg=ImageTk.PhotoImage(file="images/icons/logout bt.png")
        logoutbtn=Button(image=self.logoutimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.logout).place(x=80,y=20)
        logoutlb=Label(text='LOGOUT',font=("britannic bold",22,"bold"),bg="white",fg="black").place(x=40,y=90)
        
        
        self.slideimg=ImageTk.PhotoImage(file="images/home/slide bt.png")
        slidebtn=Button(image=self.slideimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.slidebook).place(x=300,y=300,height=150,width=230)
        slidelb=Label(text='Slide Book',font=("britannic bold",22,"bold"),bg="white",fg="black").place(x=90,y=330)
        
        self.ebookimg=ImageTk.PhotoImage(file="images/home/ebook bt.png")
        ebookbtn=Button(image=self.ebookimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.ebook).place(x=900,y=300,height=180,width=240)
        ebooklb=Label(text='E-Book',font=("britannic bold",22,"bold"),bg="white",fg="black").place(x=740,y=350)    
    
        self.pbookimg=ImageTk.PhotoImage(file="images/home/pbook bt.png")
        pbookbtn=Button(image=self.pbookimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.pbook).place(x=300,y=540,height=200,width=170)
        pbooklb=Label(text='Pronunciation\nBook',font=("britannic bold",22,"bold"),bg="white",fg="black").place(x=35,y=570)    
    
        self.dbookimg=ImageTk.PhotoImage(file="images/home/dbook bt.png")
        dbookbtn=Button(image=self.dbookimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.dbook).place(x=900,y=540,height=200,width=170)
        dbooklb=Label(text='Talking\nDictionary',font=("britannic bold",22,"bold"),bg="white",fg="black").place(x=700,y=620)    
    
    def logout(self):
        res = messagebox.askyesno('Confirm', 'Do you want to exit?')
        if res == True:
           self.root.destroy()
           login.main()
        else:
           pass

    def slidebook(self):
        self.root.destroy()
        slide_home.main()
    def ebook(self):
        self.root.destroy()
        ebook_home.main()
    def pbook(self):
        self.root.destroy()
        pbook.main()
    def dbook(self):
        self.root.destroy()
        dbook.main()

 root=Tk()
 obj=Home(root)
 root.mainloop()

if __name__=="__main__":
    main()