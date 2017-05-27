'''
def bigram():  # IMPORTANTE: necessita di uno spazio alla fine della lista dei nomi.
    l = open("C:\\Users\\Michele\\Desktop\\nomi.txt", "r")
    linelist = l.readlines()
    bigramlist = []
    for j in range(len(linelist)):
        for i in range(len(linelist[j]) - 2):  # sottrazione dovuta alla lunghezza falsata dal "\n"
            bigramlist.append(linelist[j][i] + linelist[j][i + 1] + "\n")
            if i == len(linelist):  # per copiare ultimo elemento eliminando "\n"
                bigramlist.append(linelist[j][i + 1] + linelist[j][i + 2] + "\n")
    l.close()
    l = open("C:\\Users\\Michele\\Desktop\\bigram.txt", "w")
    for i in range(len(bigramlist)):
        l.write(bigramlist[i])
    return bigramlist


def trigram():  # IMPORTANTE: necessita di uno spazio alla fine della lista dei nomi.
    l = open("C:\\Users\\Michele\\Desktop\\nomi.txt", "r")
    linelist = l.readlines()
    trigramlist = []
    for j in range(len(linelist)):
        for i in range(len(linelist[j]) - 2):
            if i == (len(linelist[j]) - 3):
                break
            trigramlist.append(linelist[j][i] + linelist[j][i + 1] + linelist[j][i + 2] + "\n")
    l.close()
    l = open("C:\\Users\\Michele\\Desktop\\trigram.txt", "w")
    for i in range(len(trigramlist)):
        l.write(trigramlist[i])
    return trigramlist
'''


class Ngrams:
    def onegram(parola):
        gram = []
        for i in range(len(parola)):
            gram.append(parola[i])
        return gram

    def bigram(parola):
        gram = []
        for i in range(len(parola) - 1):
            gram.append(parola[i] + parola[i + 1])
        return gram

    def trigram(parola):
        gram = []
        for i in range(len(parola) - 2):
            gram.append(parola[i] + parola[i + 1] + parola[i + 2])
        return gram

    option = {
        1: onegram,
        2: bigram,
        3: trigram,
    }


ngram = Ngrams()
print ngram.option[1]("margherita")
