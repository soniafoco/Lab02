from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        righe = "-"*25
        print(righe+"\nTranslator Alien-Italian\n"+righe+"\n1. Aggiungi nuova parola\n"+
              "2. Cerca una traduzione\n"+"3. Cerca con wildcard\n"+"4. Stampa tutto il dizionario\n"+"5. Exit\n"+righe)

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        file = open(dict, "r", encoding="utf-8")
        riga = file.readline()
        while riga != "":
            campi = riga.strip().split(" ")
            self.dizionario.add(campi[0], campi[1])
            riga = file.readline()
        file.close()
        return self.dizionario

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dizionario.addWord(entry)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        translation = self.dizionario.translate(query)
        if translation==None:
            print("Non trovata")
        else:
            print(translation)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        translation = self.dizionario.translateWordWildCard(query)
        if translation==None:
            print("Non trovata")
        else:
            print(translation)

    def handlePrintAll(self):
        self.dizionario.printAll()