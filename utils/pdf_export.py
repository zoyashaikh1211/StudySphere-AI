from fpdf import FPDF


def create_pdf(title, content):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    filename = "StudySphere_Notes.pdf"

    pdf.output(filename)

    return filename