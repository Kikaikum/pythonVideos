from ipaddress import ip_address
from pickle import FALSE, TRUE
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

#Coger titulo y URL's de los cursos 


"""
Aqui faltaria ir cambiando automaticamente de pagina

"""



#Declaracion de variables
data = {}
first=TRUE

#Abrir chrome en modo movil 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)

#Ir a udemy para iniciar sesion
driver.get('https://www.udemy.com')
kike=input('Inicia sesion en udemy y pulsa enter')

#Descargar cursos y preguntar cuando has cambiado de pagina manualmente
for x in range(2000):
    if not first:
        kike=input('Ves a otra pagina de cursos y pulsa enter')
    for i in range(12):        
        titulo = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div/ul/li/div[3]/div/div[{i+1}]/div[1]/div/a/strong').text
        print(titulo)        
        url = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div/ul/li/div[3]/div/div[{i+1}]/div[1]/div/a').get_attribute("href")
        print(url)
        data[titulo]=url 
        first=FALSE       
        with open('cursos.json', 'w') as json_file:
            json.dump(data, json_file)




