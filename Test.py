# coding=utf-8
from Distance import editDistance
from Ngram import Ngrams
from timeit import default_timer as timer

'''creazione di file per bigrammi e trigrammi e aggiunta dei nomi del lessico
ai rispettivi file, queste funzioni vengono eseguite 1 sola volta. Il tempo 
impiegato per il completamento di tale operazione è elevato a causa dell'elevate
operazioni di I/O con la memoria'''


def filebigram():
    alphabet = __import__("string").lowercase  # funzione che mi restituisce l'alfabeto minuscolo
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
    query = raw_input("Inserire nome da cercare: ")
    lunghezzaedit = raw_input("Inserire valore di riferimento Edit_Distance: ")
    nomi = open("nomi.txt", "r")
    val = []
    query += "\n"
    start = timer()
    for i in nomi:
        edit = editDistance(query, i)
        if edit <= int(lunghezzaedit):
            val.append(i)
    end = timer()
    print "Forse cercavi:",
    for i in val:
        nomi = i[:len(i) - 1]
        print nomi,
    print " "
    print "\nTempo Edit_Distance:", end - start
    print " "


def testngram():
    query = raw_input("Inserire nome da cercare: ")
    n = raw_input("Inserire n per gli n-gram: ")
    if int(n) == 2:
        ngram = "bi"
    if int(n) == 3:
        ngram = "tri"
    lunghezzaedit = raw_input("Inserire valore di riferimento Edit_Distance: ")
    word = []
    start = timer()
    ngramQuery = Ngrams.option[int(n)](query)  # contiene gli ngrammi della query
    for i in range(0, len(ngramQuery)):
        nomefl = 'C:\\Users\\Michele\\PycharmProjects\\Es6\\' + ngram + 'grammi\\file-' + ngramQuery[i] + '.txt'
        openfile = open(nomefl, "r")
        query += "\n"
        for k in openfile:
            edit = editDistance(query, k)
            if edit <= int(lunghezzaedit):
                word.append(k)
    end = timer()
    word = list(set(word))  # elimino le ripetizioni
    c = open("word.txt", "a")
    for k in word:
        c.write(k)
    word = list(set(word))  # elimino le ripetizioni
    print "Forse cercavi:",
    for i in word:
        nomi = i[:len(i) - 1]
        print nomi,
    print " "
    print "\nTempo con NGrams:", end - start


testedit()
testngram()
