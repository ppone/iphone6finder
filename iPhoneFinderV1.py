import urllib2
import json

''' Pass your zipcode as a string argument to the functions below'''

iphones = {
	"iPhone 6 Silver 16GB T-Mobile": "MG552",
	"iPhone 6 Silver 64GB T-Mobile": "MG5C2",
	"iPhone 6 Silver 128GB T-Mobile": "MG582",
	"iPhone 6 Gold 16GB T-Mobile": "MG562",
	"iPhone 6 Gold 64GB T-Mobile": "MG5D2",
	"iPhone 6 Gold 128GB T-Mobile": "MG592",
	"iPhone 6 Space Gray 16GB T-Mobile": "MG542",
	"iPhone 6 Space Gray 64GB T-Mobile": "MG5A2",
	"iPhone 6 Space Gray 128GB T-Mobile": "MG572",
	"iPhone 6+ Silver 16GB T-Mobile": "MGC02",
	"iPhone 6+ Silver 64GB T-Mobile": "MGC62",
	"iPhone 6+ Silver 128GB T-Mobile": "MGC32",
	"iPhone 6+ Gold 16GB T-Mobile": "MGC12",
	"iPhone 6+ Gold 64GB T-Mobile": "MGC72",
	"iPhone 6+ Gold 128GB T-Mobile": "MGC42",
	"iPhone 6+ Space Gray 16GB T-Mobile": "MGAX2",
	"iPhone 6+ Space Gray 64GB T-Mobile": "MGC52",
	"iPhone 6+ Space Gray 128GB T-Mobile": "MGC22",
}

unusedDict = {
	"iPhone 5S Silver 16GB SIM-free": "ME297",
	"iPhone 5S Silver 32GB SIM-free": "ME300",
	"iPhone 5S Gold 16GB SIM-free": "ME298",
	"iPhone 5S Gold 32GB SIM-free": "ME301",
	"iPhone 5S Space Gray 16GB SIM-free": "ME296",
	"iPhone 5S Space Gray 32GB SIM-free": "ME299",
}

def iphoneFinder(zipcode):
	'''Runs the iphones dictionary for a certain zipcode. This function only prints if an iphone value is found in stock'''

	dummy = False
	for i in iphones.keys():
		target = "http://store.apple.com/us/retailStore/availabilitySearch?parts.0=" + str(iphones[i]) + "LL%2FA&zip=" + zipcode
		json_input = urllib2.urlopen(target)
		decoded = json.load(json_input)
		for j in decoded["body"]["stores"]:
			if j["partsAvailability"][str(iphones[i]) + "LL/A"]["pickupSearchQuote"] == "Available today":
				dummy = True
				print str(i) + " - " + j["partsAvailability"][str(iphones[i]) + "LL/A"]["pickupSearchQuote"] + " - " + str(j["storeName"])

	if dummy == False:
		print "Sorry, no iPhones are available at this time"

def iphoneReport(zipcode):
	'''Runs the iphones dictionary for a certain zipcode. This function prints the nearby inventory for each key/value in the dictionary'''

	for i in iphones.keys():
		target = "http://store.apple.com/us/retailStore/availabilitySearch?parts.0=" + str(iphones[i]) + "LL%2FA&zip=" + zipcode
		json_input = urllib2.urlopen(target)
		decoded = json.load(json_input)
		for j in decoded["body"]["stores"]:
			print str(i) + " - " + j["partsAvailability"][str(iphones[i]) + "LL/A"]["pickupSearchQuote"] + " - " + str(j["storeName"])