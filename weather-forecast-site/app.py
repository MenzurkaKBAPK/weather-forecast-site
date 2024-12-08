import os
import sys

from flask import (
    Flask,
    render_template,
    request
)

sys.path.append(os.getcwd())
from config import DEBUG
from methods import get_weather


app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        from_ = request.form.get("from")
        to_ = request.form.get("to")

        from_ = get_weather(from_, get_cached=DEBUG)
        to_ = get_weather(to_, get_cached=DEBUG)

        return render_template(
            "weather.html",
            from_=from_["name"],
            to_=to_["name"],
            weather_from=from_["data"],
            weather_to=to_["data"],
            good_from=from_["good"],
            good_to=to_["good"],
            errors_from=from_["errors"],
            errors_to=to_["errors"],
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", debug=DEBUG)
