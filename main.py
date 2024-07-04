from fpdf import FPDF
import pandas as pd

# Initialize PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Load data from CSV
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add a new page
    pdf.add_page()

    # Set title font and color
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw a line
    pdf.line(10, 22, 200, 22)

    # Add space at the bottom of the first page
    pdf.ln(265)

    # Set footer for the first page
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add additional pages if required
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)

        # Set footer for additional pages
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Output the PDF to a file
pdf.output("output.pdf")
