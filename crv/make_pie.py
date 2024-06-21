from tkinter import *
import matplotlib.pyplot as plt
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
        self.headlbl = Label(self.window, text="Attendence ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)
        self.headlbl.place(x=0, y=0,width=w1,height=70)
        # self.l1 = Label(self.window, text="Attendence",font=('Century', 20, 'bold'),
        #                 foreground=dp.textcolor,background=dp.pagebkcolor)
        # self.l1.place(x=500,y=100)

        x1=40
        y1=200
        x_dif=510

        student_names=["raman","gagan","aman","mohit","rohit"]
        student_attendence = [120,111,90,378,77]
        colors_list=['red','green','teal','gray','pink']

        figure1 = plt.Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=500,y=y1)
        ax1.set_title('Attendence Record')
        ax1.pie(student_attendence ,labels=student_names ,autopct='%.1f%%',colors=colors_list)

        self.window.mainloop()


if __name__ == '__main__':
    dummy=Tk()
    obj = ComparisionClass(dummy)
    dummy.mainloop()
