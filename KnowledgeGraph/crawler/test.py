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

driver = webdriver.Chrome()
url = 'https://www.tianyancha.com/search?key=%s' % '偶数科技'
driver.get(url)
driver.implicitly_wait(3)
#print(driver.page_source)
spans = driver.find_elements_by_css_selector('div[class=\"search-result-single\"]')

if len(spans)>0:
    print("hhhh")
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

def toNumericalAndCategory(s):
    if s=='$' or s=='-':
        return "$ ","$ "
    ind=s.find("万")
    num=""
    cat=""
    if ind==-1:
        for c in s:
            if c>='0' and c<='9':
                num=num+c
            else:
                cat=cat+c
    else:
        num=float(s[:ind])
        num*=10000
        num=str(num)
        cat=s[ind+1:]
    return num,cat
#TODO: extract INFO
#extractInfoToTsv()
def extractInfo(companyName,driver,f):
    try:
        driver.find_element_by_xpath("//div[@class='tab-header -search']/div[2]/div[1]/form/div/input").clear()
        driver.find_element_by_xpath("//div[@class='tab-header -search']/div[2]/div[1]/form/div/input").send_keys(companyName)
        print('input success!')
    except:  
        print('input error!')
    time.sleep(0.5)
    try:  
        driver.find_element_by_xpath("//div[@class='tab-header -search']/div[2]/div[1]/div").click() 
        print('click success!')
    except:  
        print('click error!')
    time.sleep(0.5)
    spans = driver.find_elements_by_css_selector('div[class=\"search-result-single \"]')
    if(len(spans)>0):
        try:
            nam=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[1]/a").text
        except:
            print("Name not found!")
            nam="$"
        f.write(nam+"/")
        try:
            per=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[2]/div[1]/a[@class='legalPersonName hover_underline']").text
        except:
            print("Person not found!")
            per="$"
        f.write(per+"/")
        try:
            mny=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[2]/div[2]/span").text
        except:
            print("Capital not found!")
            mny="$"
        num,cate=toNumericalAndCategory(mny)
        f.write(num+"/"+cate+"/")
        try:
            tim=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[2]/div[3]/span").text
        except:
            print("Time not found!")
            tim="$"
        f.write(tim+"/")
        try:
            tele=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[@class='contact']/div[1]/span[2]").text
        except:
            print("Telephone not found!")
            tele="$"
        f.write(tele+"/")
        try:
            ema=driver.find_element_by_xpath("//div[@class='search-result-single ']/div[2]/div[@class='contact']/div[2]/span[2]").text
        except:
            print("Email not found!")
            ema="$"
        f.write(ema+"\n")

    else:
        print("company not found!")


csv_reader = csv.reader(open('./company_before.csv', encoding="GB18030"))
with open("./company_info","w",encoding="UTF-8") as ci:
    ci.write("公司名称"+" "+"公司法人"+" "+"注册资本"+" "+"货币类型"+" "+"注册时间"+" "+"联系电话"+" "+"邮箱\n")
    for row in csv_reader:
        extractInfo(row[0],driver,ci)




    
