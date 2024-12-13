# sqlalchemy-challenge

Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Analyze and Explore the Climate Data

Part 1: Precipitation Analysis

1.) Find the most recent date in the dataset.

2.) Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.) Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.) Sort the DataFrame values by "date".

6.) Plot the results by using the DataFrame plot method, as the following image shows:

7.) Use Pandas to print the summary statistics for the precipitation data.

# Part 1: Station Analysis

1.) Design a query to calculate the total number of stations in the dataset.

2.) Design a query to find the most-active stations (that is, the stations that have the most rows).

3.) Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4.) Design a query to get the previous 12 months of temperature observation (TOBS) data. 

# Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed

#*CODE BORROWED FROM PROFESSOR*

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
