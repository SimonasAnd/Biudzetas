from flask import Flask, render_template, request, redirect
from biudzetas import Biudzetas

app = Flask(__name__)

klase = Biudzetas()

@app.route('/')
@app.route('/index.html')
def main():
    return render_template('index.html', veiksmas = "nera")

@app.route('/balansas')
@app.route('/index.html/balansas')
def balansas():
    return render_template('index.html', veiksmas = "balansas", balansas=klase.gauti_balansa())

@app.route('/prideti.html', methods=['GET', 'POST'])
def prideti():
    if request.method == "POST":
        post_suma = int(request.form['suma'])
        post_kategorija = request.form['kategorija']
        post_siuntejas = request.form['siuntejas']
        post_papinfo = request.form['papinfo']
        if post_kategorija == "atlyginimas":
            post_kategorija = "Atlyginimas"
        elif post_kategorija == "kitas_uz":
            post_kategorija = "Kitas užmokestis"
        elif post_kategorija == "skola":
            post_kategorija = "Skola"
        elif post_kategorija == "kita":
            post_kategorija = "Kita"

        klase.ivesti_pajamas(post_suma, post_kategorija, post_siuntejas, post_papinfo)
        return render_template('prideti.html', veiksmas = "po")
    else:
        return render_template('prideti.html', veiksmas = "pradzia")

@app.route('/isimti.html', methods=['GET', 'POST'])
def isimti():
    if request.method == "POST":
        post_suma = int(request.form['suma'])
        post_kategorija = request.form['kategorija']
        post_budas = request.form['budas']
        post_isigyta = request.form['isigyta']

        if post_kategorija == "pirkiniai":
            post_kategorija = "Pirkiniai"
        elif post_kategorija == "pavedimas":
            post_kategorija = "Banko pavedimas"
        elif post_kategorija == "kita":
            post_kategorija = "Kita"

        if post_budas == "kortele":
            post_budas = "Banko kortele"
        elif post_budas == "gryni":
            post_budas = "Grynais"

        klase.ivesti_islaidas(post_suma, post_kategorija, post_budas, post_isigyta)
        return render_template('isimti.html', veiksmas = "po")
    else:
        return render_template('isimti.html', veiksmas = "pradzia")

@app.route('/ataskaita.html')
def ataskaita():
    return render_template('ataskaita.html', ataskaita=klase.gauti_ataskaitahtml())

@app.route('/ataskaita.html/trinti/')
def ataskaita_trinti_viena():
    idd = request.args.get('idd', default='', type=int)
    if idd == 999:
        klase.trinti_viska()
    else:
        klase.trinti_irasa(idd)
    return redirect("/ataskaita.html")

if __name__ == "__main__":
    app.run(debug=True)