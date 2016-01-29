# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:59:29 2016

@author: JimmyHome
"""
#beautiful soup scraper

import requests
from bs4 import BeautifulSoup

#this is the url for the tutorial I built this from
r = requests.get('https://www.youtube.com/watch?v=3xQTJi2tqgk')

#content turn webpage into static html to be analyzed
r = r.content

print r

soup = BeautifulSoup(r)

#this formats everything with the tags
pretty_soup = soup.prettify()

print  pretty_soup

#locate <a> tags and create list
link_lista = soup.find_all("a")

#locate <a> tags and create list
link_listp = soup.find_all("p")

#print a tags with tags
for link in link_lista:
    print link

#print a tags without tags
for link in link_lista:
    print link.text
    
#print p tags without tags
for link in link_listp:
    print link.text
    
  
  


