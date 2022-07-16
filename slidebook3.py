from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
from pygame import mixer
import os

def main():
 class Slide:      
    def __init__(self,root):
        self.root=root
        self.root.title("Slide Book")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='light pink')
        root.state('zoomed')
        
        title=Label(text='Lets Start \nReading!',font=("britannic bold",26,"bold"),bg="light pink",fg="black").place(x=50,y=15)
        
        #frame1
        frame1=Frame(self.root,bg='white')
        frame1.place(x=330,y=10,width=900,height=870)
        self.frame1img=ImageTk.PhotoImage(file="images/slide book/story3_1pic.png")
        frame1img=Label(frame1,image=self.frame1img).place(x=5,y=5,width=900,height=790)

        #frame2
        frame2=Frame(self.root,bg='white')
        frame2.place(x=330,y=10,width=900,height=870)
        self.frame2img=ImageTk.PhotoImage(file="images/slide book/story3_2pic.png")
        frame2img=Label(frame2,image=self.frame2img).place(x=5,y=5,width=900,height=790)

        #frame3
        frame3=Frame(self.root,bg='white')
        frame3.place(x=330,y=10,width=900,height=870)
        self.frame3img=ImageTk.PhotoImage(file="images/slide book/story3_3pic.png")
        frame3img=Label(frame3,image=self.frame3img).place(x=5,y=5,width=900,height=790)

        next1bt=Button(frame1,text='NEXT',cursor='hand2',padx=0,pady=0,bg='black',fg='white',font=("adobe gothic std b",16,"bold"),command=lambda:showframe(frame2)).place(x=700,y=800)
        
        previous2bt=Button(frame2,text='PREVIOUS',cursor='hand2',padx=0,pady=0,bg='black',fg='white',font=("adobe gothic std b",16,"bold"),command=lambda:showframe(frame1)).place(x=50,y=800)      
        next2bt=Button(frame2,text='NEXT',cursor='hand2',padx=0,pady=0,bg='black',fg='white',font=("adobe gothic std b",16,"bold"),command=lambda:showframe(frame3)).place(x=700,y=800)

        previous3bt=Button(frame3,text='PREVIOUS',cursor='hand2',padx=0,pady=0,bg='black',fg='white',font=("adobe gothic std b",16,"bold"),command=lambda:showframe(frame2)).place(x=50,y=800)
        next3bt=Button(frame3,text='NEXT',cursor='hand2',padx=0,pady=0,bg='black',fg='white',font=("adobe gothic std b",16,"bold"),command=lambda:showframe(frame1)).place(x=700,y=800)
        
        def showframe(frame):
            frame.tkraise()
        showframe(frame1)

        #frame4
        frame4=Frame(self.root,bg='white',highlightbackground='black',highlightthickness='1')
        frame4.place(x=100,y=150,width=100,height=700)
        
        self.homebt=ImageTk.PhotoImage(file="images/icons/home bt.png")
        homebtn=Button(frame4,image=self.homebt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.home).place(x=20,y=500)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(frame4,image=self.backbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=20,y=600)
        
        #PLAY, PAUSE, STOP BUTTONS
        self.playbt=ImageTk.PhotoImage(file="images/icons/play bt.png")    
        playbtn=Button(frame4,image=self.playbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.playsong).place(x=20,y=50)
        
        self.pausebt=ImageTk.PhotoImage(file="images/icons/pause bt.png")
        pausebtn=Button(frame4,image=self.pausebt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.pausesong).place(x=20,y=150)
        
        self.resumebt=ImageTk.PhotoImage(file="images/icons/resume bt.png")
        resumebtn=Button(frame4,image=self.resumebt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.resumesong).place(x=20,y=250)
        
        self.stopbt=ImageTk.PhotoImage(file="images/icons/stop bt.png")
        stopbtn=Button(frame4,image=self.stopbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.stopsong).place(x=20,y=350)
        
    def playsong(self):
      #current_song = pygame.mixer.music.load('Slide story1 audio.mp3')
      
      try:
         current_volume = float(0.5)
         mixer.init()
         mixer.music.load('audio/Slide story3 audio.mp3')
         mixer.music.set_volume(current_volume)
         mixer.music.play()
      except:
         messagebox.showerror("Error",parent=self.root)
         
    def pausesong(self):
      try:
         mixer.music.pause()
      except:
         messagebox.showerror("Error","Kindly play the music first!",parent=self.root)
   
    def resumesong(self):
      try:
         mixer.music.unpause() 
      except:
         messagebox.showerror("Error","Kindly play the music first!",parent=self.root)
   

    def stopsong(self):
      try:
         mixer.music.stop()
      except:
         messagebox.showerror("Error","Kindly play the music first!",parent=self.root)
    def back(self):
        self.root.destroy()
        import slide_home  
        slide_home.main()
    def home(self):
        self.root.destroy()
        import home
        home.main()
 root=Tk()
 obj=Slide(root)
 root.mainloop()

if __name__=="__main__":
    main()