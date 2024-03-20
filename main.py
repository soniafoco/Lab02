import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()

    dict = t.loadDictionary("dictionary.txt")

    txtIn = input()

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txt = input()
        list = txt.lower().split(" ")
        while list[0].isalpha()==False or list[0].isalpha()==False:
            print("Inserire di nuovo la parola")
            txt = input()
            list = txt.lower().split(" ")
        t.handleAdd(list)


    elif int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txt = input()
        while txt.isalpha()==False:
            print("Inserire di nuovo la parola")
            txt = input()
        translation = t.handleTranslate(txt.lower())


    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txt = input()
        translation = t.handleWildCard(txt.lower())

    elif int(txtIn) == 4:
        #stampa
        t.handlePrintAll()

    elif int(txtIn) == 5:
        break
