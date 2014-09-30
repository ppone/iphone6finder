#!/usr/local/bin/python

import urllib2
import json
import sys
from pync import Notifier
import time

''' Pass your zipcode as a string argument to the functions below'''

APPLE_STORE_US = "http://store.apple.com/us/retailStore/availabilitySearch?parts.0="

iphones = {
        1:{"description":"iPhone 6 Silver 16GB T-Mobile", "part": "MG552"},
        2:{"description":"iPhone 6 Silver 64GB T-Mobile", "part": "MG5C2"},
        3:{"description":"iPhone 6 Silver 128GB T-Mobile", "part": "MG582"},
        4:{"description":"iPhone 6 Gold 16GB T-Mobile", "part": "MG562"},
        5:{"description":"iPhone 6 Gold 64GB T-Mobile", "part": "MG5D2"},
        6:{"description":"iPhone 6 Gold 128GB T-Mobile", "part": "MG592"},
        7:{"description":"iPhone 6 Space Gray 16GB T-Mobile", "part": "MG542"},
        8:{"description":"iPhone 6 Space Gray 64GB T-Mobile", "part": "MG5A2"},
        9:{"description":"iPhone 6 Space Gray 128GB T-Mobile", "part": "MG572"},
        10:{"description":"iPhone 6+ Silver 16GB T-Mobile", "part": "MGC02"},
        11:{"description":"iPhone 6+ Silver 64GB T-Mobile", "part": "MGC62"},
        12:{"description":"iPhone 6+ Silver 128GB T-Mobile", "part": "MGC32"},
        13:{"description":"iPhone 6+ Gold 16GB T-Mobile", "part": "MGC12"},
        14:{"description":"iPhone 6+ Gold 64GB T-Mobile", "part": "MGC72"},
        15:{"description":"iPhone 6+ Gold 128GB T-Mobile", "part": "MGC42"},
        16:{"description":"iPhone 6+ Space Gray 16GB T-Mobile", "part": "MGAX2"},
        17:{"description":"iPhone 6+ Space Gray 64GB T-Mobile", "part": "MGC52"},
        18:{"description":"iPhone 6+ Space Gray 128GB T-Mobile", "part": "MGC22"},
        19:{"description":"iPhone 6 Gold 64GB Verizon", "part": "MG652"},
        20:{"description":"iPhone 6+ Gold 64GB Verizon", "part": "MGCU2"}
}

def iphoneFinder(zipcode,phone):
	'''Runs the iphones dictionary for a certain zipcode. This function only prints if an iphone value is found in stock'''

	found = False
        target = APPLE_STORE_US + str(iphones[phone]["part"]) + "LL%2FA&zip=" + zipcode
#        print("finding => " + iphones[phone]["description"])
#        print(target)
        json_input = urllib2.urlopen(target)
        decoded = json.load(json_input)
        s = ""
        for j in decoded["body"]["stores"]:
                if j["partsAvailability"][iphones[phone]["part"] + "LL/A"]["pickupSearchQuote"] == "Available today":
                        found = True
                        s =  str(iphones[phone]["description"]) + " - " + j["partsAvailability"][str(iphones[phone]["part"]) + "LL/A"]["pickupSearchQuote"] + " - " + str(j["storeName"])
                        Notifier.notify(s)
                        print(s)
        return found
                                


while True:
        for zipcode in sys.argv[1:len(sys.argv)]:
                if iphoneFinder(zipcode,14):
                        print("phone found!")
                        time.sleep(65)
                        


