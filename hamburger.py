import tkinter as tk
form=tk.Tk()
form.title("Hamburger Siparişi")
form.geometry('500x700+400+50')

başlık=tk.Label(text='Hamburger Siparişi Programına Hoşgeldiniz',fg='black',bg='yellow',font='Times 17 italic')
başlık.pack()

ad=tk.Label(text='Ad:',fg='white',bg='black',font='Times 13 bold')
ad.place(x=10,y=100)

ad_entry=tk.Entry()
ad_entry.place(x=60,y=100)

soyad=tk.Label(text='Soyad:',fg='white',bg='black',font='Times 13 bold')
soyad.place(x=10,y=150)

soyad_entry=tk.Entry()
soyad_entry.place(x=80,y=150)

adres=tk.Label(text='Adres:',fg='white',bg='pink',font='Times 13 bold')
adres.place(x=10,y=200)

adres_entry=tk.Entry()
adres_entry.place(x=80,y=200) 

telefon=tk.Label(text='Telefon Numarası:',fg='white',bg='green',font='Times 13 bold')
telefon.place(x=10,y=250)

telefon_entry=tk.Entry()
telefon_entry.place(x=160,y=250)


hamburger_türü=tk.Label(text='Hamburger Türü:',fg='white',bg='blue',font='Times 15 bold')
hamburger_türü.place(x=10,y=300)

x=tk.StringVar()
x.set('0')

radio=tk.Radiobutton(form,text='Bigmac',activebackground='green',value=1,variable=x)
radio.place(x=180,y=300)

radio2=tk.Radiobutton(form,text='Cheese Burger',activebackground='yellow',value=2,variable=x)
radio2.place(x=300,y=300)

radio3=tk.Radiobutton(form,text='Whopper',activebackground='blue',value=3,variable=x)
radio3.place(x=180,y=350)

radio4=tk.Radiobutton(form,text='Islak Burger',activebackground='red',value=4,variable=x)
radio4.place(x=300,y=350)

içecek_türü=tk.Label(text='İçecek Türü:',fg='white',bg='magenta',font='Times 15 bold')
içecek_türü.place(x=10,y=400)

y=tk.StringVar()
y.set('0')

içecek1=tk.Radiobutton(form,text='Niğde Gazozu',activebackground='green',value=1,variable=y)
içecek1.place(x=130,y=400)

içecek2=tk.Radiobutton(form,text='Kola',activebackground='yellow',value=2,variable=y)
içecek2.place(x=240,y=400)

içecek3=tk.Radiobutton(form,text='Ayran',activebackground='blue',value=3,variable=y)
içecek3.place(x=130,y=450)

içecek4=tk.Radiobutton(form,text='Fanta',activebackground='red',value=4,variable=y)
içecek4.place(x=240,y=450)



def sipariş():
    ad_entry.delete(0,'end')
    soyad_entry.delete(0,'end')
    adres_entry.delete(0,'end')
    telefon_entry.delete(0,'end')
    x.set('0')
    y.set('0')

sipariş=tk.Button(form,text='Sipariş Ver',fg='grey',bg='black',command=sipariş)
sipariş.pack(side=tk.BOTTOM)

















form.mainloop()