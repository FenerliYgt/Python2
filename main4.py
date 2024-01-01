import tkinter as tk
form=tk.Tk()
form.title('Entry')
form.geometry('500x450+250+250')

giris=tk.Entry(form,fg='black', bg='green')
giris.pack(side=tk.RIGHT)

giris2=tk.Entry(form,fg='red',bg='blue')
giris2.pack(side=tk.LEFT)






form.mainloop()

