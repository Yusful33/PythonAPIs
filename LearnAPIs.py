# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:16:17 2019

@author: ycattaneo
"""
import requests
#URL we are requesting to (in this case is about astronauts in space)
response = requests.get("http://api.open-notify.org/astros.json")
#Displaying the error code if any
print(response.status_code)

#Code Guide
#200: Everything went okay, and the result has been returned (if any).
#301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
#400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
#401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
#403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
#404: The resource you tried to access wasn’t found on the server.
#503: The server is not ready to handle the request.

#Info recieved from API
print(response.json())
#JSON = JavaScript Object Notation is the language of APIs
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

#API Request with Query Parameters
