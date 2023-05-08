# Importēju random funkciju
import random

# Importēju matēmatiskās formulas
import math


Masivs1 = [

'ir valsts kurā atrodas viens no visvecākajiem ezeriem pasaulē, Ohridas ezers, kurš ir vairāk nekā 3 miljonus gadu vecs.',

'ir vienīgā valsts, kur oficiālā valoda ir katalāņu.',

'ir pirmā valsts, kura oficiāli pieņēma kristietību kā savu oficiālo reliģiju, tas notika 301. gadā.',

'ir valsts ar vecāko zoodārzu pasaulē, Šēnburnnas zodārzs, kuru atklāja 1752. gadā.',

'ir valsts ar viszemāko galvaspilsētu pasaulē, tā atrodas 28 metrus zem jūras līmeņa.',

'ir valsts ar vislielāko mežu visā Eiropā, Belovežas gārša, kurš arī ir UNESCO pasaules mantojuma sarakstā.',

' valsts, kurā runā 3 valodās, franču, nīderlandiešu un vācu.',

'ir valsts kurā kopš 1995. gada ir palikušas ap 180 000 neuzsprāgušas mīnas, kuras ir nogalinājušas 617. cilvēkus.',

'ir valsts, kurā tika izgudrots kirilica alfabēts.',

'šogad, 2023. gadā, oficiāli pievienojās eiro zonai kļūstot par 20. valsti, kas to izdara.',

'Kurā no šīm valstīm ir vairāk kaķu (1,5 miljoni) nekā cilvēku(1,2 miljoni)?',

'Kurā valstī dzer visvairāk alu(140 L uz 1 iedzīvotāju)?',

'ir valsts ar pasaulē vecāko karogu, kuru izmanto vēl mūsdienās.',

'Kura valsts izgudroja Skype?',

'ir jaunākā NATO dalībvalsts, tā pievienojās 2023. gada 4. aprīlī.',

'ir valsts, kura pasludinājusi jaunu republiku veselas 5 reizes, vairāk nekā jebkura cita valsts pasaulē.',

'ir valsts ar visdziļāko alu pasaulē, veseli 2212 metri dziļa.',

'ir valsts ar visvairāk pilīm pasaulē, aptuveni 25 tūkstoši piļu.',

'ir valsts, kurā tika filmētas visas Mamma Mia! Filmas.',

'Šī valsts galvas pilsēta izveidojās savienojoties trim pilsētām – Pesta, Obuda, Buda.',

'Pirmā valsts, kura atzina Latvijas neatkarības atjaunošanu.',

'Šī valsts ir uzvarējusi visvairāk Eirovīzijas, veselas 7 reizes.',

'Šajā valstī 1943. gadā notika apvērsums un tā sāka cīnīties sabiedroto pusē pret Ass valstīm.',

'Pasaulē ir 2 valsts, kuru karogā ir tās kontūra, otra ir Kipra, kas šī par valsti?',

'Džinsu izgudrotājs ir nācis no šīs valsts.',

'Šajā valstī netīšām iebruka Šveice, to izdarīja 171 karavīrs.',

'Vairākas valstis pieņem, ka tajās atrodas Eiropas ģeogrāfiskais centrs, bet vienīgais, ko atzīsts Pasaules Ginesa rekordi atrodas šajā valstī.',

'Kura valsts ir vienīgā joprojām pastāvošā hercogiste pasaulē?',

'Šī valsts ir piedalījusies Eirovīzijā 49 reizes, vairākas reizes bijusi top 3, bet nav kad nav uzvarējusi.',

'Šeit ir vismazāk tūristu visā Eiropā, tikai 11 tūkstoši gadā.',

'Šī valsts ir pazīstama ar tās kazino un F1 sacensībām.',

'Šeit atrodas Taras upes kanjons, kas ir vislielākais un dziļākais kanjons Eiropā',

'1672. gadā šīs valsts iedzīvotāji pēc viņu premjerministra nāvessoda izpildes apēda viņu.',

'Šeit dzimis viens no ievērojamākajiem ģenerāļiem, kurš jebkad dzīvojis – Aleksandrs lielais.',

'Kura valsts ir ieguvusi visvairāk ziemas olimpiskās medaļas, veselas 368.',

'_ir valsts ar Eiropas vecāko restorānu, Švidinka pagrabs(Piwnica Świdnicka)',

'Šeit atrodas Eiropas galējais rietumu punkts.',

'Šīs valsts parlaments atrodas lielākajā ēkā visā Eiropā un otrā lielākajā pasaulē, tās vērtība ir 4 miljardi dolāru.',

'Šeit atrodas pasaules dziļākais ezers – Baikāls.',

'Pasaulē vecākā valsts, to dibināja tālajā 301. gadā.',

'_ir lielākā aveņu, ābolu, plūmju un bumbieru eksportētāj valsts Eiropā.',

'_ir vienīgā valsts, kuras galvaspilsēta robežojas ar 2 citām valstīm.',

'Šajā valstī tika atklāts pasaulē vecākais koka ritenis, kurš ir 5000 gadus vecs.',

'ir valsts, kurā ilgāk nekā jebkurā citā valdīja fašistu diktators no 1939. līdz 1975. gadam',

'Šajā valstī ir 4 oficiālās valodas un viena no tām ir romiešu valoda(romansh)',

'Šī valsts ir Osmaņu impērijas pēctece un to izveidoja Ataturks 20. gs. sākumā.',

'Šī valsts atteicās no trešā lielākā kodolieroču arsenāla deviņdesmitajos',

' 100 gadiem šī valsts kontrolēja ¼ daļu no visas pasaules teritorijas.',

'95% procenti šīs valsts iedzīvotāju ir vīrieši.',

'Pirmais nacionālais parks tika izveidots šajā valstī 1909. gadā, kurš ir 1970 km2 liels.'

]

Masivs2 = [

'Albānija',

'Andora',

'Armēnija',

'Austrija',

'Azerbaidžāna',

'Baltkrievija',

'Beļģija',

'Bosnija un Hercegovina',

'Bulgārija',

'Horvātija',

'Kipra',

'Čehija',

'Dānija',

'Igaunija',

'Somija',

'Francija',

'Gruzija',

'Vācija',

'Grieķija',

'Ungārija',

'Islande',

'Īrija',

'Itālija',

'Kosova',

'Latvija',

'Lihtenšteina',

'Lietuva',

'Luksemburga',

'Malta',

'Moldova',

'Monako',

'Melnkalne',

'Nīderlande',

'Maķedonija',

'Norvēģija',

'Polija',

'Portugāle',

'Rumānija',

'Krievija',

'San Marino',

'Serbija',

'Slovākija',

'Slovēnija',

'Spānija',

'Šveice',

'Turcija',

'Ukraina',

'Lielbritānija',

'Vatikāns',

'Zviedrija'

]

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

# Izveidoju funkciju lai izreiķinātu procentus
def procentu_formula(pareizi, kopa):
    procenti = (pareizi / kopa) * 100
    return procenti
# Izrēķinu procentus un to snoapaļoju
kopa = pareizi+nepareizi
procenti = procentu_formula(pareizi, kopa)
noapaloti_procenti = math.ceil(procenti)
print('Tava precizitāte bija '"{}%".format(noapaloti_procenti))

            
   