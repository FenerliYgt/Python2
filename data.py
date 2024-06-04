import tkinter 
from tkinter import ttk
import os
import openpyxl 

pencere=tkinter.Tk()
pencere.title('Data Entry Form')

def enter_data():

    firstname=ilk_isim_entry.get()
    lastname=soy_isim_entry.get()
    title=başlık_combobox.get()
    age=yaş_spinbox.get()
    nationality=milliyet_combobox.get()
                
    registration=kayıt_durumu_var.get()
    numcourses=ders_sayısı_spinbox.get()
    numsemesters=semester_sayısı_spinbox.get()

    print('İsim:',firstname,'Soy İsim:',lastname)
    print('Unvan:',title,'Yaş:',age,'Milliyet:',nationality)
    print('# Dersler:',numcourses,'# Semester',numsemesters)
    print('Kayıt Durumu:',registration)
    print('-----------------------------------------------')

    filepath= "C://Users//pc//OneDrive//Masaüstü//data.xlsx"

    if not os.path.exists(filepath):
        workbook=openpyxl.Workbook()
        sheet=workbook.active
        heading=["İsim","Soy İsim","Unvan","Milliyet","Yaş","# Tamamlanan Dersler","# Semester","Kayıt Durumu"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook=openpyxl.load_workbook(filepath)
    sheet=workbook.active
    sheet.append([firstname,lastname,title,age,nationality,numcourses,numsemesters,registration])
    workbook.save(filepath)
        





çerçeve=tkinter.Frame(pencere)
çerçeve.pack()


kullanıcı_bilgi_çerçevesi=tkinter.LabelFrame(çerçeve,text='Kullanıcı Bilgileri')
kullanıcı_bilgi_çerçevesi.grid(row=0,column=0,padx=20,pady=10)

ilk_isim=tkinter.Label(kullanıcı_bilgi_çerçevesi,text='İsim')
ilk_isim.grid(row=0,column=0)

soy_isim=tkinter.Label(kullanıcı_bilgi_çerçevesi,text='Soy İsim')
soy_isim.grid(row=0,column=1)

ilk_isim_entry=tkinter.Entry(kullanıcı_bilgi_çerçevesi)
ilk_isim_entry.grid(row=1,column=0)
soy_isim_entry=tkinter.Entry(kullanıcı_bilgi_çerçevesi)
soy_isim_entry.grid(row=1,column=1)

başlık=tkinter.Label(kullanıcı_bilgi_çerçevesi,text='Unvan')
başlık_combobox=ttk.Combobox(kullanıcı_bilgi_çerçevesi,values=['','Bay','Bayan','Dr.'])
başlık.grid(row=0,column=2)
başlık_combobox.grid(row=1,column=2)

yaş=tkinter.Label(kullanıcı_bilgi_çerçevesi,text='Yaş')
yaş_spinbox=tkinter.Spinbox(kullanıcı_bilgi_çerçevesi,from_=18,to=110)
yaş.grid(row=2,column=0)
yaş_spinbox.grid(row=3,column=0)

milliyet=tkinter.Label(kullanıcı_bilgi_çerçevesi,text='Milliyet')
milliyet.grid(row=2,column=1)
milliyet_combobox=ttk.Combobox(kullanıcı_bilgi_çerçevesi,values=[''])
milliyet_combobox.grid(row=3,column=1)

for widget in kullanıcı_bilgi_çerçevesi.winfo_children():
    widget.grid_configure(padx=10,pady=5)

dersler_çerçeve=tkinter.LabelFrame(çerçeve)
dersler_çerçeve.grid(row=1,column=0,sticky='news',padx=20,pady=10)

kayıt=tkinter.Label(dersler_çerçeve,text='Kayıt Durumu')
kayıt.grid(row=0,column=0)

kayıt_durumu_var=tkinter.StringVar(value='Kayıtlı Değil')
kayıt_check=tkinter.Checkbutton(dersler_çerçeve,text='Kayıtlı',variable=kayıt_durumu_var,onvalue='Kayıtlı',offvalue='Kayıtlı Değil')
kayıt_check.grid(row=1,column=0)

ders_sayısı=tkinter.Label(dersler_çerçeve,text='# Tamamlanan Dersler')
ders_sayısı.grid(row=0,column=1)
ders_sayısı_spinbox=tkinter.Spinbox(dersler_çerçeve,from_=0,to='infinity')
ders_sayısı_spinbox.grid(row=1,column=1)

semester_sayısı=tkinter.Label(dersler_çerçeve,text='# Semester')
semester_sayısı.grid(row=0,column=2)
semester_sayısı_spinbox=tkinter.Spinbox(dersler_çerçeve,from_=0,to='infinity')
semester_sayısı_spinbox.grid(row=1,column=2)

for widget in dersler_çerçeve.winfo_children():
    widget.grid_configure(padx=20,pady=5)

şarlar_çerçevesi=tkinter.LabelFrame(çerçeve,text='Şartlar & Koşullar')
şarlar_çerçevesi.grid(row=2,column=0,sticky='news',padx=20,pady=10)


şarlar_check=tkinter.Checkbutton(şarlar_çerçevesi,text='Şartları ve koşulları kabul ediyorum.')
şarlar_check.grid(row=0,column=0)

buton=tkinter.Button(çerçeve,text='Veri gir',command=enter_data)
buton.grid(row=3,column=0, sticky='news',padx=20,pady=20)







pencere.mainloop()