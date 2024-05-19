import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox

form=tk.Tk()
form.geometry('500x600')
form.title('Forma Alış')
resim=ImageTk.PhotoImage(Image.open('C:/Users/pc/Downloads/fenerbahçe.webp'))
label=tk.Label(form,image=resim)
label.pack()


def ürünler():
    label1=tk.Label(form,text='Formalar:',bg='yellow',fg='darkblue',font='verdana 10 bold')
    label1.place(x=10,y=90)

    liste1=['Çubuklu Forma','Sarı Deplasman Forması','Lacivert Alternatif Forma']
    formalar=Combobox(form,values=liste1)
    formalar.place(x=10,y=110)

    label2=tk.Label(form,text='Beden:',bg='yellow',fg='darkblue',font='verdana 10 bold')
    label2.place(x=180,y=90)

    liste2=['XL','L','M','S','XS']
    beden=Combobox(form,values=liste2)
    beden.place(x=180,y=110)

    label3=tk.Label(form,text='Şortlar:',bg='yellow',fg='darkblue',font='verdana 10 bold')
    label3.place(x=10,y=200)

    liste3=['Çubuklu Alt','Sarı Deplasman Alt','Lacivert Alternatif Alt']
    şortlar=Combobox(form,values=liste3)
    şortlar.place(x=10,y=220)

    label4=tk.Label(form,text='Beden:',bg='yellow',fg='darkblue',font='verdana 10 bold')
    label4.place(x=180,y=200)

    liste4=['XL','L','M','S','XS']
    beden2=Combobox(form,values=liste4)
    beden2.place(x=180,y=220)

    def hesap():
        if len(formalar.get())==0 or len(şortlar.get())==0 or len(beden.get())==0 or len(beden2.get())==0:
            messagebox.showinfo('Lütfen Boş Bırakma',message='Boş Alanları Doldur')
        else:
            sözlük1={'Çubuklu Forma':2000,'Sarı Deplasman Forması':2000,'Lacivert Alternatif Forma':2000}
            sözlük2={'Çubuklu Alt':700,'Sarı Deplasman Alt':700,'Lacivert Alternatif Alt':700}
            değer1=formalar.get()
            değer2=şortlar.get()

            fiyat=str(sözlük1[değer1])+str(sözlük2[değer2])==str(sözlük1[değer1])+str(sözlük2[değer2])[1:]+'TL'
            toplam=tk.Label(form,text='Toplam Fiyat 2700 TL')
            toplam.place(x=170,y=400)

    buton=tk.Button(form,text='Hesapla',command=hesap)
    buton.place(x=200,y=300)

x=tk.StringVar()
radio=tk.Radiobutton(form,text='Formalar-Şortlar',value=1,variable=x,command=ürünler)
radio.place(x=170,y=5)








form.mainloop()