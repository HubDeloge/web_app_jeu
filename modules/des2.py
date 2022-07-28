import random

class tirage_des:
  def tirage(self):
    le_tirage = random.randint(0,6)
    return le_tirage 

  def verification(self,choix_joueur,tirage):
    if choix_joueur == str(tirage):
      resultat='gagner'
    else:
      resultat='perdu'
    return resultat
    