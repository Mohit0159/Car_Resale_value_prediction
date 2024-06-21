from tkinter import *
from tkinter import messagebox
import detailspage as dp
from ComparisonPage1 import Comparision1Class
from ComparisonPage2 import Comparision2Class
from MyCarPredictor import CarPageClass
from PIL import ImageTk, Image
from reportPage import ViewReport3Class

class HomepageClass:
    def __init__(self):
        self.window = Tk()
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=int(self.w/2)
        h1=int(self.h/2)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        # self.window.state('zoomed')
        self.window.title('Car Predictor')

        self.headlbl = Label(self.window, text="Car Price Predictor ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)

        self.window.config(background=dp.pagebkcolor)

        self.b1 = Button(self.window,text="Predict",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda : CarPageClass(self.window))
        self.b2 = Button(self.window,text="Univarate Analysis",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision2Class(self.window))
        self.b3 = Button(self.window,text="Bivarate Analysis",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision1Class(self.window))
        self.b4 = Button(self.window,text="Sale Report",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :ViewReport3Class(self.window))
        self.b5 = Button(self.window,text="Close",font=dp.headfont2,foreground=dp.headcolor,background=dp.headbkcolor,command=self.quitter)



        x1 = 30
        y1=100
        y_diff=70
        b_width=250
        b_height=55



        carsize_w=w1 - (x1+b_width+10)
        carsize_h=200
        self.carimg1 = ImageTk.PhotoImage(Image.open("myapp_images//car2.png").resize((carsize_w,carsize_h)))
        self.carimglbl = Label(self.window,image=self.carimg1,background=dp.pagebkcolor)



        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.b1.place(x=x1,y=y1,width=b_width,height=b_height)
        self.carimglbl.place(x=x1+b_width+10,y=200,width=carsize_w,height=carsize_h)
        y1+=y_diff
        self.b2.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b3.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b4.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b5.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff


        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()

if __name__ == '__main__':
    HomepageClass()