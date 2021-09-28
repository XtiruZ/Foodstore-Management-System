import random
import time
import datetime
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background='Cadet Blue')


Tops=Frame(root,bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops, font=('arial', 60, 'bold'),
text="Restaurant Management Systems",
bd=21,bg='Cadet Blue', fg='Cornsilk', 
justify=CENTER)

lblTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE) 
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)


MenuFrame=Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10) 
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

# === Frames ===
Latta=Checkbutton(Drinks_F, text="Latta", variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=0, sticky=W)
Espresso=Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=1, sticky=W)
Iced_Latta=Checkbutton(Drinks_F, text="Iced_Latta", variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=2, sticky=W)
Vale_Coffee=Checkbutton(Drinks_F, text="Vale_Coffee", variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=3, sticky=W)
Cappuccino=Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=4, sticky=W)
African_Coffee=Checkbutton(Drinks_F, text="African_Coffee", variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=5, sticky=W)
American_Coffee=Checkbutton(Drinks_F, text="American_Coffee", variable=var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=6, sticky=W)
Iced_Cappuccino=Checkbutton(Drinks_F, text="Iced_Cappuccino", variable=var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=7, sticky=W)

# === Entries Drinks ===
txtLatta = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtLatta.grid(row=0, column=1)
txtEspresso = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtEspresso.grid(row=1, column=1)
txtIced_Latta = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtIced_Latta.grid(row=2, column=1)

txtVale_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)
txtCappucino = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtCappucino.grid(row=4, column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)

txtAmerican_Coffee = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)
txtIced_Cappucino = Entry(Drinks_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtIced_Cappucino.grid(row=7, column=1)


# === Cakes ===

SchoolCake=Checkbutton(Cake_F, text="School Cake\t\t\t", variable=var9, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=0, sticky=W)
Sunny_AO_Cake=Checkbutton(Cake_F, text="Sunday O Cake", variable=var10, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=1, sticky=W)
Jonathan_YO_Cake=Checkbutton(Cake_F, text="Jonathan O Cake", variable=var11, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=2, sticky=W)
West_African_Cake=Checkbutton(Cake_F, text="West African Cake", variable=var12, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=3, sticky=W)
Lagos_Chocolate_Cake=Checkbutton(Cake_F, text="Lagos_Chocolate_Cake", variable=var13, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=4, sticky=W)
Killburn_Chocolate_Cake=Checkbutton(Cake_F, text="Killburn Chocolate Cake", variable=var14, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=5, sticky=W)
Carlton_Hill_Cake=Checkbutton(Cake_F, text="Carlton Hill Cake", variable=var15, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=6, sticky=W)
Queen_Park_Cake=Checkbutton(Cake_F, text="Queen Park Cake", variable=var16, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
bg='Powder Blue').grid(row=7, sticky=W)

# === Entries Cake ===

txtSchool_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtSchool_Cake.grid(row=0, column=1)

txtSunny_AO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtSunny_AO_Cake.grid(row=1, column=1)

txtJonathan_YO_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtJonathan_YO_Cake.grid(row=2, column=1)

txtWest_African_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtWest_African_Cake.grid(row=3, column=1)

txtLagos_ChocoLate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtLagos_ChocoLate_Cake.grid(row=4, column=1)

txtKillburn_Chocolate_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtKillburn_Chocolate_Cake.grid(row=5, column=1)

txtCarlton_Hill_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtCarlton_Hill_Cake.grid(row=6, column=1)

txtQueen_Park_Cake = Entry(Cake_F,font=('arial', 16, 'bold'),bd=8, width=6, justify=LEFT, state=DISABLED)
txtQueen_Park_Cake.grid(row=7, column=1)

# === Receipt ===

txtReceipt = Text(Receipt_F,width=46,height=12,bg="white",bd=4,font=('arial', 12, 'bold'))
txtReceipt.grid(row=0,column=0)

# === Receipt buttons ===

btnTotal = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial', 16, 'bold'),width=4,text="Total",
bg="dark green").grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial', 16, 'bold'),width=4,text="Receipt",
bg="dark green").grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial', 16, 'bold'),width=4,text="Reset",
bg="dark green").grid(row=0,column=2)
btnExit = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial', 16, 'bold'),width=4,text="Exit",
bg="dark green").grid(row=0,column=3)


root.mainloop()
