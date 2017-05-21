def bigram():  # IMPORTANTE: necessita di uno spazio alla fine della lista dei nomi.
    l = open("C:\\Users\\Michele\\Desktop\\nomi.txt", "r")
    linelist = l.readlines()
    bigramlist = []
    for j in range(len(linelist)):
        for i in range(len(linelist[j]) - 2):
            bigramlist.append(linelist[j][i] + linelist[j][i + 1] + "\n")
            if i == len(linelist):
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
