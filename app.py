from flask import Flask, render_template
from data import users, nazev_webu, popis, technologie, titulek_webu
from generator import generuj_cisla

app = Flask(__name__)

@app.route('/')
def index():


    return render_template('index.htm', nazev_webu = nazev_webu, titulek_webu = titulek_webu, technologie = technologie)



@app.route('/contacts')
def contacts():
    return render_template("contacts.html", users = users)
    
if __name__ == '__main__':
    app.run(debug=True)


import random
from typing import Callable

def generator() -> int:

    return random.randint(1, 25)

if __name__ == "__main__":

        @app.route('/generator')
        def generator():
            gen = generuj_cisla ()
            cislo = list(gen)
            return render_template("base.htm", cislo = cislo)

        if __name__ == '__main__':
            app.run(debug=True)