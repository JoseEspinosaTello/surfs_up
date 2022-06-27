import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchamy dependencies

import sqlalchemy

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, func

#import flask dependencies

from flask import Flask, jsonify


#create sqllite engine

engine=create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect the database into our classes

Base =automap_base()

Base.prepare(engine, reflect=True)

#save table references

Measurement =Base.classes.measurement
Station =Base.classes.station

#create session link

session=Session(engine)

#define Flask app

app =Flask(__name__)


#define the welcome route

@app.route("/")

# set up routing info for each of the other routes

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/> 
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

#percipitation analysis

# create route

@app.route("/api/v1.0/precipitation")

#create function

def precipitation():
    #First, we want to add the line of code that calculates the date one year ago
    #from the most recent date in the database.
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

   #query to get the date and precipitation for the previous year.
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   
   return jsonify(precip)

#stations route

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


#monthly temp route

@app.route("/api/v1.0/tobs")

#create function

def temp_monthly():
    #calculate the one year date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))

    #jsonify our temps list, and then return it.
    return jsonify(temps=temps)



# min, average, and max temp route

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#stats function that contains perameters

def stats(start=None, end=None):
    #create a query to select the minimum, average, and maximum temperatures from our SQLite database.
    #create a list called sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == '__main__':
    app.run()
