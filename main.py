import json
import requests
import sys
import calendar
import datetime

class Mashey_Assessment:

    def __init__(self):
        
        # To use the api_data.json file in all functions of the class
        self.file = "api_data.json"
        self.data = None
        self.json_file = None
        self.id_list = None
        self.year = None
        self.month = None
        self.days = None

    #******************************************************************************

    def get_api_data_locally(self):

        #This is a helper function for asteroid_closest_approach function
        # This function gets the details from the API using API key and creates a json file named api_data.json to use it locally
        # Creates a request to the API to get data
        r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=90GarKwRkqcLpOMJnSLkbvOa9LghMB0xcMJw1CIU').json()
        
        # Creates a file where API data is written
        f = open(self.file, "w")
        
        # Adding data collected from data to the file
        json.dump(r, f)
        f.close()
    
    #******************************************************************************

    def get_total_days(self):

        # This function gets the total number of days in a month of a particular year
        temp = calendar.monthrange(self.year,self.month)
        self.days = temp[1]
        return(self.days)

    #******************************************************************************

    def open_file(self):

        # Opens the json file
        with open(self.file) as self.json_file:
            self.data = json.load(self.json_file)

    #******************************************************************************

    def close_file(self):

        # Closes the accessed file
        self.json_file.close()

    #******************************************************************************

    def asteroid_closest_approach(self):

        # Endpoint: 'https://api.nasa.gov/neo/rest/v1/neo/browse'
        
        # This function finds the smallest value of "epoch_date_close_approach" corresponding to each asteroid id
        # It then combines all these details together and returns a list of asteroids with the smallest/closest "epoch_date_close_approach" in json format 
        self.open_file()

        final_list = list()

        for i in range(0, len(self.data["near_earth_objects"])):

            # initializing the dictionary format for output
            output = {"links": None, "id": None, "neo_reference_id": None, "name": None, "name_limited": None, "designation": None, "nasa_jpl_url": None, "absolute_magnitude_h": None, "estimated_diameter": None, "is_potentially_hazardous_asteroid": None, "close_approach_data": None, "orbital_data": None, "is_sentry_object": None}

            output["links"] = self.data["near_earth_objects"][i]["links"]
            output["id"] = self.data["near_earth_objects"][i]["id"]
            output["neo_reference_id"] = self.data["near_earth_objects"][i]["neo_reference_id"]
            output["name"] = self.data["near_earth_objects"][i]["name"]
            output["name_limited"] = self.data["near_earth_objects"][i]["name_limited"]
            output["designation"] = self.data["near_earth_objects"][i]["designation"]
            output["nasa_jpl_url"] = self.data["near_earth_objects"][i]["nasa_jpl_url"]
            output["absolute_magnitude_h"] = self.data["near_earth_objects"][i]["absolute_magnitude_h"]
            output["estimated_diameter"] = self.data["near_earth_objects"][i]["estimated_diameter"]
            output["is_potentially_hazardous_asteroid"] = self.data["near_earth_objects"][i]["is_potentially_hazardous_asteroid"]

            # Sorting the "close_approach_data" based on value of "epoch_date_close_approach" in ascending order
            temp = self.data["near_earth_objects"][i]["close_approach_data"]

            newlist = sorted(temp, key=lambda k: k["epoch_date_close_approach"]) 

            # Using the first entry generated after sorting the list of dictionaries "close_approach_data"
            output["close_approach_data"] = newlist[0]

            output["orbital_data"] = self.data["near_earth_objects"][i]["orbital_data"]
            output["is_sentry_object"] = self.data["near_earth_objects"][i]["is_sentry_object"]

            final_list.append(output)

            with open('asteroid_closest_approach.json', 'w') as final_list_file:
                json.dump(final_list , final_list_file)
        
        self.close_file()
      
    #******************************************************************************

    def month_closest_approaches(self):
        """
        Endpoint: 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-01&end_date=2021-01-08'

        """

        # first week of the any calendar month
        _start_date="01"
        _end_date="08"

        # Takes the user input for month and year
        _year = input("Enter the year in YYYY format: ")
        _month = input("Enter the month in MM format: ")

        self.year = int(_year)
        self.month = int(_month)


        # We create a list of dictionaries which will be used for generating json file with all dates of the month and data for each date
        month_data = list()

        # initial request for first week
        req_data = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={self.year}-{self.month}-{_start_date}&end_date={self.year}-{self.month}-{_end_date}&api_key=90GarKwRkqcLpOMJnSLkbvOa9LghMB0xcMJw1CIU').json()
        # getting the initial data for first week
        month_data.append(req_data.get("near_earth_objects"))
        next_url = req_data.get("links")["next"]
        next_start_month = next_url[37:57].split("=")[1].split("-")[1]
        next_start_year = next_url[37:57].split("=")[1].split("-")[0]
        next_start_date = next_url[37:57].split("=")[1].split("-")[2]
        

        # request data for next weeks 
        while int(next_start_month) == self.month and int(next_start_year) == self.year:
            req_data = requests.get(next_url).json()
            month_data.append(req_data.get("near_earth_objects"))
            next_url = req_data.get("links")["next"]
            next_start_month = next_url[37:57].split("=")[1].split("-")[1]
            next_start_year = next_url[37:57].split("=")[1].split("-")[0]
            next_start_date = next_url[37:57].split("=")[1].split("-")[2]
            print(f'next year: {next_start_year} next month: {next_start_month} next_start_date: {next_start_date}')

        print("Data successfully captured for given month.")

        # remove duplicate days
        seen = set()
        final_output = list()

        element_count = 0

        for week in month_data:
            for day in week:
                if int(day.split("-")[1]) == self.month and int(day.split("-")[0]) == self.year:
                    if day not in seen:
                        seen.add(day)
                        element_count += len(week[day])
                        final_output.append({"day":day, "_value":week[day]})

        # sort by day
        final_output = sorted(final_output, key=lambda day:day["day"])

        response = {"element_count": element_count, "total_days": len(final_output), "payload":final_output}

        with open('month_closest_approaches.json', "w") as temp_file:
            json.dump(response, temp_file)

    #******************************************************************************

    def nearest_misses(self):

        # Endpoint: https://api.nasa.gov/neo/rest/v1/neo/browse
        pass

    #******************************************************************************

