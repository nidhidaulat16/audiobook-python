import pyttsx3
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

def main():
 class pbook:
   def __init__(self,root):
        self.root=root
        self.root.title("Pronunciation Book")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        self.bg=ImageTk.PhotoImage(file="images/pbook/pbook bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(text='PRONUNCIATION BOOK',font=("britannic bold",44,"bold"),bg="black",fg="white").place(x=270,y=15)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(image=self.backbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=80,y=30)
        
        frame1=Frame(self.root,bg='black',highlightbackground='black',highlightthickness='3')
        frame1.place(x=200,y=200,width=900,height=500)
        self.frbg=ImageTk.PhotoImage(file="images/pbook/pbook frame.jpg")
        frbg=Label(frame1,image=self.frbg,bg='black').place(x=40,y=30,width=800,height=400)

        wordb=Label(frame1,text="Enter the word",font=("britannic bold",30),bg='white',fg="dark blue").place(x=290,y=150)
        self.word=Entry(frame1,font=("arial",28),highlightbackground='black',highlightthickness='2')
        self.word.place(x=210,y=240,width=500)
        
        playbtn=Button(frame1,text="PLAY",cursor="hand2",padx=0,pady=0,bg="light grey",fg="black",font=("adobe gothic std b",20,"bold"),command=self.playvoice).place(x=330,y=380)
        resetbtn=Button(frame1,text="RESET",cursor="hand2",padx=0,pady=0,bg="light grey",fg="black",font=("adobe gothic std b",20,"bold"),command=self.reset).place(x=480,y=380)
        
   def playvoice(self):             
        speaker=pyttsx3.init() 
        rate = speaker.getProperty("rate")
        #print(rate)
        speaker.setProperty("rate",105) 
        text=self.word.get()
        speaker.say(text)
        speaker.runAndWait()
   def reset(self):
       self.word.delete(0, END)
   def back(self):
        self.root.destroy()
        import home
        home.main()
 root=Tk()
 obj=pbook(root)
 root.mainloop()

if __name__=="__main__":
    main()