from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql as pymysql
from PIL import ImageTk, Image
import detailspage as dp
import joblib
import sklearn
model = joblib.load('car_predictor_model')

class CarPageClass:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Car Price Predictor")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')


        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.pagebkcolor)
        self.headlbl = Label(self.window, text="Predict Car Selling  Price ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)

        self.l1 = Label(self.window, text="Year",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l2 = Label(self.window, text="Showroom Price (in lakh) ",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l3 = Label(self.window, text="Kilometers Drived ",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l4 = Label(self.window, text="Previous Owners",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l5 = Label(self.window, text="Fuel type",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l6 = Label(self.window, text="Seller Type ",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l7 = Label(self.window, text="Transmission Type",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l8 = Label(self.window, text=" - - - - - ",font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)

        self.t1 = Entry(self.window,font=dp.textfont,foreground=dp.textcolor)
        self.t2 = Entry(self.window,font=dp.textfont,foreground=dp.textcolor)
        self.t3 = Entry(self.window,font=dp.textfont,foreground=dp.textcolor)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=["0", "1", "3"], textvariable=self.v1, state='readonly',font=dp.textfont,foreground=dp.textcolor)
        self.v1.set("0")
        self.list1 = ["Petrol", "Diesel", "CNG"]
        self.v2 = StringVar()
        self.c2 = Combobox(self.window, values=self.list1, textvariable=self.v2, state='readonly',font=dp.textfont,foreground=dp.textcolor)
        self.v2.set("Petrol")
        self.list2 = ["Dealer", "Individual"]
        self.v3 = StringVar()
        self.c3 = Combobox(self.window, values=self.list2, textvariable=self.v3, state='readonly',font=dp.textfont,foreground=dp.textcolor)
        self.v3.set("Dealer")
        self.v4 = StringVar()
        self.c4 = Combobox(self.window, values=['Manual', "Automatic"], textvariable=self.v4, state='readonly',font=dp.textfont,foreground=dp.textcolor)
        self.v4.set("Manual")
        self.btn1 = Button(self.window, text="Predict Price",font=dp.textfont,
                           foreground=dp.headcolor,background=dp.headbkcolor,command=self.predict)

        self.btn2 = Button(self.window, text="Reset",font=dp.textfont,
                           foreground=dp.headcolor,background=dp.headbkcolor,command=self.clearPage)
        self.btn3 = Button(self.window, text="Sale",font=dp.textfont,
                           foreground=dp.headcolor,background=dp.headbkcolor,command=self.saveData)

        self.ressize_w=100
        self.ressize_h=100
        self.responseimglbl = Label(self.window,background=dp.pagebkcolor)
        carsize_w=500
        carsize_h=200
        self.carimg1 = ImageTk.PhotoImage(Image.open("myapp_images//car2.png").resize((carsize_w,carsize_h)))
        self.carimglbl = Label(self.window,image=self.carimg1,background=dp.pagebkcolor)

        # ******** PLacing *************
        self.headlbl.place(x=0, y=0,width=w1,height=70)
        x1 = 40
        y1 = 100
        x_diff=250
        y_diff=50
        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        self.responseimglbl.place(x=x1+x_diff*3,y=y1,width=self.ressize_w,height=self.ressize_h)
        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        self.carimglbl.place(x=x1+x_diff*2,y=y1,width=carsize_w,height=carsize_h)
        y1 += y_diff
        self.l5.place(x=x1, y=y1)
        self.c2.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l6.place(x=x1, y=y1)
        self.c3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l7.place(x=x1, y=y1)
        self.c4.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.btn2.place(x=x1 , y=y1,width=200,height=40)
        self.btn1.place(x=x1 + x_diff*1, y=y1,width=200,height=40)
        self.btn3.place(x=x1 + x_diff*2, y=y1,width=200,height=40)
        y1 += y_diff
        self.l8.place(x=x1 + x_diff, y=y1)

        self.clearPage()


        self.databaseConnection()
        self.window.mainloop()

    def predict(self):

        year = int(self.t1.get())
        presentPrice = float(self.t2.get())
        Kms_Driven = float(self.t3.get())
        Owner = int(self.v1.get())

        Fuel_Type = self.v2.get()
        if Fuel_Type == "Diesel":
            Fuel_Diesel = 1
            Fuel_Petrol = 0
        elif Fuel_Type == "Petrol":
            Fuel_Diesel = 0
            Fuel_Petrol = 1
        else:
            Fuel_Diesel = 0
            Fuel_Petrol = 0
        Seller_Type = self.v3.get()
        if Seller_Type == "Dealer":
            Seller_Individual = 0
        else:
            Seller_Individual = 1

        Transmission = self.v4.get()
        if (Transmission == 'Manual'):
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        self.price = model.predict([[year, presentPrice, Kms_Driven, Owner, Fuel_Diesel, Fuel_Petrol,
                                                Seller_Individual, Transmission_Manual]])
        self.output = round(self.price[0], 2)
        if self.output < 0:
            self.l8.config(text="Sorry you cannot sell this car")
            self.responseimg1 = ImageTk.PhotoImage(Image.open("myapp_images//thumb-down.png").resize((self.ressize_w,self.ressize_h)))
            self.responseimglbl.config(image=self.responseimg1)
            self.btn3['state'] = 'disabled'
        else:
            self.l8.config(text="You Can Sell The Car at Rs. {} Lakh(s)".format(self.output))
            self.responseimg1 = ImageTk.PhotoImage(Image.open("myapp_images//thumbs-up.png").resize((self.ressize_w,self.ressize_h)))
            self.responseimglbl.config(image=self.responseimg1)
            self.btn3['state'] = 'normal'


    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.c1.current(0)
        self.c2.current(0)
        self.c3.current(0)
        self.c4.current(0)
        self.l8.config(text="")
        self.btn3['state'] = 'disabled'
        self.output=""
        self.responseimg1 = ImageTk.PhotoImage(Image.open("myapp_images//question-mark.png").resize((self.ressize_w,self.ressize_h)))
        self.responseimglbl.config(image=self.responseimg1)

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='car_prediction_db', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def saveData(self):
        if self.validate_check()==False:
            return
        try:
            from datetime import date
            today = date.today()
            today2 = today.strftime("%Y-%m-%d")

            # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on
            qry = " insert into carsaletable (year, showroom_price, km_drived, previous_owner," \
                  " fuel_type, seller_type, transmission, price, sold_on) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry, (int(self.t1.get()),str(float(self.t2.get())) ,str(float(self.t3.get())),
                                               int(self.v1.get()), self.v2.get(), self.v3.get(), self.v4.get(),self.output,today2 ))
            self.conn.commit()
            if (rowcount == 1):
                messagebox.showinfo("Success", "Car Sold Successfully", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)

    def validate_check(self):
        if len(self.t1.get()) < 4:
            messagebox.showwarning("Validation Check", "Please Enter Year ", parent=self.window)
            return False
        elif len(self.t2.get()) < 1:
            messagebox.showwarning("Validation Check", "Please Enter Showroom Price ", parent=self.window)
            return False
        elif len(self.t3.get()) < 1:
            messagebox.showwarning("Validation Check", "Please Enter Km Drived", parent=self.window)
            return False
        elif self.output == "" :
            messagebox.showwarning("Validation Check", "First Predict the Price", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummy=Tk()
    obj = CarPageClass(dummy)
    dummy.mainloop()

