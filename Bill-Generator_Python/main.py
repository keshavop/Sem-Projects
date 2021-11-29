import tkinter
from tkinter import *
from tkinter import ttk
import random
import os
import tempfile
from tkinter import messagebox

class Bill:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+5+5")
        self.root.title("Billing Software")
        
        
        #-> TITLE
        lbl_title = Label(self.root, text="Billing Software", font=("Cascadia Code", 38, "bold"), bg="slateblue1", fg="pink")
        lbl_title.place(x=0, y=0, width=1300, height=75)

        main_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        main_frame.place(x=0, y=75, width=1390, height=620)
        
        
        #-> customer details frame
        customer_frame = LabelFrame(main_frame, text="Customer Details", font=("Arial", 22, 'bold'), bg="white", fg="red")
        customer_frame.place(x=0, y=5, width=1390, height=100)
        self.nam=StringVar()
        self.mob=StringVar()
        self.ema=StringVar()
        self.label_name = Label(customer_frame, text="Name:", font=("Arial", 22), bg="white")
        self.label_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        
        self.entry_name = ttk.Entry(customer_frame, font=("Arial", 18), width=24,textvariable=self.nam)
        self.entry_name.grid(row=0, column=1)

        self.label_mobile = Label(customer_frame, text="Phone No.:", font=("Arial", 18), bg="white")
        self.label_mobile.grid(row=0, column=2, sticky=W, padx=5, pady=20)

        self.entry_mobile = ttk.Entry(customer_frame, font=("Arial", 18), width=24,textvariable=self.mob)
        self.entry_mobile.grid(row=0, column=3)

        self.label_email = Label(customer_frame, text="E-mail:", font=("Arial", 18), bg="white")
        self.label_email.grid(row=0, column=4, sticky=W, padx=5, pady=20)

        self.entry_email = ttk.Entry(customer_frame, font=("Arial", 18), width=24,textvariable=self.ema)
        self.entry_email.grid(row=0, column=5)


        #-> Product Label Frame
        product_frame = LabelFrame(main_frame, text="Product Details", font=("Arial", 22,'bold'), bg="white", fg="red")
        product_frame.place(x=5, y=105, width=600, height=300)
        self.cat=StringVar()
        self.name=StringVar()
        self.pri=StringVar()
        self.quan=StringVar()
        self.label_category=Label(product_frame,font=("arial",18),bg="white",text="Select Category",bd=4)
        self.label_category.grid(row=0,column=0)
        
        self.combo_category=ttk.Entry(product_frame,font=("arial",12,'bold'), width=15,textvariable=self.cat)
        self.combo_category.grid(row=0,column=1)
        
        self.label_category=Label(product_frame,font=("arial",18),bg="white",text="Product Name",bd=4)
        self.label_category.grid(row=2,column=0)
        
        self.combo_category=ttk.Entry(product_frame,font=("arial",12,'bold'), width=15,textvariable=self.name)
        self.combo_category.grid(row=2,column=1)
        
        self.label_category=Label(product_frame,font=("arial",18),bg="white",text="Price",bd=4)
        self.label_category.grid(row=3,column=0)
        
        self.combo_category=ttk.Entry(product_frame,font=("arial",12,'bold'), width=15,textvariable=self.pri)
        self.combo_category.grid(row=3,column=1)
        
        self.label_category=Label(product_frame,font=("arial",18),bg="white",text="Quantity",bd=4)
        self.label_category.grid(row=4,column=0)
        
        self.combo_category=ttk.Entry(product_frame,font=("arial",12,'bold'), width=15,textvariable=self.quan)
        self.combo_category.grid(row=4,column=1)
        
        
        #-> Bill show area
        self.RightLabelFrame=LabelFrame(main_frame,text="Bill Area",font=("arial", 18), bg="white",fg="blue")
        self.RightLabelFrame.place(x=800,y=150,width=400,height=400)
        
        
        #-> search bill option
        search_frame = Frame(main_frame, bd=2, bg="white")
        search_frame.place(x=800, y=110, width=500, height=40)
        j=random.randint(1111,9999)
        self.lblBill = Label(search_frame, font=("arial", 12, "bold"), fg="white", bg="red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, stick=W, padx=2)
        self.lblBill = Label(search_frame, font=("arial", 12, "bold"), fg="red", bg="white", text=j)
        self.lblBill.grid(row=0, column=1, stick=W, padx=2)
        
        
        #-> Button frame
        btn_frame = Frame(main_frame, bd=2, bg="white")
        btn_frame.place(x=30, y=420)

        self.BtnAddToCart = Button(btn_frame, text="Add To Cart", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=lambda: self.display())
        self.BtnAddToCart.grid(row=0, column=0, padx=6, pady=6)

        self.Btngenerate_bill = Button(btn_frame, text="Generate Bill", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=lambda: self.toti())
        self.Btngenerate_bill.grid(row=0, column=1, padx=6, pady=6)

        self.BtnSave = Button(btn_frame, text="clear", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=lambda: self.clean())
        self.BtnSave.grid(row=0, column=2, padx=6, pady=6)

        self.BtnPrint = Button(btn_frame, text="Print", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=lambda: self.iprint())
        self.BtnPrint.grid(row=1, column=0, padx=6, pady=6)

        self.BtnClear = Button(btn_frame, text="Exit", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=lambda: self.exiti())
        self.BtnClear.grid(row=1, column=2, padx=6, pady=6)


        self.s=3
        self.totalpr=0
        self.textbox1=Text(self.RightLabelFrame,width=490,height=440,font="30")
        self.textbox1.pack(expand=True)
        self.totals=1
    def display(self):
        self.cati=self.cat.get() 
        self.nami=self.name.get() 
        self.peri=self.pri.get() 
        self.quani=self.quan.get() 
        self.namis=self.nam.get() 
        self.mobi=self.mob.get() 
        self.emai=self.ema.get() 
        self.totalpr=self.totalpr+(int(self.peri)*int(self.quani))
        self.text="NamE==>"+self.namis+"   MOBILE NO.==>"+self.mobi+"   EMAIL==>"+self.emai


        self.text2=self.nami+"               "+self.quani+"              "+self.peri
        
        
        if self.totals==1:
            if(self.s==3):
                self.textbox1.insert('end','\t\t'+"WELCOME TO CART")
                self.textbox1.insert('end','\n NAME :'+self.namis)
                self.textbox1.insert('end','\n MOBILE NO. :'+self.mobi)
                self.textbox1.insert('end','\n EMAIL :'+self.emai)
                self.textbox1.insert('end','\n'+"Product\t       Quantity\t        Price")
                self.s=self.s+1
            self.textbox1.config(state=NORMAL)    
            self.textbox1.insert('end',f'\n'+self.text2)   
            self.textbox1.config(state=DISABLED)
            self.textbox1.yview(END) 

            self.cat.set("")
            self.name.set("")
            self.pri.set("")
            self.quan.set("")
        else:
            messagebox.showerror("billing system","total has been made you cant add more item")
            self.cat.set("")
            self.name.set("")
            self.pri.set("")
            self.quan.set("")


    def toti(self):
        self.totals+=1
        self.text4="Total Amount :: "+str(self.totalpr)+"RS"
        self.tax=self.totalpr*(18/100)
        self.gt=self.totalpr+self.tax
        self.text5="GST :: "+str(self.tax)+"RS"
        self.text6="Total amount to pay :: "+str(self.gt)+"RS"
        self.textbox1.config(state=NORMAL) 
        self.textbox1.insert('end','\n'+"-------------------------------------------------")
        self.textbox1.insert('end','\n'+self.text4)
        self.textbox1.insert('end','\n'+self.text5)
        self.textbox1.insert('end','\n'+self.text6)
        self.textbox1.config(state=DISABLED) 
        
    def iprint(self):
        q = self.textbox1.get(1.0,  "end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename, 'w').write(q)
        os.startfile(filename, "print")    
        
    def clean(self):
        self.s=self.s-1
        self.textbox1.config(state=NORMAL) 
        self.textbox1.delete("1.0","end")
    def exiti(self):
        root.quit()
root = Tk()
obj = Bill(root)
root.mainloop()