

class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def add(self, key, value):
        self.dizionario[key] = value

    def addWord(self, entry):
        print(entry)
        if entry[0] not in self.dizionario.keys():
            self.dizionario[entry[0]] = entry[1:len(entry)]
        else:
            self.dizionario[entry[0]].append(entry[1:len(entry)])
        print("Aggiunta!")

    def translate(self, word):
        if word in self.dizionario.keys():
            return self.dizionario[word]
        else:
            return None

    def translateWordWildCard(self, word):
        translations = []
        for key in self.dizionario.keys():
            if len(key)==len(word):
                found = True
                for i in range(len(key)):
                    if word[i]!="?" and key[i]!=word[i]:
                        found = False
                if found == True:
                    translations.append(self.dizionario[key])
        return translations


    def printAll(self):
        for word in self.dizionario:
            print(word, self.dizionario[word])