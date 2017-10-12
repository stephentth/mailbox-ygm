import random

from flask import Flask, render_template, request, Response

import mailman
import captcha_checker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inbox", methods=["POST"])
def inbox():
    form = request.form.to_dict()
    name = form.get("name", "Anonymous")
    email = form.get("email", "anonymous@domain.tld")
    subject = form.get("subject", "[no subject]")
    body = form.get("body", "")
    recaptcha_response = form.get("g-recaptcha-response", "")

    if captcha_checker.checker(recaptcha_response):
        result = mailman.send_message(name, email, subject, body)
    else:
        return render_template("error.html", message="Captcha wrong")

    status_code = result[0]
    status_text = result[1]
    if status_code == 200:
        return render_template("done.html")
    else:
        return render_template("error.html", message=status_text)

@app.route("/robots.txt")
def robots():
    only_root = "User-agent: * \nAllow: /$ \nDisallow: /"
    return Response(only_root, mimetype='text/plain')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
