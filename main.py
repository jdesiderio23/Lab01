import random
class Domanda:
    def __init__(self,testo,difficoltà,risposta_corretta,risposte):
        self.difficoltà = difficoltà
        self.testo = testo
        self.risposta_corretta = risposta_corretta
        self.risposte = risposte


with open("domande.txt", encoding="utf-8") as f:
    righe = f.read().splitlines()
    testi = []
    difficoltà = []
    risposta_corretta = []
    risposte = []
    for riga in righe:
        if righe.index(riga) == 0 or righe.index(riga) % 7 == 0:
            testi.append(riga)
        if righe.index(riga) == 1 or righe.index(riga) % 7 == 1:
            difficoltà.append(riga)
        if righe.index(riga) == 2 or righe.index(riga) % 7 == 2:
            risposta_corretta.append(riga)
        if righe.index(riga) == 2 or righe.index(riga)%7==2 :
            risposte.append([riga,righe[righe.index(riga) + 1],righe[righe.index(riga) + 2],righe[righe.index(riga) + 3]])
    k = 0
    diff = 0
    print(risposta_corretta)
    while k <= len(righe)/7:
        domanda_n = random.randint(0,int(len(righe)/7)+2)
        domande = Domanda(testi[domanda_n],difficoltà[domanda_n],risposta_corretta[domanda_n],risposte[domanda_n])
        testo_random = random.choice(testi)
        base = []
        if domande.difficoltà == diff:
              base.append(domande.testo)
              print(random.choice(base))
              risposte_stampate = []
              while len(risposte_stampate) < 4:
                 risposta_random = random.choice(domande.risposte)
                 if risposta_random not in risposte_stampate:
                     print(risposta_random)
                     risposte_stampate.append(risposta_random)
                     tentativo = input("Inserire una risposta alla domanda:")
                     if tentativo == domande.risposta_corretta:
                        print("Risposta corretta!")
                        diff += 1
                     else:
                        print("Risposta errata.")
                        break
        else:
             k += 1
