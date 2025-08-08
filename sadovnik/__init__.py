from flask import Flask, render_template
import random

application = Flask(__name__)

PHONE_NUMBERS = [
    "79123456789",
    "79123456789",
    "79123456789",
    "79123456789"
]


@application.route("/")
def homepage():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("index.html", phone_number=phone_number)


@application.route("/about")
def about_page():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("about.html", phone_number=phone_number)


@application.route("/services")
def services_page():
    phone_number = random.choice(PHONE_NUMBERS)
    return render_template("services.html", phone_number=phone_number)
