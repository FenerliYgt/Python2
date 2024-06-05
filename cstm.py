import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

window=ctk.CTk()
window.title('')
window.geometry('600x400')

stringvar=tk.StringVar(value='a')
label=ctk.CTkLabel(window,text='customtkinter',fg_color=('blue','red'),text_color=('black','white'),corner_radius=10,textvariable=stringvar)
label.pack()

buton=ctk.CTkButton(window,text='ctk',fg_color='#FF0',text_color='#000',hover_color='#AA0',command=lambda: ctk.set_appearance_mode('light'))
buton.pack()

frame=ctk.CTkFrame(window)
frame.pack()

slider=ctk.CTkSlider(frame)
slider.pack(padx=20,pady=10)

switch=ctk.CTkSwitch(window,text='exercise',fg_color=('blue','red'),progress_color='pink',button_color='green',button_hover_color='yellow',switch_width=60,switch_height=30,corner_radius=2)
switch.pack()


window.mainloop()