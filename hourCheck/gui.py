from time import sleep
from threading import Thread
from tkinter import *

def submitText():
	'''Records text from textEntry in textfile hourCheck.txt'''
	f = open("hourCheck.txt", "a")
	f.write(textEntry.get() + "\n")
	textEntry.delete(0,END)

def hourCheck():
	'''Gives tkinter window focus once per hour'''
	while(True):
		sleep(3600)
		root.lift()
		print("Lifted!")

def hourCheckThread():
	'''Launches hourCheck() in a thread'''
	thread = Thread(target=hourCheck)
	thread.start()
	thread.join()

root = Tk()
root.geometry("400x400")
frame = Frame(root)
frame.pack()

bottomFrame = Frame(root)
bottomFrame.pack( side = BOTTOM )

textEntry = Text(root, height=20, width=40)
textEntry.pack( side = TOP )

blackButton = Button(bottomFrame, text="Submit", fg="black", command=submitText)
blackButton.pack( side = BOTTOM)

#root.after(1000, hourCheckThread) #currently causes tkinter/python to stop responding on Windows 7
root.mainloop()