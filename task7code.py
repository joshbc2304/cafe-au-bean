from tkinter import * #imports all from tkinter
from tkinter import messagebox#Imports tkinter messagebox
import tkinter as tk#imports tkinter as "tk" to be used throughout code

def calc(): #defines the function "calc" 
    if (str(quantity.get()).isnumeric() == True and str(quantity2.get()).isnumeric() == True and str(quantity3.get()).isnumeric() == True and str(quantity4.get()).isnumeric() == True): #if the quantity in the spinbox contains letters it will return true allowing the function to continue
        global totaldrink,totaldrink2,totaldrink3,totaldrink4,dailytotal #declares global variables to be used everywhere throughout function
        totaldrink = int(quantity.get()) + totaldrink #creates variable that stores the amount of drinks sold for the duration of the program running unless reset
        totaldrink2 = int(quantity2.get()) + totaldrink2  #creates variable that stores the amount of drinks sold for the duration of the program running unless reset
        totaldrink3 = int(quantity3.get()) + totaldrink3  #creates variable that stores the amount of drinks sold for the duration of the program running unless reset
        totaldrink4 = int(quantity4.get()) + totaldrink4  #creates variable that stores the amount of drinks sold for the duration of the program running unless reset
        total = int((quantity.get()))*3+int((quantity2.get()))*2.25+int((quantity3.get()))*2.5+int((quantity4.get()))*2.50#calcalates price per drink and adds them all together
    elif  (str(quantity.get()).isnumeric() == False or str(quantity2.get()).isnumeric() == False or str(quantity3.get()).isnumeric() == False or str(quantity4.get()).isnumeric() == False): #if the quantity in the spinbox contains letters it will return false displaying messagebox and resetting the code
        messagebox.showwarning("WARNING","DON'T TYPE LETTERS IN THERE PLEASE") #displays error if you typed a letter in the spinbox
        for order in [orders, orders2, orders3, orders4]:order.set(0)#sets checkbox to 0 #resets all the spinboxes to 0
        total1.set("Total Amount Due: $0.00") #sets total label to that
        return #stops the function
    if checked.get() ==1: #if the tax box is checked it will multiply the total by the tax rate
        totaltax = total*1.05 #creates total with tax added
        total1.set("Total Amount Due: $"+str(("%.2f" %totaltax)))
        dailytotal=totaltax+dailytotal #updates total amount due label
    else:
        total1.set("Total Amount Due: $"+str(("%.2f" %total)))#updates total amount due label
        dailytotal=total+dailytotal #updates dailytotal with new total 
    for order in [orders, orders2, orders3, orders4, checked]:order.set(0)#sets orders and checkbox to 0 

def cancel1(): #defines function called "cancel1"
    for order in [orders, orders2, orders3, orders4, checked]:order.set(0)#sets orders and checkbox to 0 
    total1.set("Total Amount Due: $0.00")#sets total to $0

def reset():  #defines function called "reset"
    global total1,totaldrink,totaldrink2,totaldrink3,totaldrink4,dailytotal #declares variables as global to be used throughout entire code
    for order in [orders, orders2, orders3, orders4, checked]:order.set(0)#sets checkbox to 0
    total1.set("Total Amount Due: $0.00")#sets total to 0 
    totaldrink,totaldrink2,totaldrink3,totaldrink4,dailytotal = 0,0,0,0,0 #resets variables to 0 
    
def stats2(): #defines function called "stats2"
    messagebox.showinfo("Daily Stats"," Daily Total: $"+str("%.2f" %dailytotal)+"\n Cappuccino: "+str(totaldrink)+"\n Espresso: "+str(totaldrink2)+"\n Latte: "+str(totaldrink3)+"\n Iced: "+str(totaldrink4))
  
window = Tk() #initalizes the tkinter window widget where all the widgets appear
window.iconbitmap('Capture.ico') #icon on the top left of the program
window.title("Café au Bean POS") #title next to the logo at the top 
window.geometry("275x275") #size of the window (in pixels)

orders,orders2,orders3,orders4,checked,total1 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),StringVar() #declares variables as intvars and a string var 
dailytotal,totaldrink,totaldrink2,totaldrink3,totaldrink4,totaltax = 0,0,0,0,0,0 #declares 6 variables and sets them to 0

title= Label(window, text="Welcome to Café au Bean",font='Helvetica 12 bold').place(x=32,y=10) #places the title in those spacial coordinates
qty=Label(window, text="QTY",font='Helvetica 9 bold').place(x=182,y=40)#places QTY label
menu = Label(window, text=""" \n          Cappuccino $3.00 \n \n             Espresso $2.25\n\n                      Latte $2.50\n\n                       Iced $2.50""",font="Helvetica 9").place(x=33, y = 43) #places the menu in the right spot to line up with the spinboxes
totalprice = Label(window, textvariable=total1, bg="pink", relief="ridge",font="Helvetica 12").place(x=46, y=245),total1.set("Total Amount Due: $0.00") #places label at those coordinates   
takeawaylabel = Label(window, text='Takeaway? (5% surcharge)',font="Helvetica 9").place(x=16,y=180) #places label

quantity = Spinbox(from_= 0, to = 10, width=2, bg="pink",textvariable=orders) #creates spinbox
quantity.place(x=185, y=60)#places spinbox where i want it
quantity2 = Spinbox(from_= 0, to = 10, width=2, bg="pink",textvariable=orders2)#creates spinbox
quantity2.place(x=185, y=90)#places spinbox where i want it
quantity3 = Spinbox(from_= 0, to = 10, width=2, bg="pink",textvariable=orders3)#creates spinbox
quantity3.place(x=185, y=120)#places spinbox where i want it
quantity4 = Spinbox(from_= 0, to = 10, width=2, bg="pink",textvariable=orders4)#creates spinbox
quantity4.place(x=185, y=150)#places spinbox where i want it

takeaway = Checkbutton(window, variable=checked,bg="pink",relief="groove").place(x=184,y=178)#places checkbox
order = Button(window, text = "Order",command=calc, bg="pink",font="Helvetica 8 bold").place(x=4, y=210) #places order button
cancel = Button(window, text ="Cancel Order",command=cancel1, bg="pink",font="Helvetica 8 bold").place(x=49, y=210)#places button 
resetday = Button(window, text="Reset ALL", command=reset, bg="pink",font="Helvetica 8 bold").place(x=134, y=210)#places button
stats = Button(window, text="Print Stats",command=stats2, bg="pink",font="Helvetica 8 bold").place(x=204,y=210)#places button

window.mainloop()#tells python to execute the code