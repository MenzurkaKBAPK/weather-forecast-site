from flask import (
    Flask
)

from api_requests.main import (
    get_location,
    get_weather_by_location
)
from config import DEBUG
from methods import check_weather


app: Flask = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return "Base page <3"


if __name__ == "__main__":
    app.run("0.0.0.0", debug=DEBUG)
