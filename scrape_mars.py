#!/usr/bin/env python
# coding: utf-8

# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup

# chrome driver
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

#########################################
# Define scrape function and dictionary #
#########################################

def scrape():
    final_data = {}
    output = marsNews()
    final_data["mars_news"] = output[0]
    final_data["mars_paragraph"] = output[1]
    final_data["mars_image"] = marsImage()
    final_data["mars_weather"] = marsWeather()
    final_data["mars_facts"] = marsFacts()
    final_data["mars_hemisphere"] = marsHemisphere()
    
    return final_data

# NASA MARS NEWS #
##################

def marsNews():
    nasa_news_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_='content_title').text
    news_p = article.find("div", class_='article_teaser_body').text
    output = [news_title, news_p]
    
    return output

# JPL MARS SPACE IMAGES - FEATURED IMAGE #
##########################################

def marsImage():
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup =BeautifulSoup(html, "html.parser")
    image = soup.find("img", class_='thumb')["src"]
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23599_hires.jpg" + image
    
    return featured_image_url

# MARS WEATHER #
################
# Retrieve mars weather report page

def marsWeather():
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('div', class_="js-tweet-text-container").find('p').text.split('hPapic')[0].rstrip()
    
    if 'InSight' in mars_weather:
        mars_scraped_info['weather'] = mars_weather
    
    return mars_weather

# MARS FACTS #
##############

def marsFacts():
    import pandas as pd
    import requests
    facts_url = "https://space-facts.com/mars/"
    response = requests.get(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_data.columns = ["Description", "Value"]
    mars_data = mars_data.set_index("Description")
    mars_facts = mars_data.to_html(index=True, header=True)
    
    return mars_facts

# MARS HEMISPHERES #
####################
# Retrieve USGS images of Mars' hemispheres

def marsHemisphere():
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemisphere_image_urls = []
    products = soup.find("div", class_='result-list')
    hemispheres = products.find_all("div", class_='item')
    
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/"+end_link
        browser.visit(image_link)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        
        dictionary = {"title": title, "img_url": image_url}
        hemisphere_image_urls.append(dictionary)
        
    return hemisphere_image_urls

