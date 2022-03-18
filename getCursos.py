from ipaddress import ip_address
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

data = {}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.udemy.com')
kike=input('mas? ')

for x in range(2000):
    kike=input('mas? ')
    for i in range(12):        
        titulo = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div/ul/li/div[3]/div/div[{i+1}]/div[1]/div/a/strong').text
        print(titulo)        
        url = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div/ul/li/div[3]/div/div[{i+1}]/div[1]/div/a').get_attribute("href")
        print(url)
        data[titulo]=url        
        with open('cursos.json', 'w') as json_file:
            json.dump(data, json_file)




