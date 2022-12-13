from flask import Flask, render_template, request, redirect
from database import database as db
from database import schemas


def run_app(__name__):
    app = Flask(__name__, template_folder="flask_app/templates", static_folder="flask_app/static")

    @app.route('/race/<_id>')
    def open_race(_id):
        race_id = _id
        item = db.session.query(db.BikeRides).filter(
            db.BikeRides.uid == race_id
        ).one()

        ride_data = schemas.RidesSchema().dump(item)
        ride_data['id'] = race_id
        return render_template("index2.html", ride_data=ride_data)

    @app.route('/race/go/', methods=['post'])
    def save_race():
        data = request.form
        race_id = data['id']

        additional_ride_data = schemas.RidesSchema().load(data)
        item = db.session.query(db.BikeRides).filter(
            db.BikeRides.uid == race_id
        ).one()
        item.ride_datetime = additional_ride_data["ride_datetime"]
        item.description = additional_ride_data["description"]
        item.meet_point = additional_ride_data["meet_point"]
        item.ride_name = additional_ride_data["ride_name"]

        db.session.commit()

        return redirect('/')

    @app.route('/')
    def index():
        return 'Welcome'

    app.run(host="0.0.0.0", port=5000)
