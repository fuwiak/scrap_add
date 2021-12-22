#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests


def fetch_page(URL):
    r = requests.get(URL, headers= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def extract_links(soup, markup: str, class_name: str, page_name: str):
    # temp = soup.body.findAll('li', attrs={'class' : 'Nfm8t'})
    markups = soup.body.findAll(markup, attrs={'class': class_name})
    links = [page_name+mark.a.get('href') for mark in markups]
    return links








URLS = ['https://www.immobilienscout24.at/regional/wien/wien/immobilien']

next_urls = ["https://www.immobilienscout24.at/regional/wien/wien/immobilien/seite-{n}".format(n=i) for i in range(2, 101)]
URLS.extend(next_urls)

all_flats_web_adress = []

# URLS = URLS[:5]
for ind, URL in enumerate(URLS):
    print(ind)
    soup = fetch_page(URL)
    links = extract_links(soup, 'li', 'Nfm8t', 'https://www.immobilienscout24.at')
    all_flats_web_adress.append(links)


all_flats_web_adress = sum(all_flats_web_adress, [])

df_link = pd.DataFrame(all_flats_web_adress, columns=["link"])

df_link = pd.DataFrame(all_flats_web_adress)
df_link.to_csv("df_link.csv")