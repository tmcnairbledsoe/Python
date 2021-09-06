# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://www.amd.com/en/direct-buy/us' 
print(urlpage)
# run web driver. Make sure gecko is in the exe path
driver = webdriver.Chrome()
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(2)
results = driver.find_elements_by_xpath("//*[@id='block-amd-content']/div/div/div/div/div/div/div[3]/div/div[2]/div[4]")
print('Number of results', len(results))
# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text

# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

driver.quit()

#Install all the needed libraries. Beautiful Soup and Selenium
#Download geckodriver; https://github.com/mozilla/geckodriver/releases
#Set it in system variables path; Control Panel > Environmental Variables > System Variables > Path > Edit
#RESTART BOX

#Line 18 gets whatever you are trying to scrape by XPath. You can get this by inspecting element and then right clickiny > Copy > XPath
