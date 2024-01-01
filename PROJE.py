import tkinter as tk
form=tk.Tk()
form.title('Ortalama Hesaplayıcı')
form.geometry('500x40')



buton=tk.Button(form, text='Hesapla' ,fg='black')
buton.pack(side=tk.BOTTOM)

label=tk.Label(form, text='1. Sınav' ,fg='black')
label.pack(side=tk.LEFT)

giris=tk.Entry(form ,fg='black' ,bg='white')
giris.pack(side=tk.LEFT)

label2=tk.Label(form, text='2. Sınav' ,fg='black')
label2.pack(side=tk.LEFT)

giris2=tk.Entry(form, fg='black' ,bg='white')
giris2.pack(side=tk.LEFT)





form.mainloop()



    


    














form.mainloop()