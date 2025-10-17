from flask import Flask, render_template

app = Flask(__name__)

users = {
    1: {
        "jmeno": "Jan",
        "prijmeni": "Novák",
        "email": "jan.novak@example.com",
        "telefon": "+420123456789",
        "kancelar": "101A"
    },
    2: {
        "jmeno": "Petra",
        "prijmeni": "Svobodová",
        "email": "petra.svobodova@example.com",
        "telefon": "+420987654321",
        "kancelar": "102B"
    },
    3: {
        "jmeno": "Martin",
        "prijmeni": "Kapcala",
        "email": "martin.kapcala@example.com",
        "telefon": "+420456789123",
        "kancelar": "103C"
    },
    4: {
        "jmeno": "Lucie",
        "prijmeni": "Dvořáková",
        "email": "lucie.dvorakova@example.com",
        "telefon": "+420321654987",
        "kancelar": "104D"
    },
    5: {
        "jmeno": "Tomáš",
        "prijmeni": "Havlásek",
        "email": "tomas.havlasek@example.com",
        "telefon": "+420789123456",
        "kancelar": "105E"
    }
}

@app.route('/')
def index():
    nazev_webu =  "Denisovo Portfolio"
    titulek_webu= "Svět, který jsem si stvořil, je výsledkem našeho myšlení. Nelze jej měnit."
    popis = "Ukázka projektů, výuka s AI, a testování Jitsi2"
    technologie =  ["Flask", "Python", "HTML", "CSS", "Jitsi2", "Copilot"]

    return render_template('index.htm', nazev_webu = nazev_webu, titulek_webu = titulek_webu, technologie = technologie)



@app.route('/contacts')
def contacts():
    return render_template("contacts.html", users = users)
    
if __name__ == '__main__':
    app.run(debug=True)
