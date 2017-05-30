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
