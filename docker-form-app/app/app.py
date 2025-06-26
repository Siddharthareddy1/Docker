from flask import Flask, request, redirect, render_template
import sqlite3
import os
from db import init_db

app = Flask(__name__)
DB_PATH = 'formdata.db'
init_db(DB_PATH)


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
        return redirect("/table")
    return render_template("form.html")

@app.route("/table")
def table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, age FROM users")
    data = cur.fetchall()
    conn.close()
    return render_template("table.html", users=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
