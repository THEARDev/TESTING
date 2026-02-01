from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

number = random.randint(1, 100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global number
    user_guess = int(request.json["guess"])

    if user_guess < number:
        return jsonify({"result": "Too low"})
    elif user_guess > number:
        return jsonify({"result": "Too high"})
    else:
        number = random.randint(1, 100)
        return jsonify({"result": "Correct! New number generated 🎉"})

if __name__ == "__main__":
    app.run()


