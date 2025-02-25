from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Liste des défis
defis = ["Se lever pour admirer le lever du soleil", "Cuisiner un gâteau", "Faire un selfie avec un prof"]

@app.route("/")
def index():
    return render_template("indexroulette.html")  # Affiche la page HTML

@app.route("/get_defi", methods=["GET"])
def get_defi():
    """Renvoie un défi aléatoire au client"""
    if not defis:
        return jsonify({"defi": "Plus de défis disponibles !"})
    
    result = random.randint(0, len(defis) - 1)
    choix = defis.pop(result)  # Supprime et retourne l'élément
    return jsonify({"defi": choix})

if __name__ == "__main__":
    app.run(debug=True)  # Démarre le serveur Flask

# cd chemin/vers/ton/projet  # Aller dans le dossier du projet
# git status                 # Vérifier les changements
# git add .                  # Ajouter tous les fichiers
# git commit -m "Description des modifications"
# git push origin main       # Envoyer sur GitHub
