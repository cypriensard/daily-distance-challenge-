from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import random

IMAGE_FOLDER = 'static/assets/'
app = Flask(__name__)

# Liste des défis
defis = [
    "Se lever pour admirer le lever du soleil", 
    "Cuisiner un gâteau", 
    "prendre une photo avec un animal", 
    "tester un dessert",
    "se poser 30 mins au parc",
    "aller dans un café devant lequel on passe tous les jours",
    "rentrer dans une librairie ou bibliothèque",
    "dessiner un objet de notre environnement en 5 mins",
    "s'arrêter à une station de métro avant sa destination pour marcher",
    "manger une spécialité",
    "manger un street food",
    "ecrire une carte postale",
    "cuisiner un vrai ptit dej !",
    "méditer 5 mins",
    "ouvrir son livre", 
    "nettoye une partie de ta maison paumé",
    "change un élément de place de chez toi",
    "faire un max pompe",
    "faire un hand stand",
    "fais un voeux",
    "apprend une nouvelle passe de rock"
]

# Route d'index
@app.route("/")

def index():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    return render_template("indexroulette.html", images=images)
# Route pour obtenir un défi
@app.route("/get_defi", methods=["GET"])
def get_defi():
    """Renvoie un défi aléatoire au client"""
    if not defis:
        return jsonify({"defi": "Plus de défis disponibles !"})
    
    result = random.randint(0, len(defis) - 1)
    choix = defis.pop(result)  # Supprime et retourne l'élément
    return jsonify({"defi": choix})

@app.route("/upload", methods=["POST"])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # On vérifie que le fichier est bien une image et qu'il a une extension valide
        filename = file.filename
        file.save(os.path.join(IMAGE_FOLDER, filename))  # Sauvegarde l'image dans le dossier 'assets'
        
        return redirect(url_for('index'))  # Redirige vers la page d'accueil après l'upload


if __name__ == "__main__":
    app.run(debug=True)  # Démarre le serveur Flask
