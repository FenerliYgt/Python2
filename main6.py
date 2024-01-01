import tkinter as tk
form=tk.Tk()
form.geometry('500x500')
label=tk.Label(text='Geometrik yöneticiler')
label.pack(side=tk.TOP)
buton=tk.Button(text='Pack()', bg='red')
buton.pack(side=tk.BOTTOM, fill=tk.X)


form.mainloop()