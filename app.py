from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nazev_webu =  "Denisovo Portfolio"
    popis = "Ukázka projektů, výuka s AI, a testování Jitsi2"
    technologie =  ["Flask", "Python", "HTML", "CSS", "Jitsi2", "Copilot"]

    return render_template('index.htm', nazev_webu = nazev_webu)

if __name__ == '__main__':
    app.run(debug=True)
