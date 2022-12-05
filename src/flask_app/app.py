from flask import Flask, render_template
from database import database as db
from database import schemas


def run_app(__name__):
    app = Flask(__name__, template_folder="flask_app/templates", static_folder="flask_app/static")

    @app.route('/race/<string:id>')
    def index(id):
        race_id = id
        item = db.session.query(db.BikeRides).filter(
            db.BikeRides.uid == race_id
        ).one()

        ride_data = schemas.RidesSchema().dump(item)

        return render_template("index2.html", ride_data=ride_data)

    app.run(host="0.0.0.0", port=5000)
