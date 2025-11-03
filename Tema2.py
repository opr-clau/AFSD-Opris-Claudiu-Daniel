elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")\

nota_minima = min(note)
nota_maxima = max(note)
print(nota_minima)
print(nota_maxima)

media = sum(note) / len(note)
print(media)

for i in range(len(note)):
    if note[i] >= 5:
        print (f"{note[i]} {elevi[i]}")

for i in range(len(note)):
    if note[i] < 10:
        print(note[i] + 1)

elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)

index = elevi.index(elev_de_sters)
print(index)
index = note.index(4)
print(index)
elevi.pop(index)
note.pop(index)
print(elevi)
print(note)

print()

while interogari_nume == elevi:
    interogari_nume == "stop"
    print(interogari_nume)
    print(note[interogari_nume])
else:
    print("nu exista")

for i in range(len(note)):
    note_promovanti = note[i]
    if note_promovanti >= 5:
        print(f"{note_promovanti} {elevi[i]}")

for i in range(len(note)):
    note_respinsi = note[i]
    if note_respinsi < 5:
        print(f"{note_respinsi} {elevi[i]}")



