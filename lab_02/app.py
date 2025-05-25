from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    result = ""
    if request.method == "POST":
        cipher = CaesarCipher()
        text = request.form.get("text")
        key = int(request.form.get("key"))
        if "encrypt" in request.form:
            result = cipher.encrypt_text(text, key)
        elif "decrypt" in request.form:
            result = cipher.decrypt_text(text, key)
    return render_template("caesar.html", result=result)

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = ""
    if request.method == "POST":
        cipher = VigenereCipher()
        text = request.form.get("text")
        key = request.form.get("key")
        if "encrypt" in request.form:
            result = cipher.vigenere_encrypt(text, key)
        elif "decrypt" in request.form:
            result = cipher.vigenere_decrypt(text, key)
    return render_template("vigenere.html", result=result)

@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    result = ""
    if request.method == "POST":
        cipher = RailFenceCipher()
        text = request.form.get("text")
        key = int(request.form.get("key"))
        if "encrypt" in request.form:
            result = cipher.rail_fence_encrypt(text, key)
        elif "decrypt" in request.form:
            result = cipher.rail_fence_decrypt(text, key)
    return render_template("railfence.html", result=result)

@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = ""
    if request.method == "POST":
        cipher = PlayFairCipher()
        text = request.form.get("text")
        key = request.form.get("key")
        matrix = cipher.create_playfair_matrix(key)
        if "encrypt" in request.form:
            result = cipher.playfair_encrypt(text, matrix)
        elif "decrypt" in request.form:
            result = cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html", result=result)

@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    result = ""
    if request.method == "POST":
        cipher = TranspositionCipher()
        text = request.form.get("text")
        key = int(request.form.get("key"))
        if "encrypt" in request.form:
            result = cipher.encrypt(text, key)
        elif "decrypt" in request.form:
            result = cipher.decrypt(text, key)
    return render_template("transposition.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)