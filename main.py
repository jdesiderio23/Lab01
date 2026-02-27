class Domanda:
    def __init__(self,testo,difficoltà,risposta_corretta, risposte):
        self.difficoltà = difficoltà
        self.testo = testo
        self.risposta_corretta = risposta_corretta
        self.risposte = risposte


with open("domande.txt") as f:
    difficoltà = f.readline(1)
    print(difficoltà)