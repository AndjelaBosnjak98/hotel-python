import sys, traceback

def ulogujSe():
	
	korisnickoIme= input("Unesite vase korisnicko ime: ")
	lozinka= input("Unesite vasu lozinku: ")
	with open("korisnici.txt" , "r") as korisnici:
		for line in korisnici:
			loginInfo= line.split("|")
		if korisnickoIme == loginInfo[0] and lozinka == loginInfo[1]:
			print("\nUspesno ste se ulogovali.\n")
			return True
	print("\nUneli ste pogresne podatke.\n")
	return False	

			
				

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
	#import pdb; pdb.set_trace()
	with open("hotel.txt" , "r") as hoteli:
		for line in hoteli:
			#import pdb; pdb.set_trace()
			hotel= line.split("|")
			print("\nNaziv hotela: ")
			print(hotel[1]) 
			print("Adresa hotela: ")
			print(hotel[2])
			print("Sobe hotela: ")
			print(hotel[3])
			print("Bazen: ")
			print(hotel[4])
			print("Restoran: ")
			print(hotel[5])
			print("Ocena hotela: ")
			print(hotel[6],"\n===========================")


def pretragaHotela():
	print("\n\nPretraga hotela po jednom ili vise kriterijuma: \n")
	print("1. Pretraga po jednom kriterijumu.")
	print("2. Pretraga po vise kriterijuma.")		

	while True:
		try:
			choice=input("Izaberite stavku menija: ")
			choice=int(choice)

			if choice <0 or choice>3:
				print("Molimo unesite broj izmedju 1 i 3.")
				continue
			else:
				if choice == 1:
					print("\n1. Pretraga po nazivu: \n")
					print("\n2. Pretraga po adresi: \n")
					print("\n3. Pretraga po oceni: \n")


					odabir=input("Unesite kriterijum: ")
					odabir=int(odabir)

					if odabir == 1:
						print(hotel[1])
					elif odabir == 2:
						print(hotel[2])
					elif odabir == 3:
						print(hotel[6])	

					

					stavka=input("Unesite zeljeni kriterijum.")
					stavka=int(stavka)

					if stavka == 1:
						print(hotel[1])
						continue
					elif stavka == 2:
						print(hotel[2])
						continue
					elif stavka == 3:
						print(hotel[6])
						continue	
					else:
						break
		except:
			pass				



def glavniMeni():
	print("Glavni meni\n============")
	print("1. Registracija korisnika")
	print("2. Prijava korisnika")
	print("3. Pregled hotela")
	print("4. Pretraga hotela")
	print("5. Prikaz najbolje ocenjenih hotela")
	print("0. Izlazak iz aplikacije")		
	
	while True:
		try:
			izbor= input("Izaberite stavku menija: ")
			izbor = int(izbor)
			
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
		except Exception as e:
			print("Molimo unesite broj izmedju 0 i 5.")
			print('Stack trace:')
			exc_type, exc_value, exc_traceback = sys.exc_info()
			traceback.print_exception(exc_type, exc_value, exc_traceback,
                              		  limit=5, file=sys.stdout)
			continue





def najboljiHoteli():
	print("\nOvo su najbolje ocenjeni hoteli:\n")

	
def dodajUDatoteku(nazivDatoteke,podaci):
	f=open(nazivDatoteke,"a")
	for niz in podaci:
		f.write("|".join(niz)+"\n")


def citajIzDatoteke(nazivDatoteke):
	with open("korisnici.txt", "r") as korisnici:
		for korisnik in korisnici:
			korisnik.append("|".join(korisnik)+"\n")

		




if __name__ == '__main__':
	print("\n\n\t\t==> Dobrodosli! <==".upper())
	print("\n\t\tAplikacija za rezervacije hotela.\n\n".upper())
	korisnik= None
	glavniMeni()















		
									
















	#print("Pravljenje naloga...")
			



