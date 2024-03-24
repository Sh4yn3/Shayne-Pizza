from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('PIZZA.db.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizza WHERE id=?;", (id,))
    pizza = cur.fetchone()
    conn.close()
    return render_template("pizza.html", pizza=pizza)


if __name__ == '__main__':
    app.run(debug=True)
