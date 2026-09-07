from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), "nexyra.db")

def init_db():
    con=sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS registrations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_name TEXT NOT NULL,
        leader_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        college TEXT NOT NULL,
        theme TEXT NOT NULL,
        member2 TEXT NOT NULL,
        member3 TEXT,
        member4 TEXT,
        created_at TEXT NOT NULL
    )""")
    con.commit(); con.close()

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/register")
def register():
    data=request.get_json(silent=True) or {}
    required=["team_name","leader_name","email","phone","college","theme","member2"]
    if any(not str(data.get(k,"")).strip() for k in required):
        return jsonify(message="Please fill in all required fields."),400
    con=sqlite3.connect(DB)
    con.execute("""INSERT INTO registrations
      (team_name,leader_name,email,phone,college,theme,member2,member3,member4,created_at)
      VALUES (?,?,?,?,?,?,?,?,?,?)""",
      (data["team_name"],data["leader_name"],data["email"],data["phone"],data["college"],
       data["theme"],data["member2"],data.get("member3",""),data.get("member4",""),
       datetime.now().isoformat(timespec="seconds")))
    con.commit(); con.close()
    return jsonify(message="Registration submitted successfully!"),201

@app.get("/api/registrations")
def registrations():
    # Add authentication before deploying this admin endpoint publicly.
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    rows=[dict(r) for r in con.execute("SELECT * FROM registrations ORDER BY id DESC")]
    con.close()
    return jsonify(rows)

if __name__=="__main__":
    init_db()
    app.run(debug=True)
