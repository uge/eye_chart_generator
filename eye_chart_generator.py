from fpdf import FPDF
import string as String
import random

def RandomLine(pdf=None, location=(40,10), font_size=16, number=0, count=10):
    s = ("%d" % number)
    pdf.text(location[0], location[1], s)

    for i in range(0,count):
        s = random.choice(String.ascii_uppercase)
        pdf.text(location[0] + 20 + (i*8), location[1], s)

if __name__ == "__main__":
    random_seed = random.randint(1,1000)
    random.seed(random_seed)

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font(family="Optician-Sans", style='', fname="./Optician-Sans.ttf", uni=True)
    pdf.set_font(family='Optician-Sans', style='', size=10)

    for i in range (1,21):
        RandomLine(pdf, location=(15,20 + 10*i), font_size=10, count=20, number=i)

    pdf.text(pdf.w//2, 10, ("%s" % random_seed))

    pdf.output(("chart-%d.pdf" % random_seed), 'F')