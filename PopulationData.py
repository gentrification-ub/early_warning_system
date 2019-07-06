'''
@author  Voltaire Vergara
The aim of this file is to reproduce the population data that is indicated in the document, Buffalo Turning the corner.
Once reproduced, all the data will be turned into csv files for visualization
'''
import json
import requests

api_key = '3fad1f7c603dfb341edd045495a58a7c0e77f15c' #My API key
parameters = {"key": api_key}
api_base_url = 'https://api.census.gov/data/2016/acs/acs5?' #API call link
response =requests.get(api_base_url, params = parameters)

parameters.update( {"get": "B02001_003E,NAME"} )

#ELICOTT NEIGHBORHOOD ACCORDING TO BUFFALO TURNING THE CORNER
parameters.update( {"for":"block group:1,2,4", "in": "state:36+county:029+tract:001402"} )

response = requests.get(api_base_url, params = parameters)


print( "Population of African American: \n" + response.content.decode("utf-8"))
print("Total of black: 1461")
parameters.update( {"get": "B02001_001E,NAME"} )
print( "Total Population: \n" + response.content.decode("utf-8"))
print("Total of population: 1644\n" + "Percent of black in these places: " +  str((1461/1644) * 100))
#["19798228","New York","36"],