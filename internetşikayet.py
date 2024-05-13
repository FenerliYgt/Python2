import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import kullanıcı_dogrulama

form=tk.Tk()
form.geometry('300x300')
form.config(bg='black')
form.title('Arıza Uygulamsı')

lbl_baslık=tk.Label(form,text='Arıza Bildirim Uygulaması',bg='black',fg='white',font='Times 17 bold')
lbl_baslık.pack()

lbl_ad=tk.Label(form,text='Kullanıcı Adı:',bg='black',fg='white',font='Times 12 bold')
lbl_ad.place(x=20,y=90)

lbl_ad=tk.Label(form,text='Şifre:',bg='black',fg='white',font='Times 12 bold')
lbl_ad.place(x=20,y=130)


entry_ad=tk.Entry(form)
entry_ad.place(x=120,y=95)

entry_sifre=tk.Entry(form,show='*')
entry_sifre.place(x=120,y=135)

def giris():
    if entry_ad.get()=='yigit' and  entry_sifre.get()=='1234':
        msg=messagebox.showinfo('Tebrikler',message='Giriş Başarılı')
        if msg=='ok':
            basvuru_formu=tk.Toplevel()
            basvuru_formu.geometry('350x350')
            basvuru_formu.title('Arıza Bildiri Formu')
            basvuru_formu.config(bg='yellow')
            baslık_label=tk.Label(basvuru_formu,text='Arıza Bildirim Formu',bg='yellow',fg='darkblue',font='Times 20 bold')
            baslık_label.pack()

            label_ad=tk.Label(basvuru_formu,text='Ad-Soyad:',font='consoles 12 italic',bg='yellow',fg='black')
            label_ad.place(x=40,y=50)

            label_kullanıcı=tk.Label(basvuru_formu,text='Kullanıcı No:',font='consoles 12 italic',bg='yellow',fg='black')
            label_kullanıcı.place(x=40,y=90)

            label_modem=tk.Label(basvuru_formu,text='Modem Tipi:',font='consoles 12 italic',bg='yellow',fg='black')
            label_modem.place(x=40,y=130)

            label_arıza=tk.Label(basvuru_formu,text='Arıza Tipi:',font='consoles 12 italic',bg='yellow',fg='black')
            label_arıza.place(x=40,y=170)

            label_adres=tk.Label(basvuru_formu,text='Adres:',font='consoles 12 italic',bg='yellow',fg='black')
            label_adres.place(x=40,y=210)

            label_mail=tk.Label(basvuru_formu,text='Mail:',font='consoles 12 italic',bg='yellow',fg='black')
            label_mail.place(x=40,y=250)
            
            entry_ad_soyad=tk.Entry(basvuru_formu)
            entry_ad_soyad.place(x=140,y=50)

            entry_kullanıcı=tk.Entry(basvuru_formu)
            entry_kullanıcı.place(x=140,y=90)
            
            liste=['Tmp','KMNR','2TMNx','MTPL','NMPY','PNDAS']
            combo_modem=Combobox(basvuru_formu,values=liste)
            combo_modem.place(x=140,y=130)

            liste1=['kablo','wifi','giriş','internet','NMPY','PNDAS']
            combo_arıza=Combobox(basvuru_formu,values=liste1)
            combo_arıza.place(x=140,y=170)
            

            entry_adres=tk.Entry(basvuru_formu)
            entry_adres.place(x=140,y=210)

            entry_mail=tk.Entry(basvuru_formu)
            entry_mail.place(x=140,y=250)

            def olustur():
                kosul=kullanıcı_dogrulama.kullanıcı(entry_kullanıcı.get())
                if kosul==True:
                    msgm=messagebox.showinfo('Başarıyla Oluştu',message='Arıza Bildiriminiz Gerçekleştirildi')
                else:
                    messagebox.showerror('Başarısız','Kullanıcı Adını Doğru Girdiğinizden Emin Olun')


                
            buton=tk.Button(basvuru_formu,text='Oluştur',command=olustur)
            buton.place(x=140,y=290)

            basvuru_formu.mainloop()

            

def iptal():
    pass

btn_giris=tk.Button(form,text='Giriş',activebackground='green',command=giris)
btn_giris.place(x=120,y=180,width=60)

btn_iptal=tk.Button(form,text='İptal',activebackground='red',command=iptal)
btn_iptal.place(x=190,y=180,width=60)



form.mainloop()