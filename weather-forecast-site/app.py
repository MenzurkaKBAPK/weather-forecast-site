from flask import (
    Flask
)


app: Flask = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return "Base page <3"


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
