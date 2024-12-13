# sqlalchemy-challenge

Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Part 1: Analyze and Explore the Climate Data

Precipitation Analysis
Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

Load the query results into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method, as the following image shows:

Use Pandas to print the summary statistics for the precipitation data.

# Station Analysis

Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

List the stations and observation counts in descending order.

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
