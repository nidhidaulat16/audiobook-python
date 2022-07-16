from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

def main():
 class Createacc:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        
        root.state('zoomed')
        self.bg=ImageTk.PhotoImage(file="images/createacc/register_bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="images/createacc/register_frame1.jpeg")
        left=Label(self.root,image=self.left).place(x=15,y=50,width=720,height=750)
        
        #frame1
        frame1=Frame(self.root,bg='white')
        frame1.place(x=500,y=100,width=760,height=650)

        self.right=ImageTk.PhotoImage(file="images/createacc/register_frame2.jpeg")
        right=Label(frame1,image=self.right).place(x=0,y=0,width=790,height=650)

        title=Label(frame1,text='Create Your Account Here!',font=("britannic bold",28,"bold"),bg="white",fg="crimson").place(x=50,y=25)

        fnamelb=Label(frame1,text="First Name",font=("Forte",20),bg='white',fg="maroon").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_fname.place(x=50,y=135,width=200)
        
        mnamelb=Label(frame1,text="Middle Name",font=("Forte",20),bg="white",fg="maroon").place(x=300,y=100)
        self.txt_mname=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_mname.place(x=300,y=135,width=200)
        
        lnamelb=Label(frame1,text="Last Name",font=("Forte",20),bg="white",fg="maroon").place(x=550,y=100)
        self.txt_lname=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_lname.place(x=550,y=135,width=200)

        phonenolb=Label(frame1,text="Phone Number",font=("Forte",20),bg="white",fg="maroon").place(x=50,y=230)
        self.txt_phoneno=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_phoneno.place(x=50,y=265,width=200)

        emailidlb=Label(frame1,text="Email Address",font=("Forte",20),bg="white",fg="maroon").place(x=350,y=230)
        self.txt_emailid=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_emailid.place(x=350,y=265,width=300)

        usernamelb=Label(frame1,text="Create Username",font=("Forte",20),bg="white",fg="maroon").place(x=50,y=360)
        self.txt_username=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_username.place(x=320,y=360,width=210)

        passwordlb=Label(frame1,text="Create Password",font=("Forte",20),bg="white",fg="maroon").place(x=50,y=440)
        self.txt_password=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_password.place(x=50,y=475,width=220)

        cpasslb=Label(frame1,text="Confirm Password",font=("Forte",20),bg="white",fg="maroon").place(x=350,y=440)
        self.txt_cpass=Entry(frame1,font=("arial",15),highlightbackground='black',highlightthickness='1')
        self.txt_cpass.place(x=350,y=475,width=220)

        registerbtn=Button(frame1,text="REGISTER",cursor="hand2",padx=0,pady=0,bg="black",fg="white",font=("adobe gothic std b",22,"bold"),command=self.register_data).place(x=50,y=550)
        
        signinbt=Button(text='SIGN IN',cursor='hand2',padx=0,pady=0,bg='white',fg='brown',font=("adobe gothic std b",22,"bold"),command=self.sign).place(x=275,y=300)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_mname.get()==""or self.txt_lname.get()=="" or self.txt_phoneno.get()=="" or self.txt_cpass.get()=="" or self.txt_emailid.get()=="" or self.txt_username.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get() != self.txt_cpass.get():
           messagebox.showerror("Error","Password and confirm Password should be same",parent=self.root)  
        else:
             try:
                 con=pymysql.connect(host="localhost",user="root",password="nidhid1601",database="audiobook")
                 cur=con.cursor()
                 cur.execute("insert into customer (username,password,phone_no,fname,mname,lname,email_id) values (%s,%s,%s,%s,%s,%s,%s)",(self.txt_username.get(),self.txt_password.get(),self.txt_phoneno.get(),self.txt_fname.get(),self.txt_mname.get(),self.txt_lname.get(),self.txt_emailid.get()))
                 con.commit()
                 con.close()
                 messagebox.showinfo("Yay","Registered Successfully",parent=self.root)
                
             except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def sign(self):
        self.root.destroy()
        import login
        login.main()
 root=Tk()
 obj=Createacc(root)
 root.mainloop()
