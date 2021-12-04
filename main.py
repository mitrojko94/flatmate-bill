from flask.views import MethodView
from wtforms import Form, StringField  #Importovali smo StringField koji nam omogucava rad sa forms
from flask import Flask, render_template, request
from wtforms.fields.simple import SubmitField  #Importovali smo SubmitField koji nam omogucava rad sa buttons
from flatmates_bill.flat import Bill, Flatmate
#ovo iznad mozemo da napisemo na drugi nacin, tipa from flatmates_bill import flat, a onda dole u kodu kucamo uvek flat.Bill, jer je flat ime fajla gde se nalazi klasa Bill


app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")  #Ubacio sam metodu render_template koja mi vraca html, a za putanju sam dodao samo index.html, bez templates, jer Flask zna da je folder templates i da se nalazi u istom folderu kao i main.py, zato je jako bitno nazvati taj folder templates


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()  #Inicijalizovali smo BillForm
        return render_template("bill_form_page.html", billform=bill_form)  #Dodajemo billform da mi instancu te klase dodali u html fajl
    
    #Dodajemo post metodu da bi mogli da radimo sa zahtevom ka serveru tj. da nam se pokazu rezultati na ovoj stranici, bill form page
    def post(self):
        pass
        #Treba da ima isti kod kao i post metoda u klasi ResultsPage, samo imamo male izmene
        #Vracamo saada bill_form_page html, a ne results html i moramo ove varijable koje vracamo da dodamo u html bill form page, ispod dugmeta
        #Na sve ove dodate argumente, kao sto su name1, name2 i slicno dodajemo i argument za billform=billform, jer moramo da ih ukljucimo u formu
        #Dodamo varijablu za results=True

class ResultsPage(MethodView):
    def post(self):  #Ovde staviti post, jer mi saljemo podatke, tako sto unosimo vrednosti, a da je get, samo bi ih citali
        billform = BillForm(request.form)  #Ovo sada radimo da ekstraktujemo podatke koje korisnik unese
        
        amount = float(billform.amount.data)  #Ova varijabla je jednaka amount vidzetu i stavimo data da bi pristupili njenim podacima
        period = billform.period.data
        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)  #Ovo smo pretvorili u float da bi dobili decimalni broj, jer da nemamo ovo pretvara se u string i onda imamo gresku u deljenju
        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        
        the_bill = Bill(amount=amount, period=period)
        #Moze da se napise i ovako: the_bill = Bill(billform.amount.data, billform.period.data), da uopste nemamo varijable za period i amount
        flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
        flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)
        
        return render_template("results.html", name1=flatmate1.name, 
                                                amount1=round(flatmate1.pays(bill=the_bill, flatmate2=flatmate2), 2),  #Stavili smo round, da zaokruzimo vrednost na dve decimale
                                                name2=flatmate2.name,
                                                amount2=round(flatmate2.pays(bill=the_bill, flatmate2=flatmate1), 2))  #Ovako smo stavili, da bi mogli u results.html da ih upotrebimo

class BillForm(Form):  #Ovo nismo nasledili od MethodForme, jer je ovo cista forma
    amount = StringField("Bill Amount: ", default=100)  #Iskoristili smo StringField da napravimo label za amount i period
    period = StringField("Bill Period: ", default="December 2020")  #Dodali smo drugi argument default, da uvek imamo neke vrednosti na stranici

    name1 = StringField("Name: ", default="Jelena")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Darko")
    days_in_house2 = StringField("Days in the house: ", default=12)

    button = SubmitField("Calculate")



app.add_url_rule("/", view_func=HomePage.as_view("home_page"))  #Dodali smo url adresu za nasu aplikaciju. Kad imamo samo / to je home_paige, a kroz jos nesto onda su ostale stranice
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))  #Ovom metodom add_url_rule dodajemo path za web, nasoj aplikaciji
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))
 
app.run(port=5000, debug=True)  #Dodavanjem debug ne moram svaki put da gasim i palim server, vec ce on sam da ucitava promene


#Precica za promenu slova u browseru je crtl+shift+r