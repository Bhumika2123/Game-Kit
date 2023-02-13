from tkinter import *
import random
from tkinter import messagebox
import jumblewordsmodule
import tictactoemodule
import stonepaperscissormodule



#-----main----

# create a GUI window
root=Tk()

#to give title to the gui window
root.title('Game Launcher')

#to set geomtry
root.geometry('590x750')

#to set bg colour
root.configure(background='#c4beaf')

#1st label to show welcome message
l1 = Label(root , text='Welcome to the Game Launcher' , fg='#192A56',bg='#c4beaf',font=("Helvetica", 16))
l1.grid(row=0,column=0)

#empty label to skip a row
l2 = Label(root , text='' , fg='#192A56',bg='#c4beaf',font=("Helvetica", 16))
l2.grid(row=2,column=0)

#button for jumbled game
b1 = Button(root,text= ' Play Jumble Words   ',command=jumblewordsmodule.playjumblewords,bd=10,bg='#67E6DC',fg='#192A56')
b1.grid(row=3,column=0)

#empty label to skip a row
l10 = Label(root , text='' , fg='#192A56',bg='#c4beaf',font=("Helvetica", 16))
l10.grid(row=4,column=0)

#button to play tic tac toe
b2=Button(root,text='Play Tic Tac Toe',command=tictactoemodule.playtictactoe,bd=10,bg='#67E6DC',fg='#192A56')
b2.grid(row=5,column=0)

#empty label to skip a row
l3 = Label(root , text='' , fg='#192A56',bg='#c4beaf',font=("Helvetica", 16))
l3.grid(row=6,column=0)

#button to play stone paper scissor
b2=Button(root,text='Play Stone Paper Scissor',command=stonepaperscissormodule.call,bd=10,bg='#67E6DC',fg='#192A56')
b2.grid(row=7,column=0)

#empty label to skip a row
l3 = Label(root , text='' , fg='#192A56',bg='#c4beaf',font=("Helvetica", 16))
l3.grid(row=8,column=0)



#label for discription about tic tac toe
l4= Label( text='About Tic Tac toe', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=9, column=0)

#empty labels for providing space between column 0&4

l5=Label( text='''
The game is played on a grid that's 3 squares by 3 squares.
You are X, your friend is O. Players take turns putting their
marks in empty squares.The first player to get 3 of her marks 
in a row is the winner.''', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=10, column=0)


#empty label to add space between discriptions of tic tac toe and jumbled words
l6= Label( text=' ', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=11, column=0)

# label for title for discription 
l7= Label( text='About Jumble Words', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=12, column=0)

#discription of jumbled words
l8=Label( text=''' 
This game will be start with a "jumbled word" as a question.
The word, of which the jumble is created, must be a meaningful dictionary word
what you have to do is, solve the jumble and find the answer word.''',fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=13, column=0 )

#label for title for discription of Stone Paper Scissor
l7= Label( text='Stone Paper Scissor', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=14, column=0)

#discription of jumbled words
l8=Label( text=''' 
 In this game, it has three possible outcomes: a draw, a win or a loss.
A player who decides to play rock will beat another player who has chosen
scissors but will lose to one who has played paper a play of paper will lose
to a play of scissors. If both players choose the same shape, the game is tied 
and is usually immediately replayed to break the tie.''',fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=15, column=0 )



#label for discription about tic tac toe
l9= Label( text='Creator - Bhumika Makhija', fg='#192A56',bg='#c4beaf',font=("Helvetica", 13)).grid(row=16, column=0)


# start the GUI
root.mainloop()
