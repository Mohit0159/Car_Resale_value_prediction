import os
from fpdf import FPDF
import detailspage as dp
class Report1PDF(FPDF):
    foot_msg1="No Message"
    def header(self):
        # self.set_fill_color(180, 10, 49)
        self.set_fill_color(201, 84, 162)
        self.set_text_color(255,255, 255)
        self.set_font('Helvetica', 'B', 20)
        self.cell(0, 20, "Car Predictor", 0, 1, 'L', 1)
        self.ln(1)
        self.cell(0, 1, "", 0, 1, 'L', 1)
        self.ln(2)

    def page_content(self, heading,col_headings,data ):

        self.set_font('Arial', 'BU', 15)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(201, 84, 162)
        self.cell(0, 20, heading, 0, 1, 'L', 1)


        self.set_fill_color(255, 255, 255)
        self.set_text_color(0,0,0)
        self.ln(10)
        spacing=1
        col_width = self.w /3-5   # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size+2

        self.set_fill_color(200, 220, 255)
        self.ln()

        self.set_font('Arial', 'B', 11)
        spacing = 1
        col_width = self.w / (len(col_headings)+1)  # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size + 4

        # Table heading
        for i in col_headings:  # for headings
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)

        # table body
        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        self.ln(30)


        self.set_fill_color(201, 84, 162)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, self.foot_msg1, 0, 0, 'C', 1)

    def print_page(self, heading,col_headings,data):
        self.add_page()
        self.page_content(heading,col_headings,data)

if __name__ == '__main__':
    pdf = Report1PDF()
    pdf.foot_msg1="Booked Seats =  3"
    heading ="View OPD slip"
    col_heading = ['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB']
    data = [['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB'],
            ['Rollno', 'kiran', 'female', 'Phone No', 'Address', 'Department', 'Course', 'DOB'],
            ['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB']]

    pdf.print_page(heading,col_heading,data)
    pdf.output('report1.pdf')
    os.system('report1.pdf ')