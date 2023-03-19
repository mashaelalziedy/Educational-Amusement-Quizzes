from flask import Flask, redirect, render_template, request, url_for
import sqlite3 as sql
app = Flask(__name__)

conn = sql.connect("results.db")
cursor = conn.cursor()

# Home Page
@app.route("/", methods=["GET"])
def home():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    sections = cursor.execute("SELECT * FROM sections")
    return render_template("index.html", sections = sections)

# Islamic Questions
@app.route("/islam.html", methods=["GET"])
def islam():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'islamics'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("islam.html", data=data)


# Islamic History Questions
@app.route("/islamhistory.html", methods=["GET"])
def islamhistory():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'islamic_history'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("islamhistory.html", data=data)


# War History Questions
@app.route("/war.html", methods=["GET"])
def war():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'war'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("war.html", data=data)


# Geography History Questions
@app.route("/geo.html", methods=["GET"])
def geo():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'geography'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("geo.html", data=data)


# Animals Questions
@app.route("/animal.html", methods=["GET"])
def animal():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'animals'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("animal.html", data=data)


# Oceans and Sea Questions
@app.route("/ocean.html", methods=["GET"])
def ocean():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'oceans'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("ocean.html", data=data)


# Operating Systems Questions
@app.route("/os.html", methods=["GET"])
def os():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'os'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("os.html", data=data)


# Programming Languages Questions
@app.route("/programming.html", methods=["GET"])
def programming():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'programming'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("programming.html", data=data)


# Saudi Arabia Questions
@app.route("/saudi.html", methods=["GET"])
def saudi():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'saudi'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("saudi.html", data=data)


# Soccer Questions
@app.route("/soccer.html", methods=["GET"])
def soccer():
    conn = sql.connect("results.db")
    cursor = conn.cursor()
    section = 'soccer'
    cursor.execute("UPDATE sections SET visitors=visitors+1 WHERE section = ?", [section])
    conn.commit()
    cursor.execute( "SELECT * FROM questions WHERE section = ?", [section])
    data=cursor.fetchall()
    return render_template("soccer.html", data=data)

    
@app.route("/score.html", methods=['GET','POST'])
def score():
    if request.method == 'POST':
        try:
            return redirect(url_for("home"))
        except Exception as e:
            print(e)
    else:
        return render_template("score.html")
    


if __name__ == "__main__":
    app.run(debug=True)
