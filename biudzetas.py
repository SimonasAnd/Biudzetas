from pajamuirasas import PajamuIrasas
from islaiduirasas import IslaiduIrasas
import pickle
from email.message import EmailMessage
from slaptazodis import password
import smtplib

class Biudzetas:
    try:
        with open('ataskaita.pkl', 'rb') as pkl_file:
            ataskaita = pickle.load(pkl_file)
            id_nr = ataskaita[-1].id+1
    except:
        ataskaita = []
        id_nr = 0


    def ivesti_pajamas(self, suma, kategorija, siuntejas, pap_info):
        paj_irasas = PajamuIrasas(self.id_nr, suma, kategorija, siuntejas, pap_info)
        self.ataskaita.append(paj_irasas)
        self.id_nr += 1
        with open('ataskaita.pkl', 'wb') as pkl_file:
            pickle.dump(self.ataskaita, pkl_file)

    def ivesti_islaidas(self, suma, kategorija, atsiskaitymo_budas, isigyta_preke_paslauga):
        isl_irasas = IslaiduIrasas(self.id_nr, suma, kategorija, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.ataskaita.append(isl_irasas)
        self.id_nr += 1
        with open('ataskaita.pkl', 'wb') as pkl_file:
            pickle.dump(self.ataskaita, pkl_file)

    def gauti_balansa(self):
        suma = 0
        for atask in self.ataskaita:
            if isinstance(atask, PajamuIrasas):
                suma += atask.suma
            elif isinstance(atask, IslaiduIrasas):
                suma -= atask.suma
        return suma

    def gauti_ataskaita(self):
        for atask in self.ataskaita:
            if isinstance(atask, PajamuIrasas):
                print(f'ID: {atask.id}, Data: {atask.data}, Tipas: {atask.tipas}, Suma: {atask.suma}, Kategorija: {atask.kategorija}, Siuntejas: {atask.siuntejas}, Papildoma info: {atask.pap_info}')
            else:
                print(f'ID: {atask.id}, Data: {atask.data}, Tipas: {atask.tipas}, Suma: {atask.suma}, Kategorija: {atask.kategorija}, Atsiskaitymo budas: {atask.atsiskaitymo_budas}, Isigyta preke/paslauga: {atask.isigyta_preke_paslauga}')

    def trinti_irasa(self, idnr):
        nerastas = True

        for atask in self.ataskaita:
            if idnr == atask.id:
                del self.ataskaita[self.ataskaita.index(atask)]
                nerastas = False
                print(f"Irasasas {idnr} [ID], sekmingai panaikintas")
                input('Paspauskite ENTER')
                with open('ataskaita.pkl', 'wb') as pkl_file:
                    pickle.dump(self.ataskaita, pkl_file)

        if nerastas:
            print("Tokio ID nera")
            input('Paspauskite ENTER')

    def trinti_viska(self):
        self.ataskaita.clear()
        self.id_nr = 0
        with open('ataskaita.pkl', 'wb') as pkl_file:
            pickle.dump(self.ataskaita, pkl_file)

    def siusti_email(self):
        email = EmailMessage()
        email['from'] = "Simon"
        email['to'] = 'quezzspam@gmail.com'
        email['subject'] = 'Balansas maziau uz 0'
        email.set_content(f'Jusu balansas pasieke {self.gauti_balansa()}')

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('quezzspam@gmail.com', password)
            smtp.send_message(email)
