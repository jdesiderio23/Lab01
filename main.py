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
    while k <= len(righe)/7:
          domande = Domanda(testi[k],difficoltà[k],risposta_corretta[k],risposte[k])
          testo_random = random.choice(testi)
          # while domande.difficoltà!=0:
          print(domande.testo)
          risposte_stampate = []
          while len(risposte_stampate) < 4:
              risposta_random = random.choice(domande.risposte)
              if risposta_random not in risposte_stampate:
                  print(risposta_random)
                  risposte_stampate.append(risposta_random)
          tentativo = input("Inserire una risposta alla domanda:")
          if tentativo == domande.risposta_corretta:
              print("Risposta corretta!")
          else:
              print("Risposta errata.")
              break
          k += 1
