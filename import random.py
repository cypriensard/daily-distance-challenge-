import random

defis = ["Se lever pour admirer le lever du soleil", "Cuisiner un gâteau", "Faire un selfie avec un prof"]

def roulette():
    if not defis:  
        return "Plus de défis disponibles !"
    
    result = random.randint(0, len(defis) - 1)
    choix = defis[result]  
    del defis[result]  
    return choix  
