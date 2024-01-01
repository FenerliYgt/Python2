import tkinter as tk 

form = tk.Tk()
form.title('Ortalama Hesaplayıcı')
label=tk.Label(text='Ortalama Hesaplayıcı')
label=tk.Button(form,text='hesapla')
label.pack()
label2=tk.Label(form,text='Hesaplayıcı')
label2.pack()
label3=tk.Label(form,text='İngilizce',fg='red')
label3.pack()
label4=tk.Label(form,text='İngilizce Ortalama',fg='black',bg='green')
label4.pack()
label5=tk.Label(form,text='xx',fg='red',bg='green',font='Times 15 italic')
label5.pack()
label6=tk.Label(form,text='En son ders',fg='green',bg='red',font='Times 17 bold')
label6.pack()
form.mainloop()



