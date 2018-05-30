# Coded by KBJay
import math
print('Wybierz figure:')
print('1. Kwadrat')
print('2. Prostokat')
print('3. Trojkat')
print('4. Romb')
print('')
wybor = input('[1-4] Wybieram: ')

listWyborow = ['1','2','3','4']
listKwadrat = ['1','2','3']
listProstokat = ['1','2','3']

if wybor not in listWyborow:
  print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
  
def kwadrat():
	print('Co chcesz policzyc?')
	print('1. Pole')
	print('2. Obwod')
	print('3. Dlugosc przekatnej')
	wyborKwadrat = input('Wybieram[1-3]: ')
	
	if wyborKwadrat not in listKwadrat:
		print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
	
	elif wyborKwadrat in listKwadrat:
		
		if wyborKwadrat == '1':
			# Pole kwadratu
			kw_a = input('Podaj dlugosc boku a: ')
			print('')
			try:
				kw_a = float(kw_a)
			except ValueError:
				print('[!] Blad. Dlugosc boku "a" musi byc liczba')
				exit()
			
			pole_kwadratu = kw_a**2
			print('Pole kwadratu wynosi: ' + str(pole_kwadratu))
		
		if wyborKwadrat == '2':
			# Obwod kwadratu
			kw_a = input('Podaj dlugosc boku a: ')
			try:
				kw_a = float(kw_a)
			except ValueError:
				print('[!] Blad. Dlugosc boku "a" musi byc liczba')
				exit()
			
			kw_obwod = kw_a * 4
			print('Obwod kwadratu wynosi: ' + str(kw_obwod))
		
		if wyborKwadrat == '3':
			#Dlugosc przekatnej kwadratu
			kw_a = input('Podaj dlugosc boku a: ')
			print('')
			try:
				kw_a = float(kw_a)
			except ValueError:
				print('[!] Blad. Dlugosc boku "a" musi byc liczba')
				exit()
				
			print('Dlugosc przekatnej kwadratu wynosi: ' + str(kw_a) + '√2')
			przekatna_kwadratu = math.sqrt(2) * kw_a
			print('Dokladny wynik: ' + str(przekatna_kwadratu) + '...')
			
def prostokat():
	print('Co chcesz policzyc?')
	print('1. Pole')
	print('2. Obwod')
	print('3. Dlugosc przekatnej')
	wyborProstokat = input('Wybieram [1-3]: ')
	
	if wyborProstokat not in listProstokat:
		print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
	
	elif wyborProstokat in listProstokat:
		
		if wyborProstokat == '1':
			# Pole prostokatu
			pro_a = input('Podaj dlugosc boku "a": ')
			pro_b = input('Podaj dlugosc boku "b": ')
			print('')
			
			try:
				pro_a = float(pro_a)
				pro_b = float(pro_b)
			except ValueError:
				print('[!] Blad. Dlugosc bokow "a" i "b" musi byc liczba')
				exit()
			
			pro_pole = pro_a * pro_b
			print('Pole prostokatu wynosi: ' + str(pro_pole))
		
		if wyborProstokat == '2':
			# Obwod prostokatu
			pro_a = input('Podaj dlugosc boku "a": ')
			pro_b = input('Podaj dlugosc boku "b": ')
			print('')
			
			try:
				pro_a = float(pro_a)
				pro_b = float(pro_b)
			except ValueError:
				print('[!] Blad. Dlugosc bokow "a" i "b" musi byc liczba')
				exit()
			pro_obwod = 2 * pro_a + 2 * pro_b
			print('Obwod tego prostokatu wynosi: ' + str(pro_obwod))
			
		if wyborProstokat == '3':
			# Dlugosc przekatnej prostokatu
			pro_a = input('Podaj dlugosc boku "a": ')
			pro_b = input('Podaj dlugosc boku "b": ')
			print('')
			
			try:
				pro_a = float(pro_a)
				pro_b = float(pro_b)
			except ValueError:
				print('[!] Blad. Dlugosc bokow "a" i "b" musi byc liczba')
				exit()
			pro_liczba_podpierwiastkowa = pro_a ** 2 + pro_b ** 2
			pro_przekatna = math.sqrt(pro_liczba_podpierwiastkowa)
			print('Przekatna tego kwadratu wynosi: √ ' + str(pro_liczba_podpierwiastkowa))
			print('Dokladny wynik: ' + str(pro_przekatna) + '...')

if wybor == '1':
	kwadrat()
elif wybor == '2':
	prostokat()
