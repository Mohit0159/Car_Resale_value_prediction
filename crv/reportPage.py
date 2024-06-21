import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
import pymysql
from tkcalendar import DateEntry
import detailspage as dp
from ReportPrint import Report1PDF


class ViewReport3Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Sale Report")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = self.w
        h1 = self.h
        self.window.minsize(w1, h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')

        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.pagebkcolor)
        self.headlbl = Label(self.window, text="Sale's Report ",
                             font=dp.headfont, foreground=dp.headcolor, background=dp.headbkcolor)

        self.l1=Label(self.window,text='From ',font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l2=Label(self.window,text='to',font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l3=Label(self.window,text='Total Cars',font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)


        from datetime import date
        today = date.today()
        self.t1 = DateEntry(self.window, width=20, foreground='white', borderwidth=2, date_pattern='y-mm-dd',
                            state="readonly",font=dp.textfont,background=dp.pagebkcolor)
        self.t2 = DateEntry(self.window, width=20, foreground='white',borderwidth=2, date_pattern='y-mm-dd',
                            state="readonly",font=dp.textfont,background=dp.pagebkcolor)
        self.t3=Label(self.window,text='0',font=dp.textfont,foreground=dp.textcolor,background=dp.pagebkcolor)

        #--------table----------
        self.tablearea = Frame(self.window )
        scrollbarx = Scrollbar(self.tablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tablearea, orient=VERTICAL)
        # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on

        self.mytable = Treeview(self.tablearea,height=20,columns=['a','b','c','d','e','f','g','h','i','j'],
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.mytable.heading('a',text='Serial No.')
        self.mytable.heading('b',text='Year')
        self.mytable.heading('c',text='Showroom Price')
        self.mytable.heading('d',text='Km Drived')
        self.mytable.heading('e',text='Owners')
        self.mytable.heading('f',text='Fuel')
        self.mytable.heading('g',text='Seller')
        self.mytable.heading('h',text='Transmission')
        self.mytable.heading('i',text='Price')
        self.mytable.heading('j',text='Sell Date')
        self.mytable['show']='headings'
        self.mytable.column("#1", width=100, anchor='center')
        self.mytable.column("#2", width=150, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=110, anchor='center')
        self.mytable.column("#7", width=120, anchor='center')
        self.mytable.column("#8", width=150, anchor='center')
        self.mytable.column("#9", width=150, anchor='center')
        self.mytable.column("#10", width=150, anchor='center')
        self.mytable.pack()


        #------ buttons---------
        self.b1=Button(self.window,text='Search',font=dp.textfont, foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :self.fetchalldata(by='date'))
        self.b2=Button(self.window,text='Print',font=dp.textfont, foreground=dp.headcolor,background=dp.headbkcolor,command=self.getPrintout)

        #---------------placements-----------------
        x1 = 160
        y1 = 100
        ydiff = 45
        xdiff = 150
        wigdet_width = 200
        t_diff = xdiff + xdiff + xdiff + xdiff
        upper_btn_x = x1 + xdiff + xdiff + 55
        btn_low_width = 120
        v_diff=600
        go_side=0
        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.l1.place(x=x1,y=y1)
        self.t1.place(x=x1+(xdiff*1),y=y1,width=wigdet_width)
        self.l2.place(x=x1+(xdiff*3),y=y1)
        self.t2.place(x=x1+(xdiff*4),y=y1,width=wigdet_width)
        self.b1.place(x=x1+(xdiff*5)+70,y=y1,width=btn_low_width,height=31)

        y1 += ydiff
        self.tablearea.place(x=x1-go_side, y=y1)

        y1=v_diff
        self.l3.place(x=x1,y=y1)
        self.t3.place(x=x1+(xdiff*1),y=y1,width=wigdet_width)
        bw=200
        self.b2.place(x=self.w/2-bw,y=y1,width=bw)
        self.clearpage()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='car_prediction_db', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)

    def fetchalldata(self,by):
        self.databaseConnection()
        try:
            myqry='select * from carsaletable  where sold_on between %s and %s'
            self.curr.execute(myqry ,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            total_seats=len(data)
            self.print_data=[]
            if data:
               for row in data:
                   self.print_data.append([row[1],row[2],row[3],row[5],row[6],row[7],row[8],row[9]])
                   self.mytable.insert('', END, values=row)
               self.t3.config(text=str(total_seats))
            else:
                messagebox.showwarning("No record", "No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Searching of record\n\n"+str(e),parent=self.window)

    def getPrintout(self):
        pdf = Report1PDF()
        pdf.foot_msg1 = "Total Booked Seats = "+self.t3['text']
        heading = "Sales Report"
        col_heading = ['year'	,'Cost',	'KM',
                       'Fuel',	'Seller'	,'Mode',	'Price',	'Sold on']

        pdf.print_page(heading, col_heading, self.print_data)
        pdf.output('report1.pdf')
        os.system('report1.pdf ')


if __name__ == '__main__':
    window = Tk()
    ViewReport3Class(window)
    window.mainloop()