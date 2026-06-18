from fpdf import FPDF


def create_pdf(title, content):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    # Remove unsupported characters
    content = content.encode("latin-1", "ignore").decode("latin-1")

    for line in content.split("\n"):

        line = line.strip()

        if line == "":
            pdf.ln(5)
        else:
            pdf.multi_cell(190, 8, line)

    filename = "study_notes.pdf"
    pdf.output(filename)

    return filename

