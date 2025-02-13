from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def index():
    return render_template('index_tourisme.html')

# Page du formulaire d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        # Traitement du formulaire (ex : enregistrement des données dans une base)
        nom = request.form['nom']
        email = request.form['email']
        # Sauvegarder ou envoyer ces informations par email ou autre
        return redirect(url_for('index'))  # Redirige vers la page d'accueil après inscription
    return render_template('formulaire_inscription_tourisme.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Récupère le port défini par Render
    app.run(host='0.0.0.0', port=port)
