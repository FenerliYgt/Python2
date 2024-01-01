import tkinter as tk
form=tk.Tk()
form.title('Hesaplayıcı')
form.geometry('500x100')
a=float(input("1. Sınav Notunu Gir:"))
b=float(input("2. Sınav Notunu Gir:"))
c=float(input("3. Sınav Notunu Gir:"))
d=(a+b+c)//3
print(float(d))

def a():
    label.config( text=a ,bg='blue')

def b():
    label.config( text=b ,bg='blue')

def c():
    label.config( text=c ,bg='blue')

def d():
    label.config(text=d ,bg='blue')


label=tk.Label(form , fg='red' ,bg='red')
label.pack()

göster=tk.Button(form, text='Hesapla', bg='black' ,fg='yellow' ,command=a)
göster.pack(side=tk.LEFT)
















form.mainloop()