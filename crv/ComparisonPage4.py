from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt
import pymysql
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp
class ComparisionClass:
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
        self.headlbl = Label(self.window, text="Sale Report",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)
        self.headlbl.place(x=0, y=0,width=w1,height=70)
        # self.l1 = Label(self.window, text="Attendence",font=('Century', 20, 'bold'),
        #                 foreground=dp.textcolor,background=dp.pagebkcolor)
        # self.l1.place(x=500,y=100)

        self.databaseConnection()
        self.getData()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='car_prediction_db', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def getData(self):

        #------ get data from anywhere (database, user, calculations,random,csv,dataframe) ----
        try:

            # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on
            qry = " select * from carsaletable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            petrol_sale=0
            diesel_sale=0
            cng_sale=0
            for myrow in data:
                if myrow[5]=='Petrol':
                    petrol_sale+=1
                elif myrow[5]=='Diesel':
                    diesel_sale+=1
                else:
                    cng_sale+=1
        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)

        # ------------ make diagram -----------------

        # student_names=["raman","gagan","aman","mohit","rohit"]
        # student_attendence = [120,111,90,378,77]
        # colors_list=['red','green','teal','gray','pink']

        pie_labels = ["Petrol","Diesel","CNG"]
        pie_values = [petrol_sale,diesel_sale,cng_sale]
        pie_colors = ["brown","teal","red"]


        figure1 = plt.Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=500,y=300)
        ax1.set_title('Attendence Record')
        # ax1.pie(pie_values ,labels=pie_labels ,autopct='%.1f%%')
        ax1.pie(pie_values ,labels=pie_labels ,autopct='%.1f%%',colors=pie_colors)


if __name__ == '__main__':
    dummy=Tk()
    obj = ComparisionClass(dummy)
    dummy.mainloop()
