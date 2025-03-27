print("vous avez {age} ans".format(age = 2025 - int(input("entrez votre année de naissance: >>>"))))


class Voiture:
  def __init__(self, nb_pneu, marque, model, couleur):
    self.nb_pneu = nb_pneu
    self.marque = marque
    self.model = model
    self.couleur = couleur

  def demarrer(self):
    print(f"la voiture de marque {self.marque}, de model {self.model} et de couleur {self.couleur} a demarrer")



ma_voiture = Voiture(8, "Pkandji", "Djetran", "noire")
ma_voiture.demarrer()
