from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from customtkinter import *
from datetime import datetime
from persiantools.jdatetime import JalaliDate
from be.bePersonal import Personal
from be.beCar import Car
from be.bePersonal import Login
from be.beCar import Login
from bll.blPersonal import blPersonal
from bll.blCar import blCar


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master=screen
        self.CreateWidget()
        #تابع المان ها و ویجت های صفحه

    def CreateWidget(self):
        style=ttk.Style()
        style.theme_use("clam")





        self.outtime=[]





        self.image0 = PhotoImage(file="img/c0.png")
        self.image1 = PhotoImage(file="img/c1.png")
        self.image2 = PhotoImage(file="img/c2.png")
        self.image3 = PhotoImage(file="img/c3.png")
        self.image4 = PhotoImage(file="img/c4.png")
        self.image5 = PhotoImage(file="img/c5.png")
        self.Menu = PhotoImage(file="img/menu.png")


        self.frmMenu = CTkFrame(self.master).place(x=550, y=10)
        self.lblMenu = CTkLabel(self.master).place(x=800, y=10)
        self.btnMenu = CTkButton(self.master).place(x=550, y=10)
        self.frmMenu = CTkFrame(self.master, bg_color="purple", height=680, width=200)
        self.frmMenu.place_forget()
        self.lblPerson = CTkLabel(self.master, text="Expert", font=('tanha', 12), bg_color="#e8271a", fg_color="#211C6A", width=50).place(x=1120, y=55)
        self.lblNumber = CTkLabel(self.master, text="Number", font=('tanha', 12), bg_color="#e8271a", fg_color="#211C6A", width=60).place(x=1120, y=105)
        self.lblDate = CTkLabel(self.master, text="Order Date", font=('tanha', 12), bg_color="#e8271a", fg_color="#211C6A", width=70).place(x=1120, y=155)
        self.lbl1 = CTkLabel(self.master, text= "to order", bg_color="#84959c", fg_color="#777a91", width=30).place(x=1020, y=12)
        self.lbl2 = CTkLabel(self.master, text="Here", fg_color='#1fcfb4', cursor="hand2", bg_color="#84959c", width=30)
        self.lbl2.bind("<Button-1>", self.ShowFrmReg)
        self.lbl2.place(x=990, y=12 )
        self.lbl3 = CTkLabel(self.master, text="Click", bg_color="#84959c", fg_color="#777a91", width=30).place(x=960, y=12)
        self.lblsar = CTkLabel(self.master, text="New Cars", text_color="white", bg_color="white", fg_color="#41611f",width=120, font=('tanha', 20)).place(x=1230, y=250)
        self.lblcar1 = Label(self.master, image=self.image1).place(x=1100, y=300)
        self.lbltc1 = CTkLabel(self.master, text="Peugeot 207 Glass ceiling", text_color="white", bg_color="white", fg_color="#41611f", width=150, font=('tanha', 12)).place(x=1100, y=410)
        self.lblcar2 = Label(self.master, image=self.image2).place(x=1100, y=450)
        self.lbltc2 = CTkLabel(self.master, text="Sonata 2023", text_color="white", bg_color="white", fg_color="#41611f", width=100, font=('tanha', 12)).place(x=1120, y=560)
        self.lblcar3 = Label(self.master, image=self.image3).place(x=1100, y=600)
        self.lbltc3 = CTkLabel(self.master, text="RX-350 2022", text_color="white", bg_color="white", fg_color="#41611f", width=100, font=('tanha', 12)).place(x=990, y=650)
        self.lblcar4 = Label(self.master, image=self.image4).place(x=850, y=300)
        self.lbltc4 = CTkLabel(self.master, text="Santa Fe 2024", text_color="white", bg_color="white", fg_color="#41611f", width=120, font=('tanha', 12)).place(x=870, y=410)
        self.lblcar5 = Label(self.master, image=self.image5).place(x=850, y=450)
        self.lbltc5 = CTkLabel(self.master, text="BMW-X6 2022", text_color="white", bg_color="white", fg_color="#41611f", width=120).place(x=870, y=560)



        self.frmSearch = CTkFrame(self.master, height=200, width=500, bg_color="#c3d7e0", fg_color="#757575")
        self.frmSearch.place(x=5, y=400)
        self.btnSearch = CTkButton(self.frmSearch,text="Search", command=self.OnClickSearch, bg_color="#c4c985", width=70)
        self.btnSearch.place(x=50, y=97)
        self.lblSearch = CTkLabel(self.frmSearch,text="Find the search term", text_color="#263238", bg_color="#78cbde", width=130, font=('tanha', 12)).place(x=140, y=97)



        self.Id = IntVar()
        self.Person = StringVar()
        self.Number = StringVar()
        self.Date = StringVar()
        self.Date1 = StringVar()
        self.Search = StringVar()
        self.Edit = StringVar()
        self.Delete = StringVar()
        self.Entry = StringVar()
        self.InReg = StringVar()
        self.OutReg = StringVar()
        self.User = StringVar()
        self.Pass = StringVar()
        self.Bio = StringVar()
        self.about = StringVar()
        self.Radio = IntVar()
        self.selected_car = StringVar()
        self.Edit1 = StringVar()
        self.Delete1 = StringVar()
        self.scrollbar1 = StringVar()
        self.scrollbar2 = StringVar()


        self.txtPerson = CTkEntry(self.master, textvariable=self.Person)
        self.txtPerson.configure(fg_color="white", bg_color="#f2a53f", justify=RIGHT)
        self.txtPerson.place(x=950, y=55)

        self.txtNumber = CTkEntry(self.master, textvariable=self.Number)
        self.txtNumber.configure(fg_color="white", bg_color="#f2a53f", justify=RIGHT)
        self.txtNumber.place(x=950, y=105)

        self.txtDate = CTkEntry(self.master, textvariable=self.Date)
        self.txtDate.configure(fg_color="white", bg_color="#f2a53f")
        self.txtDate.insert(0, "YYYY-MM-DD")
        self.txtDate.bind("<FocusIn>", self.FocusInEntry)
        self.txtDate.bind("<FocusOut>", self.FocusOutEntry)
        self.txtDate.place(x=950, y=155)


        self.txtSearch = CTkEntry(self.frmSearch, textvariable=self.Search)
        self.txtSearch.configure(bg_color="#c3d7e0", justify=RIGHT)
        self.txtSearch.place(x=310, y=100)


        self.lblcar_list = CTkLabel(self.master, text="None existent Cars", justify="center", bg_color="#9abf78", fg_color="#616161", width=120 ).place(x=760, y=10)
        self.car_list = ["Renault Talisman", "Tiba", "Quick", "Dena Plus", "Saina", "Xanthia 86", "Peugeot Pars", "Pride"]
        self.car_combobox = ttk.Combobox(self.master, justify="center", textvariable=self.selected_car, values=self.car_list)
        self.car_combobox.pack()



        self.btnSubmit = CTkButton(self.master, text="Registration", command=self.OnClickRegister, fg_color="#8ae86d", text_color="black", width=20)
        self.btnSubmit.bind("<Enter>", self.ChangeShape)
        self.btnSubmit.bind("<Leave>", self.ResetShape)
        self.btnSubmit.place(x=1260, y=160)


        self.btnDelete = CTkButton(self.master, text="Delete", command=self.OnClickDelete, fg_color="#993f7c", text_color="black", width=20)
        self.btnDelete.bind("<Enter>", self.ChangeShape)
        self.btnDelete.bind("<Leave>", self.ResetShape)
        self.btnDelete.place(x=1270, y=110)

        self.btnEdit = CTkButton(self.master, text="Edit", command=self.OnClickEdit, fg_color="#baa766", text_color="black", width=50)
        self.btnEdit.bind("<Enter>", self.ChangeShape)
        self.btnEdit.bind("<Leave>", self.ResetShape)
        self.btnEdit.place(x=1270, y=60)

        self.btnExit = CTkButton(self.master, text="Exit", command=self.Exit, bg_color="#e8271a", fg_color="red", text_color="black", width=70)
        self.btnExit.place(x=1260, y=10)


        self.ttkframe1 = CTkFrame(self.master)
        self.ttkframe1.place(x=0, y=0)

        self.tbl1 = ttk.Treeview(self.master, columns=("c1", "c2", "c3", "c4"), show="headings", height=15)
        self.tbl1.heading("#4", text="Row")
        self.tbl1.column("#4", width=50, anchor=S)

        self.tbl1.heading("#3", text="Expert")
        self.tbl1.column("#3", width=100, anchor=S)

        self.tbl1.heading("#2", text="Number")
        self.tbl1.column("#2", width=100, anchor=S)

        self.tbl1.heading("#1", text="Order Date")
        self.tbl1.column("#1", width=100, anchor=S)
        self.tbl1.place(x=5,y=0)
        self.tbl1.tag_configure('odd', background='#7e8e91')
        self.tbl1.tag_configure('even', background='#a89da6')
        self.tbl1.bind("<Button-1>", self.GetSelection)

        self.scrollbar1 = ttk.Scrollbar(self.master, orient="vertical", command=self.tbl1.yview)
        self.scrollbar1.place(x=1,y=1, width=12, height=328)
        self.tbl1.configure(yscrollcommand=self.scrollbar1.set)


        #self.tbl1.pack(side="left", fill="both", expand=True)
        #self.scrollbar1.pack(side="right", fill="y")


        self.outtime = []
        self.tbl1.bind("<Map>", self.set_cell_color)

        self.Load()


        self.frmLogin = CTkFrame(self.master, height=700, width=1200, bg_color="#c3f7c7")
        self.frmLogin.place(x=0, y=0)
        self.label = CTkLabel(self.frmLogin, text="Hello! Your Welcome", text_color="lightblue")
        self.label.place(x=550, y=0)
        self.lblwellcome = CTkLabel(self.frmLogin, text="Sanyar Gallery", bg_color="#9c5980", width=100).place(x=1100, y=2)
        self.lblUser = CTkLabel(self.frmLogin, text="Username", bg_color="#5379b5",fg_color="#5379b5", width=80).place(x=750,y=200)
        self.lblPass = CTkLabel(self.frmLogin, text="Password", bg_color="#5379b5",fg_color="#5379b5", width=80).place(x=750, y=250)
        self.lblGod = CTkLabel(self.frmLogin, text="In the name of God", fg_color="orange",text_color="white", width=180).place(x=540, y=35)
        self.txtUser = CTkEntry(self.frmLogin, textvariable=self.User, bg_color="#a9b0ba", fg_color="#80a7ba", text_color="black", width=80)
        self.txtUser.place(x=645, y=200)
        self.txtPass = CTkEntry(self.frmLogin, textvariable=self.Pass, bg_color="#a9b0ba", fg_color="#80a7ba", show="*", text_color="black", width=80)
        self.txtPass.place(x=645, y=250)

        self.show_password_button = CTkButton(self.frmLogin, text="Show/Hidden", bg_color="#15e874", fg_color="gray",command=self.toggle_password_visibility)
        self.show_password_button.place(x=580, y=320)
        self.is_password_visible = True

        self.btnLogin = CTkButton(self.frmLogin, text="Login", bg_color="#15e874", fg_color="gray", command=self.Login)
        self.btnLogin.place(x=450, y=320)





        self.lblcar0 = CTkLabel(self.frmLogin, image=self.image0).place(x=100, y=200)



        self.frmReg = CTkFrame(self.master, height=700, width=1200, bg_color="#c5c977")
        self.frmReg.place_forget()

        self.lblInReg = CTkLabel(self.frmReg, text="Internal", text_color="white", fg_color="#C0CA33", width=100, font=("tanha", 15)).place(x=1100,y=55)
        self.lblOutReg= CTkLabel(self.frmReg, text="Imported", text_color="white", fg_color="#C0CA33", width=100, font=("tanha", 15)).place(x=1100, y=100)
        self.lblDate = CTkLabel(self.frmReg, text="Order Date", text_color="white", fg_color="#C0CA33", width=100, font=("tanha", 15)).place(x=1100, y=145)

        self.txtInReg= CTkEntry(self.frmReg, textvariable=self.InReg)
        self.txtInReg.configure(fg_color="#EEEEEE", bg_color="#9c877c", text_color="black", justify=RIGHT)
        self.txtInReg.place(x=920, y=57)

        self.txtOutReg= CTkEntry(self.frmReg, textvariable=self.OutReg)
        self.txtOutReg.configure(fg_color="#EEEEEE", bg_color="#9c877c", text_color="black", justify=RIGHT)
        self.txtOutReg.place(x=920, y=102)

        self.txtDate1= CTkEntry(self.frmReg, textvariable=self.Date1)
        self.txtDate1.configure(fg_color="#EEEEEE", bg_color="#9c877c", text_color="black", justify=RIGHT)
        self.txtDate1.bind("<FocusIn>", self.FocusInEntryc)
        self.txtDate1.bind("<FocusOut>", self.FocusOutEntryc)
        self.txtDate1.place(x=920, y=145)



        self.btnSubmit = CTkButton(self.frmReg, text="Registration", command=self.OnClickRegisterNewUser, bg_color="#9c877c", fg_color="#558B2F", width=80,font=("tanha", 10))
        self.btnSubmit.bind("<Enter>", self.ChangeShape)
        self.btnSubmit.bind("<Leave>", self.ResetShape)
        self.btnSubmit.place(x=1100, y=200)

        self.btnReturn = CTkButton(self.frmReg, text="Back", command=self.forgetReg, bg_color="#9c877c",fg_color="#F06292", width=80,  font=("tanha", 10))
        self.btnReturn.bind("<Enter>", self.ChangeShape)
        self.btnReturn.bind("<Leave>", self.ResetShape)
        self.btnReturn.place(x=1100, y=350)

        self.btnDelete1 = CTkButton(self.frmReg, text="Delete", command=self.OnClickDeletec, bg_color="#9c877c", fg_color="#B71C1C", width=80, font=("tanha", 10))
        self.btnDelete1.bind("<Enter>", self.ChangeShape)
        self.btnDelete1.bind("<Leave>", self.ResetShape)
        self.btnDelete1.place(x=1100, y=300)

        self.btnEdit1 = CTkButton(self.frmReg, text="Edit", command=self.OnClickEditc, bg_color="#9c877c", fg_color="#424242",width=80, font=("tanha", 10))
        self.btnEdit1.bind("<Enter>", self.ChangeShape)
        self.btnEdit1.bind("<Leave>", self.ResetShape)
        self.btnEdit1.place(x=1100, y=250)

        self.lblbio = CTkLabel(self.frmReg,text="Sanyar car exhibition, under the management of Meysam Hassani,\n has more than 12 years of experience in the field of buying and selling \n foreign and Iranian luxury cars in zhanbazan area of Rasht city. \n",bg_color="#3b3b38",text_color="#004D40",fg_color="#E0E0E0", width=500, justify=LEFT).place(x=5, y=630)
        self.lblabout = CTkLabel(self.frmReg, text="about us", bg_color="#3b3b38",text_color="#004D40",fg_color="#E0E0E0" ,width=80).place(x=5, y=590)


        self.RadioForsales = ttk.Radiobutton(self.frmReg, text="Imported", variable=self.Radio, value=1)
        self.RadioForsales.place(x=1060, y=5)
        self.RadioInsales = ttk.Radiobutton(self.frmReg, text="Internal", variable=self.Radio, value=0).place(x=1135, y=5)

        self.ttkframe2 = CTkFrame(self.frmReg)
        self.ttkframe2.place(x=0, y=0)

        self.tbl2 = ttk.Treeview(self.frmReg, columns=("c1", "c2", "c3", "c4"), show="headings", height=15)
        self.tbl2.heading("#4", text="Row")
        self.tbl2.column("#4", width=50, anchor=S)

        self.tbl2.heading("#3", text="Order Date")
        self.tbl2.column("#3", width=100, anchor=S)

        self.tbl2.heading("#2", text="Imported")
        self.tbl2.column("#2", width=100, anchor=S)

        self.tbl2.heading("#1", text="Internal")
        self.tbl2.column("#1", width=110, anchor=S)
        self.tbl2.place(x=5, y=0)
        self.tbl2.tag_configure('odd', background='#cae37f')
        self.tbl2.tag_configure('even', background='#8d8ec9')
        self.tbl2.bind("<Button-1>", self.GetSelection1)

        self.scrollbar2 = ttk.Scrollbar(self.frmReg, orient="vertical", command=self.tbl2.yview)
        self.scrollbar2.place(x=1, y=1, width=12, height=328)
        self.tbl2.configure(yscrollcommand=self.scrollbar2.set)

        #self.tbl2.pack(side="left", fill="both", expand=True)
        #self.scrollbar2.pack(side="right", fill="y")


        self.outtime = []
        self.tbl2.bind("<Map>", self.set_cell_color)

        self.Loadc()




    def forgetReg(self):
        self.frmReg.place_forget()



    def set_cell_color(self,event):
        #l = ""
        for child in self.tbl1.get_children():
            date_str = self.tbl1.item(child)['values'][3]
            if self.calculate_date_difference(date_str) > 30:
                #l += "\n" + str(self.tbl.item(child)['values'][8])
                self.outtime.append(self.tbl1.item(child)['values'][8])
                #lbl = Label(self.master, text=l).place(x=100, y=300)



    def set_cell_color1(self,event):
        #l = ""
        for child in self.tbl2.get_children():
            date_str = self.tbl2.item(child)['values'][3]
            if self.calculate_date_difference(date_str) > 30:
                #l += "\n" + str(self.tbl.item(child)['values'][8])
                self.outtime.append(self.tbl2.item(child)['values'][8])
                #lbl = Label(self.master, text=l).place(x=100, y=300)



    def calculate_date_difference(self, date_str1):
        # اطمینان از اینکه date_str1 به رشته تبدیل شده است
        try:
            date_str1 = str(date_str1)
            date_str = datetime.strptime(date_str1, "%Y-%m-%d")

            jalali_date = date_str
            jalali_today = JalaliDate.today()

            date1 = datetime(jalali_date.year, jalali_date.month, jalali_date.day)
            date2 = datetime(jalali_today.year, jalali_today.month, jalali_today.day)

            delta = date2 - date1
            return delta.days
        except ValueError:
            # اگر تاریخ نامعتبر بود، مقدار None برنگردانیم
            return -1  # مقدار پیش‌فرض برای تاریخ نامعتبر

    def ShowFrmReg(self,e):
        self.frmReg.place(x=0, y=0)


    def Exit(self):
        self.frmLogin.place(x=0, y=0)
        self.User.set('')
        self.Pass.set('')
        self.txtUser.focus_set()


    def toggle_password_visibility(self):
        self.is_password_visible = not self.is_password_visible
        self.txtPass.configure(show="*" if self.is_password_visible else "")



    def Login(self):
        objL = Login(self.User.get(), self.Pass.get())
        objbl = blPersonal()
        r = objbl.blExistLogin(Login, objL)
        if r == True:
            self.frmLogin.place_forget()
        else:
            messagebox.showerror("Error", "!username or password is wrong")


    def FocusInEntry(self, e):
        if self.txtDate.get() == "YYYY-MM-DD":
            self.txtDate.delete(0, "end")
            self.txtDate.configure(fg="white")

    def FocusInEntryc(self, e):
        if self.txtDate1.get() == "YYYY-MM-DD":
            self.txtDate1.delete(0, "end")
            self.txtDate1.configure(fg="white")

    def FocusOutEntry(self, e):
        if self.txtDate.get() == "":
            self.txtDate.insert(0, "YYYY-MM-DD")
            self.txtDate.configure(fg="white")

    def FocusOutEntryc(self, e):
        if self.txtDate1.get() == "":
           self.txtDate1.insert(0, "YYYY-MM-DD")
           self.txtDate1.configure(fg="white")


    def show_selection(self):
        self.selected_car = self.car_combobox.get()
        if self.selected_car == "Sayna":
            print("You choiced the sayna.")
        elif self.selected_car == "Dena Plus":
            print("You choiced the dena plus")


    def OnClickRegister(self):
        if self.Person.get() == "":
            self.txtPerson.focus_set()
            messagebox.showwarning("Attention", "please enter your name and family")
        elif self.Number.get() == "":
            self.txtNumber.focus_set()
            messagebox.showwarning("Attention", "please enter your number")
        elif self.Date.get() == "":
            self.txtDate.focus_set()
            messagebox.showwarning("Attention", "please enter your order date")
        else:
            if self.isExist() == True:
                objp = Personal(self.Person.get(), self.Number.get(), self.Date.get())
                objbl = blPersonal()
                result = objbl.blAdd(objp)
                if result == True:
                    self.Load()
                    self.set_cell_color(None)
                    self.Person.set("")
                    self.Number.set("")
                    self.Date.set("YYYY-MM-DD")


                    messagebox.showinfo("Registration", "Your information has been successfully registered")
                else:
                     messagebox.showerror("Repetitive", "!This order has already been registered")


    def Clean(self):
        for item in self.tbl1.get_children():
            self.tbl1.delete(item)

    def Cleanc(self):
        for item in self.tbl2.get_children():
            self.tbl2.delete(item)



    def Load(self):
        self.Clean()
        objbl = blPersonal()
        lstPersonal = objbl.blRead(Personal)
        for item in lstPersonal:
            self.tbl1.insert('', "end", values=[item.prs_date, item.prs_number,item.prs_person, item.prs_id])

            if len(self.tbl1.get_children()) % 2==0:
               self.tbl1.item(self.tbl1.get_children() [-1], tags= ('odd',))
            else:
                self.tbl1.item(self.tbl1.get_children() [-1], tags= ('even',))
        for item in range(50):
            if item % 2 == 0:
                self.tbl1.insert("", END, values=(f"Date {item}", f"Number {item}", f"Expert {item}", f"Row {item}"),
                                 tags=('even',))
            else:
                self.tbl1.insert("", END, values=(f"Date {item}", f"Number {item}", f"Expert {item}", f"Row {item}"),
                                 tags=('odd',))


    def Loadc(self):
        self.Cleanc()
        objbl = blCar()
        lstCar = objbl.blRead(Car)
        for item in lstCar:
            self.tbl2.insert('', "end", values=[item.car_in, item.car_out,item.car_date, item.car_id])
            if len(self.tbl2.get_children()) % 2==0:
               self.tbl2.item(self.tbl2.get_children() [-1], tags= ('odd',))
            else:
                self.tbl2.item(self.tbl2.get_children() [-1], tags= ('even',))
        for item in range(50):
            if item % 2 == 0:
                self.tbl1.insert("", END, values=(f"Date {item}", f"Number {item}", f"Expert {item}", f"Row {item}"),
                                 tags=('even',))
            else:
                self.tbl1.insert("", END, values=(f"Date {item}", f"Number {item}", f"Expert {item}", f"Row {item}"),
                                 tags=('odd',))



    def GetSelection(self, e):
        objbl = blPersonal()
        SelectRow = self.tbl1.selection()
        if SelectRow != ():
            idrow = self.tbl1.item(SelectRow)["values"][3]
            self.Id.set(idrow)
            obj = objbl.blReadById(Personal, idrow)
            self.Person.set(obj.prs_person)
            self.Number.set(obj.prs_number)
            self.Date.set(obj.prs_date)

    def GetSelection1(self, e):
        objbl = blCar()
        SelectRow = self.tbl2.selection()
        if SelectRow != ():
            idrow = self.tbl2.item(SelectRow)["values"][3]
            print("id row is :")
            print(idrow)
            self.Id.set(idrow)
            obj = objbl.blReadById(Car, idrow)
            self.InReg.set(obj.car_in)
            self.OutReg.set(obj.car_out)
            self.Date1.set(obj.car_date)

    def OnClickDelete(self):
        ask = messagebox.askyesno("Attention", "Are you sure you want to delete this data؟")
        if ask == True:
            Id = self.Id.get()
            objbl = blPersonal()
            result = objbl.blDelete(Personal,Id)
            if result == True:
                self.Load()
                self.Person.set("")
                self.Number.set("")
                self.Date.set("YYYY-MM-DD")

                messagebox.showinfo("Successful Operation", "The delete operation was successful")
            else:
                messagebox.showinfo("Operation Failed", "The delete operation failed")

    def OnClickDeletec(self):
        ask = messagebox.askyesno("Attention", "Are you sure you want to delete this data?")
        if ask == True:
            print(("hhh"))
            Id = self.Id.get()
            objbl = blCar()
            result = objbl.blDelete(Car, Id)
            if result == True:
                print(result)
                self.Loadc()
                self.InReg.set("")
                self.OutReg.set("")
                self.Date1.set("YYYY-MM-DD")

                messagebox.showinfo("Successful Operation", "The delete operation was successful")
            else:
                messagebox.showinfo("Operation Failed", "The delete operation failed")


    def OnClickEdit(self):
        Id = self.Id.get()
        objp = Personal(self.Person.get(), self.Number.get(), self.Date.get())
        objbl = blPersonal()
        result = objbl.blUpdatePersonal(Personal, Id, objp)
        if result == True:
            print(result)
            self.Load()
            self.outtime = []
            self.set_cell_color(None)
            self.Person.set("")
            self.Number.set("")
            self.Date.set("YYYY-MM-DD")
            messagebox.showinfo("Successful Operation", "The edit operation was successful")
        else:
            messagebox.showinfo("Operation Failed", "The edit operation failed")


    def OnClickEditc(self):
        Id = self.Id.get()
        objc = Car(self.InReg.get(), self.OutReg.get(), self.Date1.get())
        objbl = blCar()
        result = objbl.blUpdateCar(Car, Id, objc)
        if result == True:
            print(result)
            self.Loadc()
            self.outtime = []
            self.set_cell_color(None)
            self.InReg.set("")
            self.OutReg.set("")
            self.Date1.set("YYYY-MM-DD")
            messagebox.showinfo("Successful Operation", "The edit operation was successful")
        else:
            messagebox.showinfo("Operation Failed", "The edit operation failed")




    def ChangeShape(self, e):
        e.widget.config(relief=SUNKEN)


    def ResetShape(self, e):
        e.widget.config(relief=RAISED)


    def OnClickSearch(self):
        srch = self.Search.get()
        if srch == "":
            self.Load()
        else:
            objbl = blPersonal()
            result = objbl.blSearch(Personal, srch)
            if result != []:
                self.Clean()
                for item in result:
                    self.tbl1.insert('', "end", values=[item.prs_date,item.prs_number, item.prs_person, item.prs_id])

    def OnClickSearchc(self):
        srch = self.Search.get()
        if srch == "":
            self.Loadc()
        else:
            objbl = blCar()
            result = objbl.blSearch(Car, srch)
            if result != []:
                self.Cleanc()
                for item in result:
                    self.tbl2.insert('', "end", values=[item.car_date, item.car_out, item.car_in, item.car_id])

    def isExist(self):
        objp = Personal(self.Person.get(), self.Number.get(), self.Date.get())
        objbl = blPersonal()
        return objbl.blExist(Personal, objp)

    def isExist_Car(self):
        objc = Car(self.InReg.get(), self.OutReg.get(), self.Date1.get())
        objbl = blCar()
        return objbl.blExist_Car(Car, objc)



    def OnClickRegisterNewUser(self):
        if self.InReg.get() == "":
           self.txtInReg.focus_set()
           messagebox.showwarning("Attention", "please enter the name of the internal car")
        elif self.OutReg.get() == "":
             self.txtOutReg.focus_set()
             messagebox.showwarning("Attention", "please enter the name of the imported car")
        else:
            if self.isExist_Car() == True:
                objc = Car(self.InReg.get(), self.OutReg.get(), self.Date1.get())
                objbl = blCar()
                result = objbl.blAdd(objc)
                if result == True:
                    self.Load()
                    self.set_cell_color(None)
                    self.InReg.set("")
                    self.OutReg.set("")
                    self.Date1.set("YYYY-MM-DD")

                    messagebox.showinfo("Registration", "information has been successfully registered")
                else:
                     messagebox.showerror("Repetitive", "!this order has already been registered")


















