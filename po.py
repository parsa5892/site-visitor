from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
from selenium.webdriver.common.by import By
import requests as rq
import json
url=(input("type your url to visit"))
getnum=int(input("enter how many times to visit"))
delay=int(input("enter to wait in any page"))
driverproxy=webdriver.Firefox(executable_path="./geckodriverpro")
driverproxy.get("https://geonode.com/free-proxy-list")
urlinput=driverproxy.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[1]/div[2]/div/input")
e=rq.get(urlinput.get_attribute("value"))
e=e.json()
proxys=[]
ip=e["data"]
for i in ip:
    proxys.append(str(i['ip']+":"+i['port']))
option=webdriver.FirefoxOptions()
option.add_argument("-private")
i=0
for i in range(getnum):
    print("proxy :  "+proxys[i])
    driver=webdriver.Firefox(executable_path="./geckodriver",proxy=proxys[i],options=option)
    i+=1
    driver.get("https://lnr.app/s/67kwgJ")
    sleep(delay)
    driver.close()