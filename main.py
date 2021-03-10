from tkinter import *
from ComandaVoce import *
from PIL import ImageTk, Image
root = Tk()
root.title("Open LNK files")
#root.iconbitmap("any icon path")

#my_img = ImageTk.PhotoImage(Image.open("any image path for your button"))

#mybutton = Button(root, image=my_img, command=VoiceCommand)   image button
mybutton = Button(root, command=VoiceCommand)
mybutton.pack()




root.mainloop()

