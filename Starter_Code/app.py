# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an SQLite database engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

# Landing Page - Display available routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date (provide start date in the format YYYY-MM-DD)<br/>"
        f"/api/v1.0/start_date/end_date (provide start and end dates in the format YYYY-MM-DD)"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query precipitation data for the last year
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).all()

    # Convert the results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station, Station.name).all()

    # Convert the results to a list of dictionaries
    station_data = [{"Station ID": station, "Station Name": name} for station, name in results]

    return jsonify(station_data)

# Temperature Observations (tobs) route
@app.route("/api/v1.0/tobs")
def tobs():
    # Query temperature data for the most active station (USC00519281) for the last year
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).all()

    # Convert the results to a dictionary
    tobs_data = {date: tobs for date, tobs in results}

    return jsonify(tobs_data)

# Start Date route
@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    # Query min, max, and average temperatures from the given start date to the end of the dataset
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    # Convert the results to a dictionary
    temperature_stats = {
        "Min Temperature": results[0][0],
        "Max Temperature": results[0][1],
        "Average Temperature": results[0][2]
    }

    return jsonify(temperature_stats)

# Start Date and End Date route
@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date, end_date):
    # Query min, max, and average temperatures from the given start date to the given end date
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()

    # Convert the results to a dictionary
    temperature_stats = {
        "Min Temperature": results[0][0],
        "Max Temperature": results[0][1],
        "Average Temperature": results[0][2]
    }

    return jsonify(temperature_stats)

if __name__ == "__main__":
    app.run(debug=True)
