#LOGOVANJE KORISNIKA

def logovanje(korisnickoIme,lozinka):
	if korisnickoIme in korisnici:
		if lozinka == korisnici[korisnickoIme]["lozinka"]:
			print("Logovanje je uspesno.")
			return True
	return False		



#ULOGUJ SE KORISNICE
def ulogujSe():
	while True:
		korisnickoIme= input("Korisnicko ime: ")
		if  len(korisnickoIme) == 0:
			print("Korisnicko ime ne moze biti prazno polje.")
		else:
			break
	while True:
		lozinka= input("Lozinka: ")
		if  len(lozinka) == 0:
			print("Lozinka ne moze biti prazno polje.")
		else:
			break

	if logovanje(korisnickoIme,lozinka):
		return session(korisnickoIme)
	else:
		print("Pogresno korisnicko ime ili lozinka.")			

							

#REGISTRACIJA KORISNIKA
def registrujSe():
	while True:
		korisnickoIme= input("'Novo korisnicko ime: ")
		if  len(korisnickoIme) ==0:
			print("Korisnicko ime ne moze biti prazno polje.")
			continue
		else:
			break
	while True:
		lozinka= input("Nova lozinka: ")
		if  len(lozinka) == 0:
			print("Lozinka ne moze biti prazno polje.")	
			continue
		else:
			break
	while True:
		ime= input("Unesite ime: ")
		if  len(ime) == 0:
			print("Ime ne moze biti prazno polje.")
			continue
		else:
			break
	while True:
		prezime= input("Unesite prezime: ")
		if  len(prezime) == 0:
			print("Prezime ne moze biti prazno polje.")
			continue
		else:
			break
	while True:
		kontaktTelefon= (input("Unesite kontakt telefon: "))
		if not len(kontaktTelefon) > 0:
			print("Kontakt telefon ne moze biti prazno polje.")
	
			continue
		else:
			break
	while True:
		emailAdresa= input("Unesite email adresu: ")
		if len(emailAdresa) == 0:
			print("Email adresa ne moze biti prazno polje.")
			continue
		else:
			break
	matricaZaUnos=[[korisnickoIme,lozinka,ime,prezime,kontaktTelefon,emailAdresa,"korisnik"]]
	dodajUDatoteku("korisnici.txt",matricaZaUnos)

#PREGLED HOTELA
def pregledHotela():
	

	
	

#def ponudaSoba():
	#print("Smestaj za goste\n========")
	#print("1. Jednokrevetna soba")
	#print("2. Dvokrevetna soba")
	#print("3. Trokrevetna soba")
	#print("4. Apartman")


#def jednokrevetna():
	#print("")









	

def glavniMeni():
	print("Glavni meni\n=========")
	print("1. Registracija korisnika")
	print("2. Prijava korisnika")
	print("3. Pregled hotela")
	print("4. Pretraga hotela")
	print("5. Prikaz najbolje ocenjenih hotela")
	print("0. Izlazak iz aplikacije")		
	
	while True:
		try:
			izbor= int(input("Izaberite stavku menija: "))
			if izbor <0 or izbor >5:
				print("Molimo unesite broj izmedju 0 i 5.")
				continue
			else:
				if izbor ==1:
					registrujSe()
					continue
				elif izbor ==2:
					ulogujSe()
					continue
				elif izbor ==3:
					pregledHotela()
					continue
				elif izbor ==4:
					pretragaHotela()
					continue
				elif izbor ==5:
					najboljiHoteli()
					continue	
				else:
					break
		except:
			print("Molimo unesite broj izmedju 0 i 5.")
			continue

	



def pretragaHotela():
	pass	

def najboljiHoteli():
	pass	
	
def dodajUDatoteku(nazivDatoteke,podaci):
	f=open(nazivDatoteke,"a")
	for niz in podaci:
		f.write("|".join(niz)+"\n")



if __name__ == '__main__':
	print("\t\t\t\tDobrodosli".upper())
	print("\t\tOvde mozete da rezervisete sobe u hotelu.")
	glavniMeni()			














		
									
















	#print("Pravljenje naloga...")
			



