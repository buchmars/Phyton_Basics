
# zeilenumbrüche und backslash
print("hallo Welt")
pfad 1 ='c:\reichlich'
pfad 2 ="c:\\reichlich"
print(pfad1)
print(pfad2)

kursnam e= 'Python Kurs'
print(kursname)
print("Hallo Welt")
print()
print("Leerzeile davor")

# testtext für zeilenumbrüche mit \n!
column s ='123456789012345678901234567890123456789012345678901234567890123456789'
testtex t= 'dies ist ein schöner tag!\n das wetter ist doof\n\n jeder dient der Heiligen Bockwurst'

print(columns)
print(testtext)

# ausgabe mit print(r) für eine rohe unverfälschte ausgabe

print(r"c:\niedlicherverzeichnisname")
# print(rpfad) => mit variablen funktioniert das so nicht richtig


print("\n\n\n")
# mehrere Zeilenumbrüche bei der Ausgabe
print ('mehrere Umbrüche')
print("/n")
print('''Hallo
Welt
-in 3 Zeilen''')

# mit doppelten Zeilenumbrüchen in 4 zeilen
print("/n")

print("""Hallo Bockwurst in
4
Zeilen
sogar!""")

# apostroph in Texten / Variablen nutzen!
# ausgabe = "Ku'damm für Kurfürstendamm" <-- Geht so nicht
# ausgabe = 'Ku'damm für für Kurfürstendamm' <-- Auch falsch
# ausgabe = 'Ku\\'damm für Kurfürstendamm' <-- mit 2 \\ um das ' zu escapen
ausgabe = 'Ku\\\' damm für Kurfürstendamm'
print(ausgabe)

print("\n\n\n\n\n")
# variablen sind wie schubladen oder Container.
# Regel nr.1 keine Leerzeichen in den Namen, unterstiche oder bindestriche nutzen!
# Regel nr2. Variablen mit ' oder "
# zum beispiel: meine_variable = "inhalt"
Axe l= "Test"
vornam e =Axel
print(vorname)
print("\n\n\n")

# Variable len () = gibt die länge der Variablen/string aus

kursname = 'Python lernen'

print(len(kursname))

print("\n\n\n\n\n")

# methoden werden mit . zum objekt verknüpft
# beispiel: pobjekt.methode auto.beschleunigen
# mit help(str) und doppelklick auf das gelbe kästchen kann man die optionen abrufen
# dir(str) kann man sich die möglichen methoden ausgeben lassen (im idle)

kursname = "Python lernen"
print(kursname.lower())

# teststring 2
# bei lower() & upper() werden ggf. die buchstaben umgeformt, ß = SS etc.
bockwurs t= "große Portion Bockwurst, bitte!"
print("bockwurst")
print(bockwurst.lower())
print(bockwurst.upper())
print("\n\n")

# mit lstrip() kann man leerzeichen entfernt werden
# mit lstrip() für left = links
# mit lstrip('1234567890) kann man auch gezielte Zeichen links entfernen
# strip() entfernt links als auch rechts zeichen
# rstip() entfernt nur rechts zeichen

# lstrip links
print(columns)
lstripbeispie l ="      leerzeichen ist vorne"
print("lstripbeispiel")
print("lstip()")
print(lstripbeispiel.lstrip())

# strip links und rechts
print("alle unerwünschten leerzeichen entfernen mit strip()")
print("\n")
print(columns)
beispie l ="       Bockwurst ist lustig eine Bockwurst ist schön     "
print(beispiel)
ausgab e =beispiel.strip()
print(ausgabe)

print("\n\n")

# rstrip rechts

print("jetzt alle rechtseitigen leerzeichen entfernen")
beispiel 2= "Lieber eine Bockwurst in der Hand, als einen Braten auf dem Dach          "
print(beispiel2 +"<<-- das löschen wir jetzt weg")
ausgabe = beispiel2.rstrip()
print(ausgabe + "alles weg, siehst du ;-)")

print("\n\n")

# zeichen mit strip und co entfernen
Print
