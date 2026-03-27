# Honolulu Climate Analysis & API

## Overview
This project performs a comprehensive climate analysis of Honolulu, Hawaii using historical weather data store in a SQLite database. The analysis leverages SQLAlchemy ORM queries, Pandas, and Matplotlib to explore precipitation trends, station activity, and temperature patterns over time.

In addition to the exploratory analysis, a Flask-based API is develop to make the climate data accessible through RESTful endpoints. Users can query precipitation, station information, and temperature statistics for specific date ranges, enabling easy access to meaningful climate insights.

## Analysis Summary
**Precipitation**
* Retrieved last 12 months of precipitation data
* Organized results into a DataFrame and sorted by date
* Visualize trends and generated summary statistics

**Stations**
* Calculated total number of stations
* Identified the most active station (highest observations)

**Temperature**
* Computed min, avg, and max temperature for the most active station
* Retrieved last 12 months of temperature observations
* Visualized distribution with a histogram

## Flask API
Routes
* '/' -> List all routes
