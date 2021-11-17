import tkinter
from tkinter import *
from tkinter import ttk


class Bill:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+5+5")
        self.root.title("Billing Software")
        
        #-> TITLE
        lbl_title = Label(self.root, text="Billing Software", font=(
            "Cascadia Code", 36, "bold"), bg="slateblue1", fg="pink")
        lbl_title.place(x=0, y=0, width=1400, height=75)

        main_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        main_frame.place(x=0, y=75, width=1400, height=910)

        #-> customer details frame
        customer_frame = LabelFrame(main_frame, text="Customer Details", font=("Arial", 18), bg="white", fg="red")
        customer_frame.place(x=0, y=5, width=1390, height=100)

        self.label_name = Label(customer_frame, text="Name :", font=("Arial", 16), bg="white")
        self.label_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        
        self.entry_name = ttk.Entry(customer_frame, font=("Arial", 16), width=24)
        self.entry_name.grid(row=0, column=1)

        self.label_mobile = Label(customer_frame, text="Phone No. :", font=("Arial", 16), bg="white")
        self.label_mobile.grid(row=0, column=2, sticky=W, padx=20, pady=20)

        self.entry_mobile = ttk.Entry(customer_frame, font=("Arial", 16), width=24)
        self.entry_mobile.grid(row=0, column=3)

        self.label_email = Label(customer_frame, text="E-mail :", font=("Arial", 16), bg="white")
        self.label_email.grid(row=0, column=4, sticky=W, padx=20, pady=20)

        self.entry_email = ttk.Entry(customer_frame, font=("Arial", 16), width=24)
        self.entry_email.grid(row=0, column=5)




if __name__ == '__main__':
    root = Tk()
    obj = Bill(root)
    root.mainloop()