int score = 0

print ("Hello you")
print ("Ik ben Max")

x  = input("Wie ben jij? \nN")
print ('Hello,' + x) 

print ("Ik ben nieuw op het Mediacollege in Amsterdam door een paar vragen aan mijn te stellen kom je meer over mij te weten!")

#Vraag 1
antwoord1 = input("Waar kom ik vandaag? \na. Leiden \nb. Leiderdorp \nc. Rijpwetering \nAntwoord: ")
if antwoord1 == "c" or antwoord1 == "Rijpwetering":
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n")

else:
    print("Dat antwoord was niet goed! Het antwoord is Rijpwetering")
    print ("score:", score)
    print ("\n")

#Vraag 2
antwoord2 = input("Hoe oude denk je dat ik ben? \na. 16 \nb. 17 \nc. 18 \nAntwoord: ")
if antwoord2 == "b" or antwoord2 == "17":
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n") 

else: 
    print("Dat antwoord was niet goed!")
    print ("score:", score)
    print ("\n")

    