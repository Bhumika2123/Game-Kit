from tkinter import *
import tkinter.messagebox

#declare vaariables 
pa =''
pb =''
p1 =''
p2 =''


click=True

buttons=''

flag=0

#function to call in main file
def playtictactoe():
    global p1,p2,pa,pb,click,buttons,flag
    #-----Functions-----
    flag=0
    #function to disable all the buttons
    def disableB():
          b1.configure(state=DISABLED)
          b2.configure(state=DISABLED)
          b3.configure(state=DISABLED)
          b4.configure(state=DISABLED)
          b5.configure(state=DISABLED)
          b6.configure(state=DISABLED)
          b7.configure(state=DISABLED)
          b8.configure(state=DISABLED)
          b9.configure(state=DISABLED)

    #function to check win or tie
    def checkwin():
        global flag
        #winning conditions
        if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
            b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
            b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
            b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
            b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
            b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
            b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
            b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
            disableB()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
             b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
             b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
             b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
             b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
             b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
             b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
             b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
             b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
             disableB()
             tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)
        #draw condition
        elif flag==8:
             tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
             
    #function to be called when any button is pressed
    def bClick(buttons):
        global click, player2_name, player1_name, pb, pa,flag
        if buttons["text"] == " " and click == True:
            buttons["text"] = "X"
            click = False
            pb = p2_name.get() + " Wins!"
            pa = p1_name.get() + " Wins!"
            checkwin()
            flag += 1


        elif buttons["text"] == " " and click == False:
            buttons["text"] = "O"
            click = True
            checkwin()
            flag += 1
            
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    #-----main-----

    #-----GUI-----
    root=Tk()
    root.title("Tic tac toe")

    #to get player 1 name
    p1_name =Entry(root,textvariable=p1,bd=5)   
    p1_name.grid(row=1,column=1)

    #to get player 2 name
    p2_name=Entry(root,textvariable=p2,bd=5)
    p2_name.grid(row=2,column=1)

    #label to show text player 1
    l1=Label(root,text='Player1:',fg='black',bg='white',height='1',width='10')
    l1.grid(row=1,column=0)

    #label to show text player 1
    l2=Label(root,text='Player2:',fg='black',bg='white',height='1',width='10')
    l2.grid(row=2,column=0)

    #buttons for the board of tic tac toe
    
    b1=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b1))
    b1.grid(row=3,column=0)

    b2=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b2))
    b2.grid(row=3,column=1)

    b3=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b3))
    b3.grid(row=3,column=2)

    b4=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b4))
    b4.grid(row=4,column= 0  )

    b5=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b5))
    b5.grid(row=4,column=1)

    b6=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b6))
    b6.grid(row=4,column=2)

    b7=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b7))
    b7.grid(row=5,column=0)

    b8=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b8))
    b8.grid(row=5,column=1)

    b9=Button(root,text=' ',width='17',height='5',fg='white',bg='black',command = lambda : bClick(b9))
    b9.grid(row=5,column=2)

    #start the gui
    root.mainloop()
