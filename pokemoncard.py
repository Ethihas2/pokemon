from tkinter import *
from PIL import ImageTk,Image 
import random


root = Tk()
root.geometry("800x500")
root.title("Pokemon Card Game")
root.configure(background="yellow")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasaur = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))

pokemon = [abra,bulbasaur,charmender,iyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu,ratata,squirtle]
pokemon_power = [30,60,50,100,70,70,60,90,40,70,200,40,50]
player1_score_var = 0
player2_score_var = 0
 
player1 = Label(root,text="Player 1",bg="dodgerblue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2 = Label(root,text="Player 2",bg="dodgerblue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score = Label(root,bg="dodgerblue",fg="white")
player1_score.place(relx=0.1,rely=0.7,anchor=CENTER)

player2_score = Label(root,bg="dodgerblue",fg="white")
player2_score.place(relx=0.9,rely=0.7,anchor=CENTER)

pokemon_card = Label(root) 
pokemon_card.place(relx=0.5,rely=0.5,anchor=CENTER)


def player_1():
    global player1_score_var
    random_num = random.randint(0,12)
    pokemon_card["image"]=pokemon[random_num]
    player1_score_var += pokemon_power[random_num]
    print(player1_score_var)
    player1_score["text"]=str(player1_score_var)

def player_2():
    global player2_score_var
    random_num = random.randint(0,12)
    pokemon_card["image"]=pokemon[random_num]
    player2_score_var += pokemon_power[random_num]
    print(player2_score_var)
    player2_score["text"]=str(player2_score_var)


button1 = Button(root,image=button,command=player_1)
button1.place(relx=0.1,rely=0.5,anchor=CENTER)

button2 = Button(root,image=button,command=player_2)
button2.place(relx=0.9,rely=0.5,anchor=CENTER)

root.mainloop()