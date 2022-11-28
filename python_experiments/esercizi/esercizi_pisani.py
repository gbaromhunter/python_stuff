# Creare due tuple che rappresentino i due
# elenchi di nomi e cognomi descritti sotto:
# nomi: Numa, Tullo, Anco
# cognomi: Pompilio, Ostilio, Marzio
# Ottenere una lista in cui ogni elemento è un
# dizionario {'nome': nome, 'cognome':
# cognome}, che accoppia nomi e cognomi in
# base all'ordine.
# Esercizio 1
# Tipi contenitore

names = ("Numa", "Tullo", "Anco")
surnames = ("Pompilio", "Ostilio", "Marzio")
peoples = [{k: v for (k, v) in zip(("Name", "Surname"), (names[0], surnames[0]))},
           {k: v for (k, v) in zip(("Name", "Surname"), (names[1], surnames[1]))},
           {k: v for (k, v) in zip(("Name", "Surname"), (names[2], surnames[2]))}]

l = [{'nome': nome, 'cognome': cognome} for nome,
cognome in zip(names, surnames)]
