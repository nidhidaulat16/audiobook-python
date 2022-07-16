from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from tkPDFViewer import tkPDFViewer as pdf 
import PyPDF2
from pygame import mixer
import os
import notepad

def main():
 
 class ebook: 
   def __init__(self,root):
        self.root=root
        self.root.title("E-Book")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        self.bg=ImageTk.PhotoImage(file="images/ebook_home/ebook1 bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        frame1=Frame(self.root,bg='crimson')
        frame1.place(x=460,y=770,width=680,height=80)
        
        pdfFileObj = open('ebooks/A_Little_Journey.pdf', 'rb') 
        scrollbar=Scrollbar(self.root)
        scrollbar.place(x=1150,y=20,height=740)
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
       
        str=''
        for i in range(0,14):
            str+=pdfReader.getPage(i).extractText()
        
        # closing the pdf file object 
        pdfFileObj.close() 
        
        self.textarea = Text(font=('calibri', 13, 'bold'),height=7,wrap='word',highlightbackground='black',highlightthickness='2')
        self.textarea.place(x=450, y=20,height=740,width=700)
        self.textarea.insert(END,str)
        self.textarea.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textarea.yview)
        
        #PLAY, PAUSE, STOP BUTTONS
        self.playbt=ImageTk.PhotoImage(file="images/icons/play bt.png")    
        playbtn=Button(frame1,image=self.playbt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.playsong).place(x=5,y=5)
        
        self.pausebt=ImageTk.PhotoImage(file="images/icons/pause bt.png")
        pausebtn=Button(frame1,image=self.pausebt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.pausesong).place(x=105,y=5)
        
        self.resumebt=ImageTk.PhotoImage(file="images/icons/resume bt.png")
        resumebtn=Button(frame1,image=self.resumebt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.resumesong).place(x=205,y=5)
        
        self.stopbt=ImageTk.PhotoImage(file="images/icons/stop bt.png")
        stopbtn=Button(frame1,image=self.stopbt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.stopsong).place(x=305,y=5)
        
        self.homebt=ImageTk.PhotoImage(file="images/icons/home bt.png")
        homebtn=Button(frame1,image=self.homebt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.home).place(x=505,y=5)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(frame1,image=self.backbt,cursor="hand2",bg="white",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=605,y=5)
        
        #voice gender
        cmb_gender=Label(text="Select your Assistant",font=("Forte",20,"bold"),bg="white",fg="black").place(x=60,y=400)
        self.voice = ttk.Combobox(text="", font=("britanic bold", 14),state='readonly',justify=CENTER)
        self.voice['values'] = ("Female","Male")
        self.voice.place(x=150, y=450,height=40,width=105)
        self.voice.current(0)

        self.notepadimg=ImageTk.PhotoImage(file="images/icons/notepad bt.png")
        notepadbtn=Button(image=self.notepadimg,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.note).place(x=250,y=550)
        notelb=Label(text='Review',font=("forte",20,"bold"),bg="white",fg="black").place(x=130,y=550)
        
       
   
   def playsong(self):
      # current_song = pygame.mixer.music.load('A_Little_Journey.mp3')
      current_volume = float(0.5)
      try:
         reader = self.voice.get()
         if(reader== 'Female'):
               mixer.init()
               mixer.music.load('audio/A_Little_Journey f.mp3')
               mixer.music.set_volume(current_volume)
               mixer.music.play()
         elif(reader == 'Male'):
               mixer.init()
               mixer.music.load('audio/A_Little_Journey m.mp3')
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
   
   def home(self):
        self.root.destroy()
        import home
        home.main()
   def back(self):
        self.root.destroy()
        import ebook_home
        ebook_home.main()

   def note(self):
        #self.root.destroy()
        notepad.main()

 root=Tk()
 obj=ebook(root)
 root.mainloop()

if __name__=="__main__":
    main()

