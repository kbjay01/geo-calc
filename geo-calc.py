# -*- coding: utf-8 -*-
# Coded by KBJay
import math
print('Wybierz figure:')
print('1. Kwadrat')
print('2. Prostokat')
print('3. Trojkat')
print('4. Romb')
print('5. Trapez')
print('')
wybor = input('[1-4] Wybieram: ')

listWyborow = ['1','2','3','4','5']
listKwadrat = ['1','2','3']
listProstokat = ['1','2','3']
listTrojkat = ['1','2','3']
listRomb = ['1','2']
listTrapez = ['1','2']
if wybor not in listWyborow:
  print('[!] Blad. Podano wybor z poza dozwolonego zakresu')


def handler(shape,var1,var2,var3):
	if shape == 'kwadrat' or 'romb' and var2 == False and var3 == False:
		var2 = 0
		var3 = 0
	elif shape == 'prostokat' or 'trojkat' or 'romb2' and var3 == False:
		var3 = 0
	try:
		print('')
		var1 = float(var1)
		var2 = float(var2)
		var3 = float(var3)
	except ValueError:
		print('[!] Blad. Podawane dlugosci musza byc liczbami')
		exit()
  
def kwadrat():
	figura = 'kwadrat'
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
			handler(figura,kw_a,False,False)
			pole_kwadratu = float(kw_a) ** 2
			print('Pole kwadratu wynosi: ' + str(pole_kwadratu))
		
		elif wyborKwadrat == '2':
			# Obwod kwadratu
			kw_a = input('Podaj dlugosc boku a: ')
			handler(figura,kw_a,False,False)
			kw_obwod = float(kw_a) * 4
			print('Obwod kwadratu wynosi: ' + str(kw_obwod))
		
		elif wyborKwadrat == '3':
			#Dlugosc przekatnej kwadratu
			kw_a = input('Podaj dlugosc boku a: ')
			handler(figura,kw_a,False,False)
			print('Dlugosc przekatnej kwadratu wynosi: ' + str(kw_a) + '√2')
			przekatna_kwadratu = math.sqrt(2) * float(kw_a)
			print('Dokladny wynik: ' + str(przekatna_kwadratu))
			
def prostokat():
	figura = 'prostokat'
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
			handler(figura,pro_a,pro_b,False)
			pro_pole = float(pro_a) * float(pro_b)
			print('Pole prostokatu wynosi: ' + str(pro_pole))
		
		if wyborProstokat == '2':
			# Obwod prostokatu
			pro_a = input('Podaj dlugosc boku "a": ')
			pro_b = input('Podaj dlugosc boku "b": ')
			handler(figura,pro_a,pro_b,False)
			pro_obwod = 2 * (float(pro_a) + float(pro_b))
			print('Obwod tego prostokatu wynosi: ' + str(pro_obwod))
			
		if wyborProstokat == '3':
			# Dlugosc przekatnej prostokatu
			pro_a = input('Podaj dlugosc boku "a": ')
			pro_b = input('Podaj dlugosc boku "b": ')
			handler(figura,pro_a,pro_b,False)
			pro_liczba_podpierwiastkowa = float(pro_a) ** 2 + float(pro_b) ** 2
			pro_przekatna = math.sqrt(pro_liczba_podpierwiastkowa)
			print('Przekatna tego kwadratu wynosi: √ ' + str(pro_liczba_podpierwiastkowa))
			print('Dokladny wynik: ' + str(pro_przekatna))
		
def trojkat():
	figura = 'trojkat'
	print('Co chcesz obliczyc?')
	print('1. Pole')
	print('2. Obwod')
	print('3. Dlugosc przeciwprostokatnej [dotyczy Trojkata Prostokatnego]')
	wyborTrojkat = input('Wybieram[1-3]: ')
	
	if wyborTrojkat not in listTrojkat:
		print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
	elif wyborTrojkat in listTrojkat:
		
		if wyborTrojkat == '1':
			#Pole
			tr_a = input('Podaj dlugosc podstawy: ')
			tr_h = input('Podaj wysokosc trojkata: ')
			handler(figura,tr_a,tr_h,False)
			tr_pole = (float(tr_a) * float(tr_h))/2
			print('Pole tego trojkata wynosi: ' + str(tr_pole))
		
		if wyborTrojkat == '2':
			#Obwod
			figura = 'trojkat3'
			tr_a = input('Podaj dlugosc boku "a": ')
			tr_b = input('Podaj dlugosc boku "b": ')
			tr_c = input('Podaj dlugosc boku "c": ')
			handler(figura,tr_a,tr_b,tr_c)
			tr_obwod = float(tr_a) + float(tr_b) + float(tr_c)
			print('Obwod tego trojkata wynosi: ' + str(tr_obwod))
			
		if wyborTrojkat == '3':
			#Pitagoras przeciwprostokatnej
			tr_a = input('Podaj dlugosc przyprostokatnej "a": ')
			tr_b = input('Podaj dlugosc przyprostokatnej "b": ')
			handler(figura,tr_a,tr_b,False)
			tr_przeciwprostokatna = float(tr_a) ** 2 + float(tr_b) ** 2
			print('Dlugosc przeciwprostokatnej tego trojkata wynosi: √' + str(tr_przeciwprostokatna))
			print('Czyli dokladnie: ' + str(math.sqrt(tr_przeciwprostokatna)))

def romb():
	print('Co chcesz obliczyc?')
	print('1. Pole')
	print('2. Obwod')
	wyborRomb = input('Wybieram [1-2]: ')
	if wyborRomb not in listRomb:
		print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
	elif  wyborRomb in listRomb:
		
		if wyborRomb == '1':
			#Pole
			figura = 'romb2'
			print('')
			print('Jakie posiadasz dane?')
			print('1. Wysokosc i dlugosc podstawy')
			print('2. Dlugosci przekatnych')
			podWyborRomb = input('Znam[1-2]: ')
			if podWyborRomb in listRomb:
				if podWyborRomb == '1':
					r_a = input('Podaj dlugosc podstawy: ')
					r_h = input('Podaj wysokosc: ')
					handler(figura,r_a,r_h,False)
					r_pole = float(r_a) * float(r_h)
					print('Pole tego rombu wynosi: ' + str(r_pole))
				
				elif podWyborRomb == '2':
					r_e = input('Podaj dlugosc jednej z przekatnych: ')
					r_f = input('Podaj dlugosc drugiej przekatnej: ')
					handler(figura,r_e,r_f,False)
					r_pole = (float(r_e) * float(r_f))/2
					print('Pole tego rombu wynosi: ' + str(r_pole))

			if podWyborRomb not in listRomb:
				print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
			
		if wyborRomb == '2':
			#Obwod
			figura = 'romb'
			r_a = input('Podaj dlugosc boku: ')
			handler(figura,r_a,False,False)
			r_obwod = float(r_a) * 4
			print('Obwod tego rombu wynosi: ' + str(r_obwod))
def trapez():
	print('Co chcesz policzyc?')
	print('1. Pole')
	print('2. Obwod')
	wyborTrapez = input('Wybieram: ')
	if wyborTrapez not in listTrapez:
		print('[!] Blad. Podano wybor z poza dozwolonego zakresu')
	elif wyborTrapez in listTrapez:
		
		if wyborTrapez == '1':
			#Pole
			figura = 'trapez'
			trap_a = input('Podaj dlugosc podstawy: ')
			trap_b = input('Podaj dlugosc drugiej podstawy: ')
			trap_h = input('Podaj wysokosc: ')
			handler(figura,trap_a,trap_b,trap_h)
			poleTrapezu = (float(trap_a) + float(trap_b)) / 2 * float(trap_h)
			print('Pole tego trapezu wynosi: ' + str(poleTrapezu))
						
if wybor == '1':
	kwadrat()
elif wybor == '2':
	prostokat()
elif wybor == '3':
	trojkat()
elif wybor == '4':
	romb()
elif wybor == '5':
	trapez()
