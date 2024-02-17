# Sample Python code utilizing modules
 
# Importing the datetime module to work with dates and times
import datetime
 
# Importing the math module to perform mathematical operations
import math
 
# Importing the random module to generate random numbers
import random
 
# Importing the requests module to make HTTP requests
import requests
 
# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)
 
# Calculate the square root of a number
num = 25
square_root = math.sqrt(num)
print("Square Root of", num, ":", square_root)
 
# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("Random Number between 1 and 100:", random_number)
 
# Make an HTTP GET request to a sample API
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bpi']['USD']['rate']
    #print("Current Bitcoin Price (in USD):", bitcoin_price)
    print("Changed")
else:
    print("Failed to retrieve Bitcoin price. Status code:", response.status_code)
