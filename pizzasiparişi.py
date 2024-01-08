import tkinter as tk 
form=tk.Tk()
form.title('Pizza Sipariş Programı')
form.geometry('500x700+400+100')


başlık=tk.Label(text='Pizza Sipariş Programına Hoşgeldiniz', fg='black', bg='green',font='Times 17 italic')
başlık.pack()

ad=tk.Label(text='Ad:', fg='black', bg='pink',font='Times 10 bold')
ad.place(x=10, y=100)

ad_entry=tk.Entry()
ad_entry.place(x=60, y=100)


soyad=tk.Label(text='Soyad:', fg='black', bg='pink',font='Times 10 bold')
soyad.place(x=10, y=140)

soyad_entry=tk.Entry()
soyad_entry.place(x=60, y=140)

pizza_boyutu=tk.Label(text='Pizza Boyutu:',fg='black',bg='pink',font='Times 10 bold')
pizza_boyutu.place(x=10, y=180)

x=tk.StringVar()
x.set('0')

radio=tk.Radiobutton(form, text='Büyük Boy',activebackground='green',value=1,variable=x)
radio.place(x=100,y=180)

radio2=tk.Radiobutton(form, text='Orta Boy',activebackground='blue',value=2,variable=x)
radio2.place(x=100,y=220)

radio3=tk.Radiobutton(form, text='Küçük Boy', activebackground='yellow',value=3,variable=x)
radio3.place(x=100,y=260)

pizza_türü=tk.Label(text='Pizza Türü:', fg='black',bg='pink',font='Times 10 bold')
pizza_türü.place(x=10,y=330)


y=tk.StringVar()
y.set('0')

pizza_türü1=tk.Radiobutton(form, text='Karışık Pizza',activebackground='green',value=1,variable=y)
pizza_türü1.place(x=100,y=330)

pizza_türü2=tk.Radiobutton(form, text='Mozerella Peynirli Pizza', activebackground='blue',value=2,variable=y)
pizza_türü2.place(x=100,y=370)

pizza_türü3=tk.Radiobutton(form, text='Kavurmalı Pizza', activebackground='yellow',value=3,variable=y)
pizza_türü3.place(x=100,y=410)

pizza_türü4=tk.Radiobutton(form, text='Margarita Pizza', activebackground='pink',value=4,variable=y)
pizza_türü4.place(x=100,y=450)

pizza_türü5=tk.Radiobutton(form, text='Peperonili  Pizza', activebackground='purple',value=5,variable=y)
pizza_türü5.place(x=100,y=490)

içecek=tk.Label(text='İçecek:',fg='black',bg='pink',font='Times 10 bold')
içecek.place(x=300, y=100)

z=tk.StringVar()
z.set('0')

içecek_türü1=tk.Radiobutton(form, text='Ayran',activebackground='green',value=1,variable=z)
içecek_türü1.place(x=350,y=100)

içecek_türü2=tk.Radiobutton(form, text='Sprite',activebackground='blue',value=2,variable=z)
içecek_türü2.place(x=350,y=140)

içecek_türü3=tk.Radiobutton(form, text='Fanta',activebackground='yellow',value=3,variable=z)
içecek_türü3.place(x=350,y=180)

içecek_türü4=tk.Radiobutton(form, text='Coco Cola',activebackground='purple',value=4,variable=z)
içecek_türü4.place(x=350,y=220)


def sipariş():
    ad_entry.delete(0,'end')
    soyad_entry.delete(0,'end')

    x.set('0')
    y.set('0')
    z.set('0')

    siparişiniz_alındı=tk.Label(form,text='Siparişiniz Alındı.',fg='black',bg='blue')
    siparişiniz_alındı.pack(side=tk.BOTTOM,fill=tk.X)


sipariş=tk.Button(form, text='Sipariş Ver',fg='black',bg='green',command=sipariş)
sipariş.pack(side=tk.BOTTOM,fill=tk.X)


form.mainloop()