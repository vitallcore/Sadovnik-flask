from flask import Flask, render_template
import random


app = Flask(__name__)

PHONE_NUMBERS = [
    "79006722106",
    "79876543210",
    "79111234567",
    "79223334455"
]


@app.route("/")
def homepage():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("index.html", phone_number=phone_number)


@app.route("/about")
def about_page():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("about.html", phone_number=phone_number)


@app.route("/services")
def services_page():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("services.html", phone_number=phone_number)


if __name__ == "__main__":
    app.run(debug=False)
