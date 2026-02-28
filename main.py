import random
class Domanda:
    def __init__(self,testo,difficoltà,risposta_corretta,risposte):
        self.difficoltà = difficoltà
        self.testo = testo
        self.risposta_corretta = risposta_corretta
        self.risposte = risposte


with open("domande.txt", encoding="utf-8") as f:
    righe = f.read().splitlines()
    testi = righe[0::7]
    difficoltà = righe[1::7]
    risposta_corretta = righe[2::7]
    risposte=[]
    for i in range(0,int(len(righe)/7)+1):
        risposte.append(righe[2+i*7:6+i*7])
    domande_stampate = 0
    diff = 0
    k = 0
    while domande_stampate <= len(righe)/7 and k<=100000:
        domanda_n = random.randint(0,int(len(righe)/7))
        domande = Domanda(testi[domanda_n],difficoltà[domanda_n],risposta_corretta[domanda_n],risposte[domanda_n])
        testo_random = random.choice(testi)
        base = []
        if int(domande.difficoltà) == diff:
              base.append(domande.testo)
              print(random.choice(base))
              domande_stampate += 1
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
