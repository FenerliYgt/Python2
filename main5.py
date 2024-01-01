import tkinter as tk
import random as rd 

form=tk.Tk()
form.title('Tekrar Uygulaması')
form.geometry('500x400+500+350')
liste=[]
for i in range(5):
    while len(liste)!=6:
        a=rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste, bg='green')
def saydamlaştır():
    form.wm_attributes('-alpha',0.3)

def Döndür():
    form.wm_attributes('-alpha',0.9)

def MaxYap():
    form.state('zoomed')
def MinYap():
    form.state('iconic')

    
label=tk.Label(form,fg='red', bg='red')
label.pack()


göster=tk.Button(form,text='Göster' ,fg='black',bg='yellow',command=göster)
göster.pack(side=tk.LEFT)

göster=tk.Button(form,text='Saydamlaştır' ,fg='black',bg='yellow',command=saydamlaştır)
göster.pack(side=tk.LEFT)

göster=tk.Button(form,text='Döndür' ,fg='black',bg='yellow',command=Döndür)
göster.pack(side=tk.LEFT)

göster=tk.Button(form,text='MaxYap' ,fg='black',bg='yellow',command=MaxYap)
göster.pack(side=tk.LEFT)

göster=tk.Button(form,text='MinYap' ,fg='black',bg='yellow',command=MinYap)
göster.pack(side=tk.LEFT)




form.mainloop()