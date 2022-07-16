from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import pyttsx3
import PyPDF2
import createacc

def main():
 class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Here")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        
        self.bg=ImageTk.PhotoImage(file="images/login/login bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        fr=Frame(self.root,highlightbackground='black',highlightthickness='3')
        fr.place(x=280,y=25,width=810,height=260)
        self.frbg=ImageTk.PhotoImage(file="images/login/label.png")
        frbg=Label(fr,image=self.frbg).place(x=0,y=0,width=800,height=230)

       
        frame1=Frame(self.root,bg='white',highlightbackground='black',highlightthickness='3')
        frame1.place(x=280,y=260,width=810,height=610)
        self.frame=ImageTk.PhotoImage(file="images/login/framebg.png")
        frame=Label(frame1,image=self.frame).place(x=0,y=0,width=800,height=600)

        username=Label(frame1,text="Username",font=("Forte",20,"bold"),bg="light grey",fg="black").place(x=400,y=100)
        self.txt_username=Entry(frame1,font=("Forte",18),highlightbackground='black',highlightthickness='1')
        self.txt_username.place(x=560,y=100,width=220)
         
        password=Label(frame1,text="Password",font=("Forte",20,"bold"),bg="light grey",fg="black").place(x=400,y=200)
        self.txt_password=Entry(frame1,font=("Forte",18),highlightbackground='black',highlightthickness='1')
        self.txt_password.place(x=560,y=200,width=220)
         
        login=Button(frame1,text="LOGIN",cursor="hand2",bg="black",fg="white",font=("britannic bold",18,"bold"),command=self.verify).place(x=500,y=270)
        
        reglabel=Label(frame1,text="Dont have an account? \nCreate one!",font=("Forte",18,"bold"),bg="light grey",fg="dark red").place(x=430,y=420)
        register=Button(frame1,text="REGISTER",cursor="hand2",bg="black",fg="white",font=("britannic bold",18,"bold"),command=self.reg).place(x=480,y=500)
        
    def reg(self):
        self.root.destroy()
        createacc.main()
        
    def verify(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                 con=pymysql.connect(host="localhost",user="root",password="nidhid1601",database="audiobook")
                 cue=con.cursor()
                 cue.execute("select * from customer where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get()))
                 row=cue.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
                 else:
                     messagebox.showinfo("Success",("Welcome "+self.txt_username.get()+", Lets Read Books!"),parent=self.root)
                     self.root.destroy()
                     import home
                     home.main()
                 con.close()
                 
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
   
         
 root=Tk()
 obj=Login(root)
 root.mainloop()

if __name__=="__main__":
    main()