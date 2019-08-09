name=input('please, give me your name  ')
surname=input('please, give me your surname')
telnumber=input('please, give me your telephone number')

print("Czy imię składa się tylko z liter?", name.isalnum())
print("Czy nazwisko składa się tylko z liter?", surname.isalnum())
print("Czy numer telefonu składa się z cyfr", telnumber.isdigit())

name=name.capitalize()
surname=surname.capitalize() #pierwsza litera ciagu z duzej
telnumber=telnumber.replace(' ','').replace('-', '') #najpierw zamienia spacje na puste a potem myslnik na puste

print(name, surname)
print(telnumber)

print('jest to imie kobiece', name.endswith('a'))
personal=name+' '+surname+' '+telnumber
print(personal)
print(len(personal))
print(len(name+surname))