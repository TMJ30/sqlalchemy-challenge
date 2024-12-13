# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from datetime import datetime, date
import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

session = Session(engine) #Create session from python to sql

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


# #################################################
# # Flask Routes
# #################################################

@app.route("/") #landing page
def homepage():
    print("LOADING HOMEPAGE . . .")
    return ("Welcome to the main page! <br/>"
            "Available Routes: <br/>"
            "/api/v1.0/precipitation <br/>"
            "/api/v1.0/stations <br/>"
            "/api/v1.0/tobs <br/>"
            "/api/v1.0/start <br/>"
            "/api/v1.0/start/end <br/>"

    )

@app.route("/api/v1.0/precipitation") #Return a JSON list of precipitation and dates from the dataset.
def precipitation():


    #find the date and recorded percipitation from last year to most recent year
    date_precp = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').filter(measurement.date <= '2017-08-23').\
        order_by(measurement.date).all()
    
    session.close()

    #create dictionary for Date: & Percipitation: . . .then add it to list to list it out in on it's page
    date_precp_list = []
    for date, prcp in date_precp:
        date_precp_dict = {} 
        date_precp_dict['Date'] = date #in dict, create Date column then pull date information
        date_precp_dict['Prcp'] = prcp #in dict, create Prcp column then pull prcp information
        date_precp_list.append(date_precp_dict)

    print("LOADING PERCIPITATION . . .")
    return jsonify(date_precp_list)


@app.route("/api/v1.0/stations") #Return a JSON list of stations from the dataset.
def stations():

    station_list = session.query(station.station).all()
    session.close()

    all_stations = list(np.ravel(station_list)) #turn truple into regular list

    print("LOADING STATIONS . . .")
    return jsonify(all_stations)
    

@app.route("/api/v1.0/tobs") #Return a JSON list of temperatures and date of observations for the previous year from most active station.
def tobs():

    most_active_tobs = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= '2016-08-23').filter(measurement.date <= '2016-12-31').\
        order_by(measurement.date).all()
    session.close()

    #create dictionary to put into list
    active_tobs_list = []
    for date, tobs in most_active_tobs:
        active_tobs_dict = {}
        active_tobs_dict['Date'] = date
        active_tobs_dict['Tobs'] = tobs
        active_tobs_list.append(active_tobs_dict)

    print("LOADING TEMPERATURES . . .")
    return(active_tobs_list)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""

    # Select statement
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    if not end:

        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).\
            filter(measurement.date >= start).all()

        session.close()

        temps = list(np.ravel(results))
        print(f"Start Date: {start}, End Date: {end}")
        return jsonify(temps)

    # calculate TMIN, TAVG, TMAX with start and stop
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")

    results = session.query(*sel).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    print(f"Start Date: {start}, End Date: {end}")
    return jsonify(temps=temps)



if __name__ == "__main__":
    app.run(debug=True)