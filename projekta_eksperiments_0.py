
import random


Masivs1 = [ "1",
            "2",
            "3",
            "4",
            "4",]


Masivs2 = ["a",
           "b",
           "c",
           "d",
           "e"]


a=1


for i in range(a):

       
        jautajums = random.choice(Masivs1)
        
       
        indeks = Masivs1.index(jautajums)
        
        pareiza_atbilde = Masivs2[indeks]
        
        Masivs2.remove(pareiza_atbilde)
        
        random_atbilde = random.sample(Masivs2, 2)

        atbildes = [pareiza_atbilde] + random_atbilde
  
        random.shuffle(atbildes)
 
        print(jautajums)
        print("A. {}".format(atbildes[0]))
        print("B. {}".format(atbildes[1]))
        print("C. {}".format(atbildes[2]))
      
        lietotaja_ievade = input("Ievadiet atbildi(A, B, or C): ")
        
        if lietotaja_ievade.upper() == "A" and atbildes[0] == pareiza_atbilde:
            print("Pareizi!")
            
        elif lietotaja_ievade.upper() == "B" and atbildes[1] == pareiza_atbilde:
            print("Pareizi!")
            
        elif lietotaja_ievade.upper() == "C" and atbildes[2] == pareiza_atbilde:
            print("Pareizi!")
            
        else:
            print("Nepareizi")
            
   
        Masivs1.remove(jautajums)



   