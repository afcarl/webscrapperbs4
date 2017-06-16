# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# specify the url
url = "http://www.accuweather.com/en/in/chennai/206671/current-weather/206671"

# get the web page content and store it in a variable 'webpage’
webpage = urllib2.urlopen(url)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(webpage, "html.parser")

#finding the block we need
temp_block = soup.find('span', attrs={'class': 'large-temp'})
stats_block = soup.find('ul', attrs={'class': 'stats'})
sunrise_block = soup.find('ul', attrs={'class': 'time-period'})

# strip() is used to remove starting and trailing tags
temp = temp_block.text.strip()
stats = stats_block.text.strip()
sunrise= sunrise_block.text.strip()

print "Temperature:"+temp
print "\nStats:\n\n"+stats
print "\nSunrise:\n\n"+sunrise

temp=temp.encode('utf-8') 
stats=stats.encode('utf-8') 
sunrise=sunrise.encode('utf-8') 

# opening a csv file in append mode to keep the old data
with open('weather.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([temp,stats,sunrise,datetime.now()])
