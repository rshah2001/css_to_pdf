from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
   # after adding a page you want to add anything you have to use cell
    pdf.add_page()
    # any cell that is created after the line below will have the Times font, bold and size of 12(in points and not mm)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(10, 20, 200, 22)

pdf.output("output.pdf")
