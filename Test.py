from Distance import editDistance
from Ngram import Ngrams


# creazione file per bigrammi
def filebigram():
    alphabet = __import__("string").lowercase
    for letter1 in alphabet:
        for letter2 in alphabet:
            nomefile = 'file-' + letter1 + letter2 + '.txt'
            open(nomefile, "w")
    nomi = open("nomi.txt", "r")
    for k in nomi:
        name = k[:len(k) - 1]  # elimino il carattere \n alla fine della mia parola
        gram = Ngrams.option[2](name)
        for i in gram:
            filename = 'file-' + i + '.txt'
            f = open(filename, "a")
            f.write(name + "\n")


def filetrigram():
    alphabet = __import__("string").lowercase
    for letter1 in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                nomefile = 'file-' + letter1 + letter2 + letter3 + '.txt'
                open(nomefile, "w")
    nomi = open("nomi.txt", "r")
    for k in nomi:
        name = k[:len(k) - 1]
        gram = Ngrams.option[3](name)
        for i in gram:
            filename = 'file-' + i + '.txt'
            f = open(filename, "a")
            f.write(name + "\n")


def testedit():
    query = raw_input("Inserire nome da cercare ")
    nomi = open("nomi.txt", "r")
    val = []
    query += "\n"
    for i in nomi:
        m = editDistance(query, i)
        if m <= 1:
            val.append(i)
    print "Forse cercavi:",
    for i in val:
        nomi = i[:len(i) - 1]
        print nomi,
    print ""


def testngram():
    query = raw_input("Inserire nome da cercare:")
    n = raw_input("Inserire n per gli n-gram:")
    if int(n) == 2:
        ngram = "bi"
    if int(n) == 3:
        ngram = "tri"
    lunghezzaedit = raw_input("Inserire valore di riferimento Edit_Distance:")
    word = []
    ngramQuery = Ngrams.option[int(n)](query)  # contiene gli ngrammi della query
    for i in range(1, len(ngramQuery)):
        nomefl = 'C:\\Users\\Michele\\PycharmProjects\\Es6\\' + ngram + 'grammi\\file-' + ngramQuery[i] + '.txt'
        l = open(nomefl, "r")
        query += "\n"
        for k in l:
            edit = editDistance(query, k)
            if edit <= int(lunghezzaedit):
                word.append(k)
    word = list(set(word))  # elimino le ripetizioni
    c = open("word.txt", "a")
    for k in word:
        c.write(k)
    word = list(set(word))
    print "Forse cercavi:",
    for i in word:
        nomi = i[:len(i) - 1]
        print nomi,


testngram()
'''
query = raw_input("Inserire nome da cercare")
ngramQuery = Ngrams.option[int(2)](query)  # contiene gli ngrammi della query
for i in range(1, len(ngramQuery)):
    print ngramQuery[i]
'''
