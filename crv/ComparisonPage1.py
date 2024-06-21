from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp

class Comparision1Class:
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
        self.headlbl = Label(self.window, text="Analysis ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)
        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.l1 = Label(self.window, text="Bivarate analysis",font=('Century', 20, 'bold'),
                        foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l1.place(x=40,y=100)

        x1=40
        y1=200
        x_dif=510
        car_data = pd.read_csv('car data.csv')


        figure1 = plt.Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*0,y=y1)
        ax1.set_title('Years v/s Selling_Price')
        car_data.plot(kind='scatter',x='Year', y='Selling_Price', legend=True, ax=ax1)

        figure2 = plt.Figure(figsize=(5,5), dpi=100)
        ax2= figure2.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure2, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*1+10,y=y1)
        ax2.set_title('Present Price v/s Selling_Price')
        car_data.plot(kind='scatter',x='Present_Price', y='Selling_Price', legend=True, ax=ax2)

        figure3 = plt.Figure(figsize=(5,5), dpi=100)
        ax3= figure3.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure3, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*2+20,y=y1)
        ax3.set_title('Kms_Driven v/s Selling_Price')
        car_data.plot(kind='scatter',x='Kms_Driven', y='Selling_Price', legend=True, ax=ax3)

        self.window.mainloop()


    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()


if __name__ == '__main__':
    dummy=Tk()
    obj = Comparision1Class(dummy)
    dummy.mainloop()
