import logging.config

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # put your live url here
    request_url = "https://function-app-demo-nayanexx.azurewebsites.net/api/"

    response = requests.get(request_url + "getNotes")
    notes = response.json()
    return render_template("index.html", notes=notes)


def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
