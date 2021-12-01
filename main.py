from flat import Bill, Flatmate
from reports import PdfReport


amount_input = float(input("Hey user, enter the bill amount: "))
period_input = input("What is the bill period? E.g. December 2020: ")

person_one = input("What is your name? ")
person_one_day = int(input(f"How many days did {person_one} stay in the house during the bill period? "))

person_two = input("What is the name of the other flatmate: ")
person_two_day = int(input(f"How many days did {person_two} stay in the house during the bill period? "))

the_bill = Bill(amount=amount_input, period=period_input)
john = Flatmate(name=person_one, days_in_house=person_one_day)
marry = Flatmate(name=person_two, days_in_house=person_two_day)

print(f"{person_one} pays: ", john.pays(bill=the_bill, flatmate2=marry))  #Stavili smo istancu od Bill klase da nam je jednaka nasem bill
print(f"{person_two} pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)