# schimb butoane + fundal


#proiect 1.3

import tkinter
from tkinter import * 
from tkinter import messagebox
import random
from tkinter import Label
from time import strftime
import tkinter as tk
from tkinter import filedialog
import ast
from tkinter import Tk, Text

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

text = Text(root,height=8)
text.pack()


def signin():
    username = user.get()
    password = code.get()
    
    file= open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    print(r.keys())
    print(r.values())
    
    if username in r.keys() and password == r[username]:
        root = Tk()
        root.geometry('925x500+300+200')
        root.title("TIC TAC TOE") #Aici pot schimba titlul
        root.resizable(False,False)
        root.configure(bg="#3498DB") #Aici schimbam funalul
        
        def enter():
            root = Tk()
            root.title('Tic-Tac-Toe')
            root.resizable(False,False)
            #root.iconbitmap('localhost')
            root.geometry('320x360+600+300')
            # X starts so true
            clicked = True
            count = 0
            # disable all the buttons
            def disable_all_buttons():
                b1.config(state=DISABLED)
                b2.config(state=DISABLED)
                b3.config(state=DISABLED)
                b4.config(state=DISABLED)
                b5.config(state=DISABLED)
                b6.config(state=DISABLED)
                b7.config(state=DISABLED)
                b8.config(state=DISABLED)
                b9.config(state=DISABLED)
            # Check to see if someone won
            def checkifwon():
                global winner
                winner = False
                if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
                    b1.config(bg="red")
                    b2.config(bg="red")
                    b3.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
                    b4.config(bg="red")
                    b5.config(bg="red")
                    b6.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
                    b7.config(bg="red")
                    b8.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
                    b1.config(bg="red")
                    b4.config(bg="red")
                    b7.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
                    b2.config(bg="red")
                    b5.config(bg="red")
                    b8.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
                    b3.config(bg="red")
                    b6.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
                    b1.config(bg="red")
                    b5.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
                    b3.config(bg="red")
                    b5.config(bg="red")
                    b7.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
                    disable_all_buttons()
                #### CHECK FOR O's Win
                elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
                    b1.config(bg="red")
                    b2.config(bg="red")
                    b3.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
                    b4.config(bg="red")
                    b5.config(bg="red")
                    b6.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
                    b7.config(bg="red")
                    b8.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
                    b1.config(bg="red")
                    b4.config(bg="red")
                    b7.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
                    b2.config(bg="red")
                    b5.config(bg="red")
                    b8.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
                    b3.config(bg="red")
                    b6.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
                    b1.config(bg="red")
                    b5.config(bg="red")
                    b9.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()
                elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
                    b3.config(bg="red")
                    b5.config(bg="red")
                    b7.config(bg="red")
                    winner = True
                    messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
                    disable_all_buttons()

                # Check if tie
                if count == 9 and winner == False:
                    messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
                    disable_all_buttons()

            # Button clicked function
            def b_click(b):
                global clicked, count
                if b["text"] == " " and clicked == True:
                    b["text"] = "X"
                    clicked = False
                    count += 1
                    checkifwon()
                elif b["text"] == " " and clicked == False:
                    b["text"] = "O"
                    clicked = True
                    count += 1
                    checkifwon()
                else:
                    messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )
            # Start the game over!
            def reset():
                global b1, b2, b3, b4, b5, b6, b7, b8, b9
                global clicked, count
                clicked = True
                count = 0
                # Build our buttons
                b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
                b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
                b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
                b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
                b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
                b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
                b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
                b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
                b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
                # Grid our buttons to the screen
                b1.grid(row=0, column=0)
                b2.grid(row=0, column=1)
                b3.grid(row=0, column=2)
                b4.grid(row=1, column=0)
                b5.grid(row=1, column=1)
                b6.grid(row=1, column=2)
                b7.grid(row=2, column=0)
                b8.grid(row=2, column=1)
                b9.grid(row=2, column=2)
            # Create menue
            my_menu = Menu(root)
            root.config(menu=my_menu)
            # Create Options Menu
            options_menu = Menu(my_menu, tearoff=False)
            my_menu.add_cascade(label="Options", menu=options_menu)
            options_menu.add_command(label="Reset Game", command=reset)#butonul de resest game
            reset()
            root.mainloop()
            
            
            
        Button(root,width=50,pady=40,text='GAME- TIC TAC TOE ',bg='#F1C40F',fg='black',border=8,command=enter).place(x=270,y=250)
        #butoanele din a 2a fereastra

       
        Button(root,width=30,pady=20,text='Click on the button below to play!',bg='#F1C40F',fg='black',command=enter,font=('Impact',40,'bold'),border=0).place(x=50,y=10)
        


        mainloop()    
       
        
        
        
    
    elif username in r.keys() and password != r[username]:
        messagebox.showerror("Invalid","Invalid username or password")
        
        mainloop()






img = PhotoImage(file="C:\\Users\\user\\Downloads\\—Pngtree—login vector_8490813.png")
Label(root,image=img,bg='white').place(x=-230,y=-300)


frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=125,y=3)

#---------------------------------------------------------------------------------------------------------------------
#PENTRU USERNAME
def on_enter(e):
    user.delete(0,'end')

def on_Leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')
             

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')

user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_Leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#---------------------------------------------------------------------------------------------------------------------
#PENTRU PASSWORD
def on_enter(e):
    code.delete(0,'end')

def on_Leave(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')


code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_Leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#---------------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
Label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=230,y=270)





root.mainloop()

