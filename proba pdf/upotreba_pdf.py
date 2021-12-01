from fpdf import FPDF

pdf = FPDF(orientation="P", unit="pt", format="A4")
#Orijentacija je P, sto znaci da je portret mod, pt je skracenica za points, a po defaultu je mm, za unit (12pt = 16px), format je velicina papira, koji je papir

pdf.add_page()  #Dodajemo strane na ovaj nacin. Mozemo isto da im podesimo argumente, ali ih ostavljamo po defaultu, a to je portret, mm, A4

# Dodavanje teksta na sledeci nacin:
pdf.set_font(family="Times", size=24, style="B")  #Podesava tekst koji cemo mi da dodamo. Ovo "B" za style se odnosi na Bold
pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)  #Posmatramo ovo kao pravougaonik, ovaj cell i dodajemo mu sirinu i visinu koja zelimo da pude, a vrednost tih velicina je u pointima (pt). Ovo "C" je da poravnamo tekst, jer je C oznaka za centar. ln=1 znaci da ce sledeci cell ici u red ispod, a ako toga nema ici ce u red sa nama tj. do nas

# Za dodavanje jos teksta, ako nam treba koristimo jos jednu cell
pdf.cell(w=100, h=40, txt="Period:", border=1)  #Nismo dodali align, jer je po defaultu left, a mi to hocemo. Ako stavimo da je border=1, onda cemo imati ivice pravougaonika oko naseg teksta, a ako stavimo border=0, nema ivica pravougaonika

pdf.cell(w=150, h=40, txt="March 2021", border=1, ln=1)
pdf.output("bill.pdf")  #Ovo smo stavili kako ce da nam izgleda fajl koji mozemo da otvorimo, zato smo stavili ime fajla bill sa ekstenzijom pdf

# Pokrenemo fajl pomocu naseg pdf readera, tako sto kliklnemo dva puta na njega, ovde u VSC ili otvorimo folder gde nam je smeste fajl i pokrenemo ga
# Ako se pojavi greska OSError, to znaci da je fajl otvoren. Moramo da zatvorimo fajl, da bi nam radila izmena koju smo napravili
# Ako nam tekst izlazi iz pravougaonika, povecamo mu w u toj cell, kao sto je slucaj za Flatmates Bill
# Ako stavim da je w=0, kao sto je u nasem primeru, to znaci da ce cela povrsina biti zauzeta po vertikali, cell ce to da zauzme
