'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
pomlcky = "-" * 40
#vytvoření slovníku se jménem a heslem + inputy
opravneni = {"bob": "123", "ann": "pass123", "mike": "password123", "liz":"pass123"}
jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej přihlašovací heslo: ")

# ověření jména a hesla + exit() pokud chybné
if opravneni.get(jmeno) == heslo:
    print(f'Welcome to the app, {jmeno}. We have 3 texts to be analyzed')
else:
    print(f'not certified user')
    exit()
print(pomlcky)

#vyber textu od uzivatele a jeho přiřazení do proměnné
try:
    volba = int(input(" Zadej zvolený text: "))
except ValueError:
    print("Nezadáno číslo")
    exit()
else:   
    if volba not in [1, 2, 3]:
        print("Zadáno číslo mimo  1,2,3")
        exit()
    else:
        zvoleny_text = TEXTS[volba - 1]
print(pomlcky)

#převedení na seznam a očištění
seznam_slov = zvoleny_text.split(" ")
ocistena_slova = [i.strip(",. \n") for i in seznam_slov]

#počet slov
text_pocet_slov = len(ocistena_slova)

# počet slov s prvním velkým písmenem
text_pocatecni_velka = 0
text_velka_vsechny = 0
text_mala_vsechny = 0

for word in ocistena_slova:
    if word.isupper() and word.isalpha():
        text_velka_vsechny += 1
    elif word.istitle():
        text_pocatecni_velka += 1
    elif word.islower() and word.isalpha():
        text_mala_vsechny += 1

# pocet cisel ve stringu jako celek
cisla_string = [nums for nums in ocistena_slova if nums.isnumeric()]

#Součet čísel jako celek 
cisla_string_soucet = 0
for num in cisla_string:
    cisla_string_soucet += int(num)

print(f'There are {text_pocet_slov} words in the selected text.')
print(f'There are {text_pocatecni_velka} titlecase words.')
print(f'There are {text_velka_vsechny} uppercase words.')
print(f'There are {text_mala_vsechny} lowercase words.')
print(f'There are {len(cisla_string)} numeric strings.')
print(f'The sum of all the numbers {cisla_string_soucet}')

# slovník klíč - indexy slov v ocistených slovech a hodnota - len tohto slova
delka_slova = 0
pocet_pismen = {}
for znak in ocistena_slova:
    pocet_pismen.setdefault(delka_slova, len(znak))
    delka_slova += 1
# přednastevení proměnných počtu písmen ve slovech
pocet_1 = 0
pocet_2 = 0
pocet_3 = 0
pocet_4 = 0
pocet_5 = 0
pocet_6 = 0
pocet_7 = 0
pocet_8 = 0
pocet_9 = 0
pocet_10 = 0
pocet_11 = 0
pocet_12 = 0
pocet_13 = 0

# výpočet počtu písmen ve slovech. Snažil jsem se to udělat jednodušeji, ale nepřišel jsem na to jak, proto takto jednotlivě.
for i in pocet_pismen:
    if pocet_pismen.get(i) == 1:
        pocet_1 += 1
    elif pocet_pismen.get(i) == 2:
        pocet_2 += 1
    elif pocet_pismen.get(i) == 3:
        pocet_3 += 1
    elif pocet_pismen.get(i) == 4:
        pocet_4 += 1
    elif pocet_pismen.get(i) == 5:
        pocet_5 += 1
    elif pocet_pismen.get(i) == 6:
        pocet_6 += 1
    elif pocet_pismen.get(i) == 7:
        pocet_7 += 1
    elif pocet_pismen.get(i) == 8:
        pocet_8 += 1
    elif pocet_pismen.get(i) == 9:
        pocet_9 += 1
    elif pocet_pismen.get(i) == 10:
        pocet_10 += 1
    elif pocet_pismen.get(i) == 11:
        pocet_11 += 1
    elif pocet_pismen.get(i) == 12:
        pocet_12 += 1
    elif pocet_pismen.get(i) == 13:
        pocet_13 += 1

# vtvoření slovníku, ze kterého se bude vybírat graf
final_slovnik = {"pocet_1": pocet_1, "pocet_2": pocet_2, "pocet_3": pocet_3, "pocet_4": pocet_4, "pocet_5": pocet_5, 
"pocet_6": pocet_6, "pocet_7": pocet_7, "pocet_8": pocet_8, "pocet_9": pocet_9, "pocet_10": pocet_10, "pocet_11": pocet_11, 
"pocet_12": pocet_12, "pocet_13": pocet_13}

print(pomlcky)
print("LEN      | OCCURENCES        | NUMBER")
print(pomlcky)

# vytvoření grafu
for index, znak in enumerate(final_slovnik):
    if final_slovnik.get(znak) == 0:
        continue
    else:
        print(index+1, final_slovnik.get(znak) * 'x', final_slovnik.get(znak))
