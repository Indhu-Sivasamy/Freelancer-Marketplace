from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        connection = sqlite3.connect("freelancer.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO users(name, email, password, role)
        VALUES (?, ?, ?, ?)
        """, (name, email, password, role))

        connection.commit()
        connection.close()

        return "<h2>User Registered Successfully!</h2>"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)