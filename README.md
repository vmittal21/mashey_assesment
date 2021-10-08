# Mashey Assesment
Asteroid Hunter :: v1.1.0

## Details of API used for this assessment:

### Asteroids - NeoWs

NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.

Data-set: All the data is from the NASA JPL Asteroid team (http://neo.jpl.nasa.gov/).

This API is maintained by SpaceRocks Team: David Greenfield, Arezu Sarvestani, Jason English and Peter Baunach.

Neo - Feed
Retrieve a list of Asteroids based on their closest approach date to Earth. GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY

Query Parameters
Parameter	Type	Default	Description
start_date	YYYY-MM-DD	none	Starting date for asteroid search
end_date	YYYY-MM-DD	7 days after start_date	Ending date for asteroid search
api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage

#### Example query
##### https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

Neo - Lookup
Lookup a specific Asteroid based on its NASA JPL small body (SPK-ID) ID GET https://api.nasa.gov/neo/rest/v1/neo/

Path Parameters
Parameter	Type	Default	Description
asteroid_id	int	none	Asteroid SPK-ID correlates to the NASA JPL small body
api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage

#### Example query
##### https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY

#### Neo - Browse
##### Browse the overall Asteroid data-set GET https://api.nasa.gov/neo/rest/v1/neo/browse/

#### Example query
##### https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# How to run the project and file details

1. main.py has all the functions and helper functions coded

2. test.py executes the main.py file

3. For everytime execution, run the following commands:
    python test.py
    (It will prompt for entering the year and month for generating data for month_closest_approaches)
    (Use YYYY and MM integer format for inputting the month and year details)

4. Raw JSON data is stored in following files:

    * api_data.json
    * asteroid_closest_approach.json
    * month_closest_approaches.json
    * nearest_misses.json

5. The above raw data files are JSONified using the free resource https://jsonformatter.curiousconcept.com/ 

6. JSONified files are stored for better readability:
    
    * api_data_jsonified.json
    * asteroid_closest_approach_jsonified.json
    * month_closest_approaches_jsonified.json
    * nearest_misses_jsonified.json

