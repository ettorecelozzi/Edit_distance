from Distance import editDistance
from Ngram import Ngrams


def testedit():
    query = raw_input("Inserire nome da cercare ")
    nomi = open("C:\\Users\\Michele\\Desktop\\nomi.txt", "r")
    val = []
    query += "\n"
    for i in nomi:
        m = editDistance(query, i)
        if m <= 1:
            val.append(i)
    print val


def testngram():
    ngramQuery = []
    query = raw_input("Inserire nome da cercare")
    n = raw_input("Inserire n per gli n-gram")
    ngramQuery.append(Ngrams.option[n](query))  # contiene gli ngrammi della query
    nomi = open("C:\\Users\\Michele\\Desktop\\nomi.txt", "r")
    tmp = []
    for nome in nomi:
        tmp.append(Ngrams.option[n](nome))
