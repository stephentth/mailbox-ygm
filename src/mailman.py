import os
import requests
import datetime

from jinja2 import Environment, FileSystemLoader

MAILGUN_API = os.getenv("mailgun_api", "")
MAILGUN_URL = os.getenv("mailgun_url", "")
MAILGUN_EMAIL_SANDBOX = os.getenv("mailgun_email_sandbox", "")
MAILGUN_NAME_SANDBOX = os.getenv("mailgun_name_sandbox=", "")
YOUR_NAME = os.getenv("your_name", "")
YOUR_EMAIL = os.getenv("your_email", "")

def email_format(name, email, subject, body):
    now = datetime.datetime.now().isoformat()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, "templates")
    env = Environment(
        loader=FileSystemLoader(template_path)
    )

    email_template = env.get_template("letter.html")
    letter = email_template.render(now=now, name=name, email=email, subject=subject, body=body)
    return letter

def send_message(name, email, subject, body):
    url = MAILGUN_URL
    body = email_format(name, email, subject, body)
    subject = "INBOX: {} - {}".format(name, subject)

    result = requests.post(
        url,
        auth=("api", MAILGUN_API),
        data={"from": "{} <{}>".format(MAILGUN_NAME_SANDBOX, MAILGUN_EMAIL_SANDBOX),
              "to": "{} <{}>".format(YOUR_NAME, YOUR_EMAIL),
              "subject": "{}".format(subject),
              "html": "{}".format(body)})
    return result.status_code, result.text

