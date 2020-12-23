from app import app
from flask import jsonify, request
from app.models import Divvy
from sqlalchemy.sql import func

@app.route('/')
def index():
    return "Hello World!"


@app.route('/average')
def average():
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    from_station_id = request.args.get('from_station_id')
    if from_station_id:
        average = Divvy.query.with_entities(func.avg(Divvy.trip_duration)).filter(Divvy.starttime >= starttime).filter(Divvy.stoptime <= endtime).filter(Divvy.from_station_id == from_station_id).one()
        return jsonify(averageDuration = float(average[0]), from_station_id=from_station_id, from_station=Divvy.query.filter_by(from_station_id=from_station_id).first().from_station_name)
    else:
        average = Divvy.query.with_entities(func.avg(Divvy.trip_duration)).filter(Divvy.starttime >= starttime).filter(Divvy.stoptime <= endtime).one()
        return jsonify(averageDuration = float(average[0]))