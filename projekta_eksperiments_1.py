# Importēju random funkciju
import random

# Importēju matēmatiskās formulas
import math


Masivs1 = [ "_ is home to one of the oldest lakes in the world, Lake Ohrid, which is over three million years old.",
            "_ is the only country in the world whose official language is Catalan.",
            "_ has the oldest zoo in the world, the Tiergarten Schönbrunn, which was founded in 1752.",
            "_ is home to the largest forest in Europe, the Białowieża Forest, which is also a UNESCO World Heritage site.",
            "_ produces over 220,000 tons of chocolate per year, making it one of the largest chocolate producers in the world.",]


Masivs2 = ["Albania",
    "Andor",
    "Austria",
    "Belarus",
    "Belgium"]

pareizi=0
nepareizi=0
a=0

a=int(input('Cik daudz jautājumus jūs gribat lai jums uzdod (1-48)? - ')) 
for i in range(a):

        # Pēc nejaušas izvēles paņem jautājumu no pirmā masīva
        jautajums = random.choice(Masivs1)
        
        # Atrod paņemtā masīva skaitļa indeksu
        indeks = Masivs1.index(jautajums)
        
        # Atrod valsts nosaukumu no otrā masīva ar to pašu indeksu no pirmā masīva
        pareiza_atbilde = Masivs2[indeks]
        
        # Noņem valsts nosaukumu no 2. masīva
        Masivs2.remove(pareiza_atbilde)
        
        # Paņem 2 nepareizas atbildes no 2. masīva
        random_atbilde = random.sample(Masivs2, 2)
        
        # Savieno pareizo un nepareizās atbildes vienā masīvā
        atbildes = [pareiza_atbilde] + random_atbilde
        
        # Samaisa masīvu lai atbildes būtu nezināmā secībā
        random.shuffle(atbildes)
        
        # Izprintē atbildes un jautājumu
        print(jautajums)
        print("A. {}".format(atbildes[0]))
        print("B. {}".format(atbildes[1]))
        print("C. {}".format(atbildes[2]))
        
        # Saņem programmas lietotāja atbildi
        lietotaja_ievade = input("Ievadiet atbildi(A, B, or C): ")
        
        # Pārbauda vai lietotāja atbilde ir pareiza vai nepareiza
        if lietotaja_ievade.upper() == "A" and atbildes[0] == pareiza_atbilde:
            print("Pareizi!")
            pareizi+=1
        elif lietotaja_ievade.upper() == "B" and atbildes[1] == pareiza_atbilde:
            print("Pareizi!")
            pareizi+=1
        elif lietotaja_ievade.upper() == "C" and atbildes[2] == pareiza_atbilde:
            print("Pareizi!")
            pareizi+=1
        else:
            print("Nepareizi. Pareizā atbilde ir {}.".format(pareiza_atbilde))
            nepareizi+=1
        
        # Noņem jautājumu no 1. masīva
        Masivs1.remove(jautajums)
# Izvada cik atbildes bija pareizas un nepareizas
print('Jums bija',pareizi,'pareizas atbildes un',nepareizi,'nepareizas')


   