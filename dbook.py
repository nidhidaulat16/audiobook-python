from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import json
import pyttsx3
from difflib import get_close_matches

def main():
 class Dbook:
    def __init__(self,root):
        self.root=root
        self.root.title("Talking dictionary")
        self.root.geometry("1275x970+0+0")
        self.root.config(bg='white')
        root.state('zoomed')

        self.bg=ImageTk.PhotoImage(file="dbook/dbook bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        frame1=Frame(self.root,bg='white',highlightbackground='black',highlightthickness='3')
        frame1.place(x=200,y=200,width=900,height=600)
        self.frbg=ImageTk.PhotoImage(file="dbook/dbook frame.jpg")
        frbg=Label(frame1,image=self.frbg,bg='black').place(x=0,y=0,width=900,height=600)

        title=Label(text='TALKING DICTIONARY',font=("britannic bold",44,"bold"),bg="white",fg="black").place(x=300,y=15)
        
        self.backbt=ImageTk.PhotoImage(file="images/icons/back bt.png")
        backbtn=Button(image=self.backbt,cursor="hand2",bg="black",fg="black",font=("britanic bold",15,"bold"),command=self.back).place(x=80,y=30)
        
        enterwordLabel = Label(frame1,text='Enter Word', font=('forte', 28, 'bold'), fg='red3', bg='white').place(x=10, y=20)

         
        self.enterword=Entry(frame1,font=("arial",23),highlightbackground='black',highlightthickness='2')
        self.enterword.place(x=270,y=20,width=400)
        
        self.searchimage = ImageTk.PhotoImage(file='dbook/search.png')
        searchButton = Button(frame1,image=self.searchimage,bd=0,bg='white',cursor='hand2',command=self.search).place(x=720, y=20)

        self.micimage = ImageTk.PhotoImage(file='dbook/mic.png')
        micButton = Button(frame1,image=self.micimage,bg='white',bd=0,cursor='hand2',command=self.wordaudio).place(x=800, y=20)

        meaninglabel = Label(frame1, text='Meaning', font=('forte', 28, 'bold'), fg='red3', bg='white').place(x=350, y=120)
        self.textarea = Text(frame1, font=('arial', 18, 'bold'), height=7, width=50,wrap='word',highlightbackground='black',highlightthickness='2')
        self.textarea.place(x=25, y=200)

        self.audioimage = ImageTk.PhotoImage(file='dbook/microphone.png')
        audioButton = Button(frame1, image=self.audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',cursor='hand2',command=self.meaningaudio).place(x=370, y=450)

        self.clearimage = ImageTk.PhotoImage(file='dbook/clear.png')
        clearButton = Button(frame1, image=self.clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=self.clear).place(x=470, y=450)

        engine=pyttsx3.init()
    
    
    def wordaudio(self):
           speaker=pyttsx3.init()
           rate = speaker.getProperty("rate")
           #print(rate)
           speaker.setProperty("rate",105)
           text=self.enterword.get()
           speaker.say(text)
           speaker.runAndWait()
    
    def search(self):
        data = json.load(open('dbook/data.json'))
        word = self.enterword.get()
        word = word.lower()
        if word in data:
           meaning = data[word]
           self.textarea.config(state=NORMAL)
           self.textarea.delete(1.0, END)
           for item in meaning:
               self.textarea.insert(END, u'\u2022' + item + '\n\n')
           self.textarea.config(state=DISABLED)
        elif len(get_close_matches(word, data.keys())) > 0:

             close_match = get_close_matches(word, data.keys())[0]
             res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
             if res == True:
                meaning = data[close_match]
                self.textarea.delete(1.0, END)
                self.textarea.config(state=NORMAL)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')
                self.textarea.config(state=DISABLED)
             else:
                self.textarea.delete(1.0, END)
                messagebox.showinfo('Information', 'Please type a correct word')
                self.enterword.delete(0, END)

        else:
             messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
             self.enterword.delete(0, END)
    
    def  meaningaudio(self):
         engine=pyttsx3.init()
         rate = engine.getProperty("rate")
         #print(rate)
         engine.setProperty("rate",105)
         text=self.textarea.get(1.0,END)
         engine.say(text)
         engine.runAndWait()
    
    def clear(self):
        self.textarea.config(state=NORMAL)
        self.enterword.delete(0, END)
        self.textarea.delete(1.0, END)
        self.textarea.config(state=DISABLED)
    
    def back(self):
        self.root.destroy()
        import home
        home.main()

 root=Tk()
 obj=Dbook(root)
 root.mainloop()

if __name__=="__main__":
    main()