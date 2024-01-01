import tkinter as tk
form=tk.Tk()
form.title('Arayüz')
form.geometry('500x300')

Email=tk.Label(text='Email:', fg='black', bg='blue', font='Times 10 bold')
Email.place(x=10,y=30)

Şifre=tk.Label(text='Şifre:', fg='black', bg='blue', font='Times 10 bold')
Şifre.place(x=10, y=60)

Email_entry=tk.Entry()
Email_entry.place(x=60,y=30)

Şifre_entry=tk.Entry(show='*')
Şifre_entry.place(x=60,y=60)


def kayıtol():
    yaş=tk.Label(text='Yaş:', fg='black', bg='blue', font='Times 10 bold')
    yaş.place(x=10,y=170)
    soyad=tk.Label(text='Soyad:', fg='black', bg='blue', font='Times 10 bold')
    soyad.place(x=10, y=150)
    ad=tk.Label(text='Ad:', fg='black', bg='blue', font='Times 10 bold')
    ad.place(x=10, y=130)
    ad_entry=tk.Entry()
    ad_entry.place(x=60,y=130)
    soyad_entry=tk.Entry()
    soyad_entry.place(x=60,y=150)
    yaş_entry=tk.Entry()
    yaş_entry.place(x=60, y=170)

def giriş():
    Email_entry.delete(0,'end')
    Şifre_entry.delete(0,'end')



kayıtol_btn=tk.Button(form, text='Kayıt ol', fg='black' ,bg='green' ,command=kayıtol)
kayıtol_btn.place(x=65, y=90)

giriş_btn=tk.Button(form, text='Giriş', fg='black', bg='green', command=giriş)
giriş_btn.place(x=150, y=90)

form.mainloop()