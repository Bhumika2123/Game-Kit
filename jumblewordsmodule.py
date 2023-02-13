from tkinter import *
import random
from tkinter import messagebox

#function to call in main file
def playjumblewords():
    global index
    #function to reset the jumbled word and display new one
    def reset():
        global index
        index=random.randrange(0,20,1)
        lb.config(text=words[index])
        e1.delete(0,END)

    #function to configure the label as a jumbled word
    def word():
        lb.config(text=words[index])

    #function to check if answere is correct or not
    def check():
        var = e1.get() #to get the answere from the entry widgets into var
        #conditions to check the answere
        if var.lower()==answers[index]:
            messagebox.showinfo("congrulations","You got the answer right! Congrulations")
            reset()
        else:
            messagebox.showerror("Wrong","Better luck next time")
            e1.delete(0,END)

    #----- Main -----

    #list conataining all the answeres
    answers = ['computer','gadgets','research','new','electronics','softwarre','communication',
          'tools','download','science','machine','energy','transport','battery','internet',
          'future','military','space','innovation','education']

    #list containing all the jumbled words
    words = ['tompreuc','tgdgeas','eresahrc','ewn','ectsielnocr','tesfawro','uoiinnommtacc',
         'ootsl','wnlododa','ecinsec','ecnimah','erngey','orttpnsra','abtryet','ernttnei',
         'rftueu','imalrity','cesap','nntnovoaii','dcotanuei']

    #to create a random number 
    index=random.randrange(0,20,1)

    #variable for containing given answeres 
    ans=""

    #----- GUI -----

    root = Tk()
    root.geometry('350x400')
    root.title('Jumble Words')
    root.configure(background='#bdb9b1')

    #label to show the jubled word
    lb = Label(root,text='Here',bg="#bdb9b1",fg="#000000")
    lb.pack(pady=15)

    #text box to get the answere
    e1=Entry(root,textvariable=ans)
    e1.pack(pady=20)

    #button to check the answere
    btncheck=Button(root,text="Check",width=20,command=check)
    btncheck.pack(pady=25)

    #button to reset the word
    btnreset=Button(root,text="Reset",width=20,command=reset)
    btnreset.pack(pady=30)
    
    word()

    #start the gui
    root.mainloop()
        
