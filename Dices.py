from random import randint
from tkinter import *

window = Tk()
window.title("Dice Simulator")
window.geometry("300x210")
window.resizable(False,False)
window.config(bg = "black")

f1 = Frame( window , bg = "black")
f2 = Frame( window , bg = "black")

photos_nums = [PhotoImage( file = 'one.png'),
				PhotoImage( file = 'two.png'),
				PhotoImage( file = 'three.png'),
				PhotoImage( file = 'four.png'),
				PhotoImage( file = 'five.png'),
				PhotoImage( file = 'six.png')]

def roll():
	d1 = randint(0,5)
	d2 = randint(0,5)

	Dice1Label.configure( image =photos_nums[d1])
	Dice2Label.configure( image = photos_nums[d2])

	return d1,d2

Dice1Label = Label(f1,image = photos_nums[5],bg = "black")
Dice2Label = Label(f1,image = photos_nums[5],bg = "black")

RollButton = Button(f2, text = "Roll the dices",font = ('Times New Roman',14),command = roll)

Dice1Label.pack(side = "left" , padx = 10 , pady = 10)
Dice2Label.pack(side = "right", padx = 10 , pady = 10)

RollButton.pack(padx = 10 , pady = 10)

f2.pack(side = "bottom" , fill = "x", padx = 10 , pady = 10)
f1.pack(side = "top" , fill = "both", padx = 10 , pady = 10)

window.mainloop()
