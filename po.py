from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
from selenium.webdriver.common.by import By
import pandas as pd
sheet=pd.read_csv("/home/non/Desktop/new/Free_Proxy_List.csv")
url=(input("type your url to visit"))
getnum=int(input("enter how many times to visit"))
delay=int(input("enter to wait in any page"))
option=webdriver.FirefoxOptions()
option.add_argument("-private")
i=0
for i in range(getnum):
    proxy=ip=str(sheet['ip'][i])+":"+str(sheet['port'][i])
    print(proxy)
    driver=webdriver.Firefox(executable_path="/home/non/Desktop/new/geckodriver",proxy=proxy,options=option)
    i+=1
    driver.get("https://lnr.app/s/67kwgJ")
    sleep(10)
    driver.close()