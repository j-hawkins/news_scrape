
"""
Spyder Editor

This is a temporary script file.
"""
#%%
from bs4 import BeautifulSoup
import requests
import os


# URLs 
url = [r'https://www.bbc.co.uk/news',
       r'https://edition.cnn.com/',
       r'https://www.dailymail.co.uk/home/index.html',
       r'https://www.independent.co.uk/']

# Find current working directory
curr_dir = os.getcwd()

# Create output file
f = open(curr_dir + '\webscrape_output.txt', 'w+')

for i in url:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    tag = 'title'
    results = soup.find(tag).text
    # Write to output file 
    f.write("{} {}\n".format(results, i))

f.close()




    
