import tkinter
window=tkinter.Tk()
button=tkinter.Button(window, text = 'Не нажимать', width=40)
button.pack(padx=10, pady=10)
clickCount=0
def onClick (event):
    global clickCount
    clickCount+=1
    if clickCount ==1:
        button.configure(text="4619")
    elif clickCount == 2:
        button.configure(text="19529")
    else:
        button.pack_forget()
button.bind("<ButtonRelease - 1>", onClick)
window.mainloop()
