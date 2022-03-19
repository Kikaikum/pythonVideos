from ipaddress import ip_address
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

#Este archivo a partir de JSON de cursos crea un JSON para cada curso con las URLS de cada video para luego descargarlo


#Declarar Variables
datos=[]

#Abrir Chrome con selenium en modo movil y ah pantalla completa
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

#Ir a udemy y iniciar sesion
driver.get('https://www.udemy.com')
kike=input('Inicia sesion en udemy y pulsa enter')



with open('cursos.json') as file:
    data = json.load(file)

for i in data:
    print(i,data[i])
    driver.get(data[i])
    sleep(2)
    for x in range(50):
        try:           
            boton=driver.find_elements_by_css_selector('udlite-btn.udlite-btn-large.udlite-btn-link.udlite-heading-md.js-panel-toggler.panel--panel-toggler--30J_B')
            print(boton)
            for z in boton:
                print(z)
            print('click1')
        
            sleep(5000)
            try:
                for v in range(20):
                    boton = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[1]/div[1]/main/div/div[2]/section/div[2]/div/div/div[7]/div[2]/div/ul/li[{v+1}]')                    
                    boton.click()
                    print('click')
                    sleep(2)
                    titulo = driver.find_element_by_xpath(f'/html/body/div[2]/div[1]/div/div/main/div/div[2]/section/div[2]/div/div/div[{x+1}]/div[2]/div/ul/li[{v+1}]/div/div[2]/div[1]/div/span/span/span').text
                    print(titulo)
                    link = driver.find_element_by_xpath(f'/html/body/div[2]/div[1]/div[1]/div[1]/main/div/div[1]/div/div/div/div/div/div/div/div/div/section/div/div[1]/div/div/video').get_attribute("src")
                    print(link)
                    datos[titulo]=link       
                    with open(i+'.json', 'w') as json_file:
                        json.dump(data, json_file)
                                   
            except:
                print('ya no hay mas')


        except:
            print('ya no hay mas')

