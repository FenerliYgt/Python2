import tkinter as tk
form=tk.Tk()
form.title('Hesap Makinesi')
form.geometry('320x300')



sonuç=tk.Label(form,text='',font='Courier 16 bold',width=30,justify='center')
sonuç.place(x=-50,y=20)

sayı1=tk.Entry(form,font='Courier 14 bold',width=15,justify='right')
sayı1.place(x=70,y=50)
sayı2=tk.Entry(form,font='Courier 14 bold',width=15,justify='right')
sayı2.place(x=70,y=80)

def topla():
    if sayı1.get().isdigit() and sayı2.get().isdigit():
        s1=float(sayı1.get())
        s2=float(sayı2.get())
        sonuç.configure(text=str(s1+s2))

def çarp():
    if sayı1.get().isdigit() and sayı2.get().isdigit():
        s1=float(sayı1.get())
        s2=float(sayı2.get())
        sonuç.configure(text=str(s1*s2))

def böl():
    if sayı1.get().isdigit() and sayı2.get().isdigit():
        s1=float(sayı1.get())
        s2=float(sayı2.get())
        sonuç.configure(text=str(s1//s2))

def çıkar():
    if sayı1.get().isdigit() and sayı2.get().isdigit():
        s1=float(sayı1.get())
        s2=float(sayı2.get())
        sonuç.configure(text=str(s1-s2))



tuş1=tk.Button(form,text='+',font='Courier 14 bold',width=10,command=topla)
tuş1.place(x=90,y=110)
tuş2=tk.Button(form,text='x',font='Courier 14 bold',width=10,command=çarp)
tuş2.place(x=90,y=150)
tuş3=tk.Button(form,text='/',font='Courier 14 bold',width=10,command=böl)
tuş3.place(x=90,y=190)
tuş4=tk.Button(form,text='-',font='Courier 14 bold',width=10,command=çıkar)

tuş4.place(x=90,y=230)
form.mainloop()