from flask import Flask, render_template, request
from data import users, nazev_webu, popis, technologie, titulek_webu
from generator import generator 

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    email = None

    if request.method == "POST":
        email = request.args.get("email")

    return render_template('index.htm',nazev_webu=nazev_webu,titulek_webu=titulek_webu,technologie=technologie,email=email)

@app.route('/contacts')
def contacts():
    return render_template("contacts.html", users=users)

@app.route('/generator')
def generator_page():
    cislo = generator()  
    return render_template("base.htm", cislo=cislo)

if __name__ == '__main__':
    app.run(debug=True)
