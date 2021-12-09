list_1 = [15,48, 'kakadu' ,59,12,'gaven','154',12.4,'Dert','sjdk sd','Fkjhh','GGIHHH']


print(f'{list_1=}'.split('=')[0])#ismeta = ir padalina i dvi dalis
print(f'{list_1=}'.split('=')[1])#ismeta = ir padalina i dvi dalis
print(f'{list_1[11]}'.partition('I'))#padalina eilute i tris dalis pazymeta dalis bus per viduri o kitos is abieju pusiu
print(f'{list_1=}'.find('i'))# returns index of a symbol
print(f'{list_1[0]}'.join(['asd', 'sd','gh','jk']))#asd[0]sd[0]gh[0] ir tt

print(f'{list_1[5]}'.title())#grazina kopija is didziosios raides
print(f'{list_1[2]}'.upper())#grazina kopija su visomis didziosiomis raidemis
print(f'{list_1}'.index('['))#grazina indeksa bet jeigu su {} tada indeksas [ yra 0
print(f'{list_1[11]}'.lower())#konvertuoja is didziuju i mazasias
print(f'{list_1[5]}'.swapcase())#konvertuoja i didziasias raides ir atvirksciai
print(f'{list_1[5]}'.capitalize())#grazina is didziosios raides
print(f'{list_1[10]}'.casefold())#padaro viska mazosiom raidem


print(f'{list_1[2]}'.endswith('du'))# tikrina zodis 'kakadu' baigiasi su du
print(f'{list_1[5]}'.endswith('gaven',0,5))#raides nuo 0 iki 5 pasirinkte listo indexo string reiksmeje
print(f'{list_1[2]}'.startswith('ka'))# tikrina ar eilute prasideda su 'ka'
print(f'{list_1[5]}'.startswith('gaven',0,5))#tikrina ar 5 nario nuo 0 iki 5 prasideda su gaven


print(f'{list_1[7]}'.isalnum())#grazina True jeigu alpha numeric 1254 arba abcds
print(f'{list_1[5]}'.isalpha())#grazina True jeigu alpha abcde
print(f'{list_1[5]}'.isascii())#grazina True jeigu ascii - all kind of weird symbols that don't belong in keyboard
print(f'{list_1[1]}'.isdecimal())#grazina True jeigu decimal
print(f'{list_1[0]}'.isdigit())#grazina True jeigu eilute string neturiu jokiu kitu simboliu kaip sveiki skaiciai
print(f'{list_1[8]}'.islower())#grazina True jeigu eilute string prasideda is mazosios raides
print(f'{list_1[7]}'.isnumeric())#grazina True numeric(paguglinti numeric, nes ten kazkokios raides ir skaiciai tik, + - ir pan)
print(f'{list_1[7]}'.isprintable())#grazina True jeigu eile spausdinama
print(f'{list_1[9][4]}'.isspace())#grazina True jei eiluteje yra tarpas
print(f'{list_1[10]}'.istitle())#grazina True jeigu eilute prasideda is didziosios raides(pavadinimas)
print(f'{list_1[11]}'.isupper())#grazina True jei visos raides eiluteje yra didziosios