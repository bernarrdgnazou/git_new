print("bonjour vous avez {a} ans".format(a = 2025 - int(input("quel est votre année de naissance ? >>"))))


class Voiture:
    def __init__(self, nb_pneu, couleur, model, marque):
        sefl.marque = marque
	self.nb_pneu = nb_pneu
	slef.couleur = couleur
	slef.model = model


   def demarrer(self):
	print(f"la voiture de marque {self.marque} et de model {self.model} a démarrer")



ma_voiture = Voiture(4, "rouge", "Djetran", "Pkandji")
ma_voiture.demarrer()
