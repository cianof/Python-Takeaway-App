from lxml import html
import requests, json
import googlemaps



#key hidden for obvious security purposes
API_KEY = ""  

gmaps = googlemaps.Client(key='API_KEY')
usersLat = 0.0
usersLng = 0.0

pizzaChoice = ''

#uses the google Maps API to retrieve the User's co-ordinates.
def getlocation():
	location = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=API_KEY")
	results = json.loads(response)
    usersLat = res_json.get("location").get("lat")
    usersLng = res_json.get("location").get("lng")
    print(usersLat)
    print(usersLng)

#uses the co-ordinates recieved from the above function to get a radius and within contains local restaurants
def getRadius():
	#TO-DO 


#this will scrape the relevent pizza chain's website and try to parse their menu
def showMenu():
	if pizzaChoice == "Apache":

		page = requests.get('https://www.apache.ie/order/pizza')
		tree = html.fromstring(page.content)
		menu = tree.xpath('//div[@title="buyer-name"]/text()')
		print("What would you like to order? \nChoose from: ")
		print("menu", menu)

	elif pizzaChoice == "Dominos":

		page = requests.get('https://www.dominos.ie/menu?eircode=1#')
		tree = html.fromstring(page.content)
		menu = tree.xpath('//div[@title="buyer-name"]/text()')
		print("What would you like to order? \nChoose from: ")
		print("menu", menu
	else 
	print("sorry this chain does not suit our drivers")






