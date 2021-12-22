#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests


path = "df_link.csv"
data = pd.read_csv(path, index_col=[0])
data.rename(columns={'0': 'links'},inplace=True)

def fetch_page(URL):
    r = requests.get(URL, headers= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


zimmer_list = []
price_list = []
description_list = []
area_list = []
corrupted_add = []




for ind, URL in enumerate(data['links']):
    try:
        soup = fetch_page(URL)
        zimmer = soup.find("span", {"class": "liRmo wi_ND j5x8k t5Xdw"}).text
        price = soup.body.findAll("div", attrs={'class': 'relative z-index-10 WZBVL wi_ND X2vjS t5Xdw'})[0].text
        description = soup.find("div", {"class": "AhB_5 wi_ND X2vjS"}).text
        area = soup.findAll("span", {"class": "liRmo wi_ND MhP2K t5Xdw"})[-1].text

        zimmer_list.append(zimmer)
        price_list.append(price)
        description_list.append(description)
        area_list.append(area)
        print(ind)


    except:
        corrupted_add.append(URL)
        pass


df = pd.DataFrame(zip(zimmer_list, price_list,area_list, description_list ), names=["zimmer", "price","area", "description"])


df.to_csv("raw_data.csv", index=False)