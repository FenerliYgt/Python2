import tkinter as tk
from tkinter import messagebox
form=tk.Tk()
form.title('Ortalama Hesaplayıcı')
form.geometry('300x300')
form.config(bg='black')

başlık=tk.Label(form,text='Ortalama Hesaplayıcı',bg='black',fg='white',font='Times 17 bold')
başlık.pack()

kullanıcı_adı=tk.Label(form,text='Kullanıcı Adı:',bg='black',fg='white',font='Times 12 bold')
kullanıcı_adı.place(x=20,y=90)

şifre=tk.Label(form,text='Şifre:',bg='black',fg='white',font='Times 12 bold')
şifre.place(x=20,y=130)

kullanıcı_entry=tk.Entry(form)
kullanıcı_entry.place(x=120,y=95)

şifre_entry=tk.Entry(form,show='*')
şifre_entry.place(x=120,y=130)

def giriş():
    if kullanıcı_entry.get()=='Yiğit' and şifre_entry.get()=='1234':
        msg1=messagebox.showinfo('Tebrikler',message='Giriş Başarılı')
        if msg1=='ok':
            not_sayfası=tk.Toplevel()
            not_sayfası.geometry('500x350')
            not_sayfası.title('Not Sayfası')
            not_sayfası.config(bg='darkblue')
            sonuç=tk.Label(not_sayfası,text='',bg='darkblue',fg='white',font='Courier 16 bold',width=30,justify='center')
            sonuç.place(x=40,y=20)

            sınav1=tk.Label(not_sayfası,text='1. Sınav:',bg='darkblue',fg='white',font='Times 12 bold')
            sınav1.place(x=30,y=60)
            sınav2=tk.Label(not_sayfası,text='2. Sınav:',bg='darkblue',fg='white',font='Times 12 bold')
            sınav2.place(x=30,y=120)
            sınav3=tk.Label(not_sayfası,text='3. Sınav:',bg='darkblue',fg='white',font='Times 12 bold')
            sınav3.place(x=30,y=180)
            sınav4=tk.Label(not_sayfası,text='4. Sınav:',bg='darkblue',fg='white',font='Times 12 bold')
            sınav4.place(x=30,y=240)
            
            sınav1_entry=tk.Entry(not_sayfası,font='Courier 14 bold',width=10)
            sınav1_entry.place(x=100,y=60)
            sınav2_entry=tk.Entry(not_sayfası,font='Courier 14 bold',width=10)
            sınav2_entry.place(x=100,y=120)
            sınav3_entry=tk.Entry(not_sayfası,font='Courier 14 bold',width=10)
            sınav3_entry.place(x=100,y=180)
            sınav4_entry=tk.Entry(not_sayfası,font='Courier 14 bold',width=10)
            sınav4_entry.place(x=100,y=240)

            def hesapla():

                if sınav1_entry.get().isdigit() and sınav2_entry.get().isdigit() and sınav3_entry.get().isdigit and sınav4_entry.get().isdigit():
                    s1=float(sınav1_entry.get())
                    s2=float(sınav2_entry.get())
                    s3=float(sınav3_entry.get())
                    s4=float(sınav4_entry.get())
                    sonuç.configure(text=str((s1+s2+s3+s4)//4))

            buton2=tk.Button(not_sayfası,text='Hesapla',activebackground='green',command=hesapla)
            buton2.pack(side=tk.BOTTOM, fill=tk.X)

            not_sayfası.mainloop()
    else:
        msg2=messagebox.showerror('Hata',message='Kullanıcı Adı Veya Şifre Hatalı Tekrar Deneyin')

buton1=tk.Button(form,text='Giriş',activebackground='green',command=giriş)
buton1.place(x=150,y=180,width=60)






form.mainloop()