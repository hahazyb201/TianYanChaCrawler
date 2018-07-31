#Construct on query

'''
search the company on TianYanCha(done)
click on the item
extract information of shareholders and analyse:
    if all shareholders are people:
        return the person having most shares
    else:
        visit companies as shareholders and extract information of their shareholders recursively.

BTW, take down information of shareholders in order to construct the KG(knowledge graph).
'''

import urllib.request
import urllib.error
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import csv
import threading, queue
import numpy as np

driver = webdriver.Chrome()
url = 'https://www.tianyancha.com/search?key=%s' % '偶数科技'
driver.get(url)
driver.implicitly_wait(3)
#print(driver.page_source)
spans = driver.find_elements_by_css_selector('div[class=\"search-result-single\"]')

if len(spans)>0:
    print("found the company")
else:
    #sign in the username  
    try:  
        driver.find_element_by_xpath("//div[@class='modulein modulein1 mobile_box pl30 pr30 f14 collapse in']/div[2]/input").send_keys('13383033617')  
        print('user success!') 
    except:  
        print('user error!')
    time.sleep(0.5)
    #sign in the pasword  
    try:  
        driver.find_element_by_xpath("//div[@class='modulein modulein1 mobile_box pl30 pr30 f14 collapse in']/div[3]/input").send_keys('137972499Ba3')  
        print('pw success!')  
    except:  
        print('pw error!')
    time.sleep(0.5)
    
    #click to login  
    try:  
        driver.find_element_by_xpath("//div[@class='modulein modulein1 mobile_box pl30 pr30 f14 collapse in']/div[5]").click()  
        print('click success!')
    except:  
        print('click error!')
    time.sleep(0.5)

spans = driver.find_elements_by_css_selector('div[class=\"search-result-single \"]')

if(len(spans)>0):
    print("hhh2")
else:
    print("login failed!")

people=[]
absoluteCapital=[]

NAME=input("Enter the company's name: ")
ff=open("./share","w")
def searchForCompany(companyName,curShare):
    url = 'https://www.tianyancha.com/search?key=%s' % companyName
    js="window.open('%s');" % url
    driver.execute_script(js)
    cur_handles=driver.window_handles
    cur=driver.current_window_handle
    f=0
    for h in cur_handles:
        if f==1:
            driver.switch_to.window(h)
            break
        if h==driver.current_window_handle:
            f=1
    time.sleep(0.5)
    
    spans = driver.find_elements_by_css_selector('div[class=\"search-result-single \"]')
    s=""
    if(len(spans)>0):
        s=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[@class='content']/div[1]/a").text
        ff.write(s+"\n")
        #print(driver.page_source)
        driver.find_element_by_xpath("//div[@class='search-result-single ']/div[@class='content']/div[1]/a").click()
        cur_handles=driver.window_handles
        f=0
        for h in cur_handles:
            if f==1:
                driver.close()
                driver.switch_to.window(h)
                break
            if h==driver.current_window_handle:
                f=1

        try:
            shareholders=driver.find_elements_by_css_selector('div[class=\"dagudong\"]')
            print(len(shareholders))
            sharePercentage=driver.find_elements_by_css_selector('span[class=\"num-investment-rate\"]')   #某些页面股东表格格式异常！
            print(len(sharePercentage))
            for i in range(len(shareholders)):
                print(i)
                si=driver.find_element_by_xpath("//div[@class='data-content']/table/tbody/tr["+str(i+1)+"]/td[2]/div[@class='text-image-human']/div[@class='dagudong']/a")
                print("33")
                sp=sharePercentage[i].text
                print(sp)
                if '%' not in sp:
                    continue
                ff.write(s+" holder: "+si.text+"\n")
                if si.get_attribute("tyc-event-ch")=="CompangyDetail.gudong.ziranren":
                    if si.text not in people:
                        people.append(si.text)
                        absoluteCapital.append(float(sp.strip('%'))/100.0*curShare)
                    else:
                        absoluteCapital[people.index(si.text)]+=float(sp.strip('%'))/100.0*curShare
                else:
                    searchForCompany(si.text,float(sp.strip('%'))/100.0)
        except:
            print("find shareholders error!")
        time.sleep(0.5)
    else:
        print("company not found!")
    driver.close()
    driver.switch_to.window(cur)
    return







searchForCompany(NAME,1.0)

print("real decision maker is: ",people[np.argmax(absoluteCapital)])


