print('hi man, i have for you fantastic list of serials with raate, enjoy ')
serials={							#tworzenie biblioteki, to po lewej odpowiada temu po prawej
'Robin Hood-mans in trausers' : 7,
'Fight Clab' : 9,
'Narnia Stories' : 8,
'Sworld art online' : 10,
'The Witcher' : 10,
'Lucyfer': 10,
'Pirates' :8

}

print (list(serials.keys())) #wyświetlenie kluczy
print('***************************************')


name = input('Jaki serial chcesz obejrzec? ') #przypisywanie do name z klawiatury
print("Serial {} otrzymał ocenę {}".format(name, serials[name])) #wyswietla zamiast {} przypisana wartosc
													#do zmiennej name oraz wywoluje ocene z biblioteki
													#za pomoca zmiennej name
print('Czy chcesz dodać film do spisu?')
print('nie masz wyboru :)')

new=input('jaki serial chcesz dodac?')  #przypisuje wartosc do zmiennej new
rating=input('Jaka ocene otrzymal ' +new+ '?')	#przypisuje wartosc do zmiennej rating i wyswietla zmienna new
serials[new]=float(rating)	#dodaje wartosc do biblioteki ze zmiennej new ktora jest porownana do oceny

print('*********************************************')
print(list(serials.keys())) #wyswietla biblioteke w formir listy