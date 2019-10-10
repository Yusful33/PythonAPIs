import requests 
import json
api_key = 'd1w48MCCZQ4vCs30VY9ToWNtrUwhDWr5m8V_-9ThQlhWrJ0UnTd5PX5LmW27ZRHf3Gx7HzcNboQs3m6tmFDoa3MGub3IHzw2vHwR8TP6VYE1KKFRx89TucXYayeeXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'
params = {'term': 'Gluten-Free', 'location': 'Fairfax, VA', 'limit': '5', 'Open_now': 'True'}
req = requests.get(url, params=params, headers=headers)
#You want an error code of 200 here
print('The status code is {}'.format(req.status_code))
#Seeing the information requested
parsed = json.loads(req.text)
#Cleaning up the formatting of info recieved
#print(json.dumps(parsed, indent=4))
#Just looking at the 
businesses = parsed["businesses"]
#Loop to go through every single restaurant that fits our search criteria
for business in businesses:
    print("Name", business["name"])
    print("Rating:", business["rating"])
    #Need to utilize the .join here becuase "display_address" is within the "location" list
    print("Address:", " ".join(business["location"]["display_address"]))
    print("Phone:", business["phone"])
    print("\n")
    id = business["id"]
    #Expanding our results to pull in more than just restaurants but also reviews
    url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"
    req = requests.get(url, headers=headers)
    parsed = json.loads(req.text)
    reviews = parsed["reviews"]
    #Displaying out the basic info of the restaurant and three reviews
    for review in reviews:
        print("User:", review["user"]["name"], "Rating:", 
          review["rating"], "Review:", review["text"], "\n")
