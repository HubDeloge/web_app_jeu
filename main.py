from flask import Flask, render_template, request
from modules import des2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/jeux',methods=['GET', 'POST'])
def fonction_jeu():
  mon_tirage = des2.tirage_des().tirage()
  choix_joueur = request.form.get('le_pari')
  resultat = des2.tirage_des().verification(choix_joueur,mon_tirage)
  print(choix_joueur) 
  return render_template('page jeu.html', resu =resultat, tira = mon_tirage)

app.run(host='0.0.0.0', port=81)