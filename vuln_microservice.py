from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# ❌ Hardcoded API key
API_KEY = "12345-SECRET-KEY"

# ❌ Insecure database connection (no auth)
def get_db():
    return sqlite3.connect("test.db")

# ❌ SQL Injection vulnerability
@app.route("/user")
def get_user():
    name = request.args.get("name")
    query = f"SELECT * FROM users WHERE name = '{name}'"
    conn = get_db()
    cursor = conn.execute(query)
    return str(cursor.fetchall())

# ❌ Weak password hashing
@app.route("/hash")
def hash_pwd():
    pwd = request.args.get("pwd")
    return hashlib.md5(pwd.encode()).hexdigest()

@app.route("/")
def home():
    return "Vulnerable Microservice Demo"

if __name__ == "__main__":
    app.run(debug=True)
