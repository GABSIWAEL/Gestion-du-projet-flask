from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ventes_mensuelles = []
depenses_mensuelles = []
commandes = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'montant_vente' in request.form:
            montant_vente = float(request.form['montant_vente'])
            ventes_mensuelles.append(montant_vente)
        elif 'montant_depense' in request.form:
            montant_depense = float(request.form['montant_depense'])
            depenses_mensuelles.append(montant_depense)
        elif 'date_commande' in request.form and 'montant_commande' in request.form:
            date_commande = request.form['date_commande']
            montant_commande = float(request.form['montant_commande'])

            # Additional fields for command
            prenom = request.form.get('prenom')
            nom = request.form.get('nom')
            telephone = request.form.get('telephone')
            adresse = request.form.get('adresse')
            transporteur = request.form.get('transporteur') == 'true'
            payee = 'payee' in request.form

            commandes.append({
                "date": date_commande,
                "montant": montant_commande,
                "prenom": prenom,
                "nom": nom,
                "telephone": telephone,
                "adresse": adresse,
                "transporteur": transporteur,
                "payee": payee
            })

    return render_template('index.html', ventes=ventes_mensuelles, depenses=depenses_mensuelles, commandes=commandes)


@app.route('/ajouter_vente', methods=['POST'])
def ajouter_vente():
    if request.method == 'POST':
        montant_vente = float(request.form['montant_vente'])
        ventes_mensuelles.append(montant_vente)
    return redirect(url_for('index'))


@app.route('/ajouter_depense', methods=['POST'])
def ajouter_depense():
    if request.method == 'POST':
        montant_depense = float(request.form['montant_depense'])
        depenses_mensuelles.append(montant_depense)
    return redirect(url_for('index'))


@app.route('/ajouter_commande', methods=['POST'])
def ajouter_commande():
    if request.method == 'POST':
        date_commande = request.form['date_commande']
        montant_commande = float(request.form['montant_commande'])

        # Additional fields for command
        prenom = request.form.get('prenom')
        nom = request.form.get('nom')
        telephone = request.form.get('telephone')
        adresse = request.form.get('adresse')
        transporteur = request.form.get('transporteur') == 'true'
        payee = 'payee' in request.form

        commandes.append({
            "date": date_commande,
            "montant": montant_commande,
            "prenom": prenom,
            "nom": nom,
            "telephone": telephone,
            "adresse": adresse,
            "transporteur": transporteur,
            "payee": payee
        })

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
