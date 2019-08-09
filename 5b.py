print('ile masz lat?')
Age= int(input())
if(Age>=18):
	
	print('Uzytkownik pelnioletni')
	if(Age>100):
		print('200 lat')
else:
	
	print('Uzytkownik niepelnioletni, do osiagniecia pelnioletnosci pozostalo ci:',18-Age,'lat')