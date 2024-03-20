# Project 15 
# Site Connectivity Checker

# Step 1 - import urllib
# Step 2 - use urllib.request
# Step 3 - write a function that takes a url
# Step 4 - returns a response

import urllib.request as urllib

print("This is a site connectivity checker program.")
input_url = input("Input the url of the site you want to check: ")

def main(url):
    print("Checking connectivity...")
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully!")

# Continuing...
