import sys
import tkinter

# wczytanie przepisow:
przepfile = open('drinki','r')
DRINKI = {}
SKLADNIKI = {}

for line in przepfile:
	if line.strip().startswith('#@'):
		continue
	action = line.strip().split(' ## ')
	name = action[0]
#	print(name)
	sklad = int(action[1])
	
	# wczytanie skladnikow
	skladnikiS = {}
	for i in range(sklad):
		skladnik = action[i+2].strip().split(' # ')
		nazwa_skladn = skladnik[0]
		ilosc_skladn = int(skladnik[1])
#		print('skladnik: ' + nazwa_skladn + ' | ilosc: ' + str(ilosc_skladn) + 'ml')
		skladnikiS[nazwa_skladn] = ilosc_skladn	
#	print(skladnikiS)
	
	# zapis skladnikow do slownika
	for i in skladnikiS:
		if i not in SKLADNIKI:
			SKLADNIKI[i] = [name]
		else:
			tmp = SKLADNIKI[i]
			if name in tmp:
				continue
			tmp.append(name)
			SKLADNIKI[i] = tmp
	
	# zapis przepisu na drink do slownika
	if name not in DRINKI:
		DRINKI[name] = [skladnikiS]
	else:
		tmp = DRINKI[name]
		tmp.append(skladnikiS)
		DRINKI[name] = tmp
		
'''
Reprezentacja wiedzy

DRINKI [ nazwa ] 
posiada tablice [ ] ze słownikiem { } składnik = ilość

print('')
print(DRINKI)	wszystkie drinki
print('')
print(DRINKI['Orgasm'])		wszystkie wariacje podanego drinku
print('')
print(DRINKI['Orgasm'][0])		konkretna wariacja podanego drinku
print('')
print(DRINKI['Orgasm'][0]['śmietanka'])		zwraca ilosc danego skladnika w danej wariacji drinku

SKLADNIKI [ nazwa ]
posiada tablice [ ] z drinkami jakie mozna ze skladnika zrobic

print('')
print(SKLADNIKI)	wyswietla slownik ze skladnikami
print('')
print(SKLADNIKI['sok_ananas'])		wyswietla jakie drinki mozna zrobic za pomoca konkretnego skladnika
'''

def menu():
	print('Co chcesz zrobic?')
	print(' 1. Konkretny Drink')
	print(' 2. Mam skladniki, co z nich moge zrobic')
	print(' 3. Zakoncz')
	return int(input('\tWybór: '))
	
def sprawdzIlosc(nazwa,skladnik):
	ile = len(DRINKI[nazwa])
	ilosc = 99999
	for i in range(ile):
		if skladnik in DRINKI[nazwa][i]:
			tmp = DRINKI[nazwa][i][skladnik]
			if tmp < ilosc:
				ilosc = tmp
				war = i
		else:
			continue
	return [str(ilosc) + 'ml',war]

def wypisz_sklad():
	drink = input('Podaj nazwe drinku: ')
	if drink not in DRINKI:
		print('Nie ma takiego drinku w bazie')
		return 'error'
	licznik = 0
	for i in DRINKI[drink]:
		print('Wariant ' + str(licznik+1) + ':\n')
		for skladnik in sorted(i):
			ilosc = str(DRINKI[drink][licznik][skladnik])
			print(ilosc + 'ml\t' + skladnik)
		print('')
		licznik += 1

def wypisz_driny():
	skladnik = input('Podaj nazwe skladnika: ')
	if skladnik not in SKLADNIKI:
		print('Nie ma takiego skłądnika w bazie')
		return 'error'
	print('Możesz zrobić:\n')
	for drin in SKLADNIKI[skladnik]:
		ilosc = sprawdzIlosc(drin,skladnik)
		wariant = ilosc[1]
		print(drin + ' (' + skladnik + ' ' + ilosc[0] + ')')
		print('   Dodatkowo potrzebujesz:')
		for sklad in sorted(DRINKI[drin][wariant]):
			if sklad == skladnik:
				continue
			ile = str(DRINKI[drin][wariant][sklad])
			print('    ' + ile + 'ml\t' + sklad)
	print('')

FLAG = True
while FLAG:
	opt = menu()
	if opt == 1:
		print('Lista Drinków:')
		for i in sorted(DRINKI):
			print('   ' + i)
		wypisz_sklad()
	elif opt == 2:
		print('Lista znanych skladnikow')
		for i in sorted(SKLADNIKI):
			print('   ' + i)
		wypisz_driny()
	else:
		FLAG = False