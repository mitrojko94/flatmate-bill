from fpdf import FPDF
import webbrowser
#import os

class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts and the period of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename
    
    def generate(self, flatmate1, flatmate2, bill):

        #flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2)))
        #flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2)))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        #Add icon
        pdf.image(name="files/house.png", w=30, h=30)  #Na ovaj nacin dodamo slike, imaju dva parametra, prvi je ime slike ili putanja do nje, a drugi je velicina slike

        #Insert title
        pdf.set_font(style="B", size=24, family="Times")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, ln=1, align="C")
        
        #Insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, border=0, ln=1, txt=bill.period)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)  #Nismo stavili style, jer je po defaultu normalan
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, border=0, ln=1, txt=str(round(flatmate1.pays(bill, flatmate2), 2)))  #Ubacimo u metodu pays parametre koje ima metoda generate. Stavili smo pre teksta str, da bi to sve konvertovali u string, jer je to bilo float, a float i string ne mogu zajedno
        # Stavili smo round da zaokruzimo broj na 2 decimale, zato imamo round, a posle prvog parametra broj 2, jer su 2 decimale

        #Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, border=0, ln=1, txt=str(round(flatmate2.pays(bill, flatmate1), 2)))

        #os.chdir("files") Menjam direktorijum sa Flatmate Bill na files -> Flatmate Bill/files
        pdf.output(self.filename)  #Sad ce ovde da stoji ime koje mi stavimo dole, tj. onako kako definisemo naziv pdf fajla

        webbrowser.open(self.filename)  #Ovo je komanda da kada spozovemo ovu metodu da se automatski otvori pdf fajl sa ovim podacima
