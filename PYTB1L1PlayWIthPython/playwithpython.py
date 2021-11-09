2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3

print('Mijn naam is Max')
naam = 'Max'
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])


leeftijd = 17
print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
leeftijd = leeftijd + 1
leeftijd
leeftijd-=1
leeftijd

if leeftijd < 17:
    hoelang_tot17jaar = 17 - leeftijd
    print('Over ' + str(hoelang_tot17jaar) + ' jaar wordt je 17')
elif leeftijd > 17:
    hoelang_al17jaar = leeftijd - 17
    print('Het is alweer ' + str(hoelang_al17jaar) + ' jaar geleden dat je 17 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    

from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %B %Y')

import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')