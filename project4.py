from tkinter import *
import sqlite3
import tkinter.messagebox
from project5 import *

conn = sqlite3.connect('Project.db')
c = conn.cursor()

ids = [1,2,3,4,5,6,7]
class Application:
    def __init__(self,master):
        # Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('Project.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM acco WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.deliv()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('Project.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        if self.n_username.get()!=' ' and self .n_password.get()!=' ':
            find_user = ('SELECT * FROM acco WHERE username = ?')
            c.execute(find_user,[(self.n_username.get())]) 

            if c.fetchall():
                ms.showerror('Error!','Username Taken Try a Diffrent One.')
            else:
                insert = 'INSERT INTO acco(username,password) VALUES(?,?)'
                c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
                db.commit()
                
                ms.showinfo('Success!','Account Created!')
                self.log()
        #Create New Account 
        

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10,bg="black")
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' New User',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10,bg="black")
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.prod).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    def prod(self): 
        root2 = Tk()
        root2.geometry('1250x720+0+0')
        self.root2=root2        
   
        self.left = Frame(root2, width=1280, height=720, bg="black")
        self.left.pack(side=LEFT)

        self.heading = Label(self.left, text="Customer Details", font=('arial 40 bold'), fg="steel blue")
        self.heading.place(x=400,y=0)

        self.id = Label(self.left, text='Customer id', font=('arial 18 bold'), fg='black' )
        self.id.place(x=20,y=150)

        self.name = Label(self.left, text='Customer Name', font=('arial 18 bold'),fg = 'black')
        self.name.place(x=20,y=210)

        self.mno = Label(self.left, text='Mobile No.', font=('arial 18 bold'),fg = 'black')
        self.mno.place(x=20,y=270)

        self.addr = Label(self.left, text='Address', font=('arial 18 bold'),fg = 'black')
        self.addr.place(x=20,y=330)

        self.id_ent = Entry(self.left, width=35, bg='cyan')
        self.id_ent.place(x=250,y=155)

        self.name_ent = Entry(self.left, width=35, bg='cyan')
        self.name_ent.place(x=250,y=215)

        self.phn_ent = Entry(self.left, width=35, bg='cyan')
        self.phn_ent.place(x=250,y=275)

        self.addr_ent = Entry(self.left, width=35, bg='cyan')
        self.addr_ent.place(x=250,y=335)

        self.submit = Button(self.left, text="Submit", width=20, height=2, bg='light yellow', command=self.Perform)
        self.submit.place(x=250, y=395)

        sql2 = "SELECT cid FROM customer"
        self.result = c.execute(sql2)

        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
     

    def Perform(self):
        self.val1 = self.id_ent.get()
        self.val2 = self.name_ent.get()
        self.val3 = self.phn_ent.get()
        self.val4 = self.addr_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
            tkinter.messagebox.showinfo("warning", "please fill up all the details")
            
        else:
            sql = "INSERT INTO 'customer' (cid,cname,phno,address) VALUES(?,?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4))
            conn.commit()
            tkinter.messagebox.showinfo(" ","success" )
            
    
            root1 = Tk()
            root1.geometry('1250x720+0+0')
            self.root1=root1

            self.left = Frame(root1, width=1280, height=720, bg="black")
            self.left.pack(side=LEFT)

            self.heading1 = Label(self.left, text="Product Details", font=('arial 40 bold'), fg="steel blue")
            self.heading1.place(x=400,y=0)
        
            self.pid = Label(self.left, text='Product id', font=('arial 18 bold'), fg='black' )
            self.pid.place(x=20,y=150)

            self.pname = Label(self.left, text='Product Name', font=('arial 18 bold'),fg = 'black')
            self.pname.place(x=20,y=210)

            self.qty = Label(self.left, text='Quantity.', font=('arial 18 bold'),fg = 'black')
            self.qty.place(x=20,y=270)

            self.price = Label(self.left, text='Price', font=('arial 18 bold'),fg = 'black')
            self.price.place(x=20,y=330)

            self.pcid = Label(self.left, text='Customer Id for Verification', font=('arial 18 bold'),fg = 'black')
            self.pcid.place(x=20,y=390)

            self.pid_ent = Entry(self.left, width=35, bg='cyan')
            self.pid_ent.place(x=400,y=155)

            self.pname_ent = Entry(self.left, width=35, bg='cyan')
            self.pname_ent.place(x=400,y=215)

            self.qty_ent = Entry(self.left, width=35, bg='cyan')
            self.qty_ent.place(x=400,y=275)

            self.price_ent = Entry(self.left, width=35, bg='cyan')
            self.price_ent.place(x=400,y=335)

            self.pcid_ent = Entry(self.left, width=35, bg='cyan')
            self.pcid_ent.place(x=400,y=395)

            self.submit = Button(self.left, text="Submit", width=20, height=2, bg='light yellow', command=self.Perform2)
            self.submit.place(x=290, y=455)

            sql4 = "SELECT pid FROM product"
            self.result = c.execute(sql4)

    def Perform2(self):
        self.val1 = self.pid_ent.get()
        self.val2 = self.pname_ent.get()
        self.val3 = self.qty_ent.get()
        self.val4 = self.price_ent.get()
        self.val5 = self.pcid_ent.get()



        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
            tkinter.messagebox.showinfo("warning", "please fill up all the details")
        else:
            sql = "INSERT INTO 'product' (pid,pname,qauntity,price,pcid) VALUES(?,?,?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4,self.val5))
            conn.commit()
            tkinter.messagebox.showinfo(" ","success" )

    def deliv(self):
        root3= Tk()
        root3.geometry('1250x720+0+0')
        self.root3=root3
   
        self.left = Frame(root3, width=1280, height=720, bg="black")
        self.left.pack(side=LEFT)

        self.heading = Label(self.left, text="Delivery Details", font=('arial 40 bold'), fg="steel blue")
        self.heading.place(x=400,y=0)

        self.id = Label(self.left, text='Enter the product id', font=('arial 18 bold'), fg='black' )
        self.id.place(x=20,y=150)

        self.id_ent = Entry(self.left, width=35, bg='cyan')
        self.id_ent.place(x=270,y=155)

        self.ok = Button(self.left, text="OK", width=20, height=2, bg='light yellow',command=self.display)
        self.ok.place(x=350, y=200)
    
    def display(self):
        self.input=self.id_ent.get()

        sql="SELECT status,del_location FROM delivery WHERE dpid=?"
        self.res=c.execute(sql,self.input)
        for self.row in self.res:
            self.id1=self.row[0]
            self.dell=self.row[1]

        self.abcd=self.dell
        

        
        self.uid1 = Label(self.left,text="Delivery Status", font=('arial 18 bold'))
        self.uid1.place(x=0,y=260)

        self.dell = Label(self.left,text="Delivery location", font=('arial 18 bold'))
        self.dell.place(x=0,y=320)

        self.uid2= Label(self.left,text=self.id1, font=('arial 18 bold'))
        self.uid2.place(x=300,y=260)

        self.uid3 = Label(self.left,text="days left", font=('arial 18 bold'))
        self.uid3.place(x=320,y=260)

        self.del2 = Label(self.left,text=self.abcd, font=('arial 18 bold'))
        self.del2.place(x=300,y=320)
        
 

root = Tk()     
b = Application(root)
root.geometry('1250x720+0+0')
root.resizable(False,False)
root.mainloop()
