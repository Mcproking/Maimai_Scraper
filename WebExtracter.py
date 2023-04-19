import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    # USERDATA ! NEED TO REMOVE ! MAKE IT INTO JSON ALSO CAN KEKW
    with open("./details_goes_here.txt","r") as f:
        details = f.readlines()
        id = details[0].split(":")[1].splitlines()[0]
        password = details[1].split(":")[1].splitlines()[0]
    Details = {"USERNAME":id, "PASSWORD":password}
except:
    print("ID and Password not yet insert")
    exit()

# Randomize number for sleep, try not to get too consistant
def randNum(minTime, maxTime): 
    return random.randint(minTime,maxTime)

def main():
    tic = time.perf_counter()
    Login(Details)
    time.sleep(randNum(3,5))
    openRecord()
    time.sleep(randNum(3,5))
    insertRecordstxt()
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.4f} seconds")

def Login(Details):
    global driver
    USERNAME = Details["USERNAME"]
    PASSWORD = Details["PASSWORD"]

    # Website URL and webkits
    URL = "https://maimaidx-eng.com/maimai-mobile/home/"
    PATH = r"chromedriver_win32\\chromedriver.exe"

    # Init the Webdriver and connect to the website
    driver = webdriver.Chrome(PATH)
    driver.get(URL)

    # Expand the login Form under the "Sega ID" button
    openSega = "$('#segaid dt').addClass('isOpen');\n$('#segaid dd').css('display','block');"
    driver.execute_script(openSega)

    # Locate User and Password <input> and login the website.
    searchSID = driver.find_element(by=By.ID, value="sid")
    searchPassword = driver.find_element(by=By.ID, value="password")
    searchSID.send_keys(USERNAME)
    searchPassword.send_keys(PASSWORD)
    time.sleep(randNum(2,4))
    searchPassword.send_keys(Keys.RETURN)
    
    XpathRecord = '//div[@class="c-caution"]'
    errorLogin = driver.find_elements(by=By.XPATH,value=XpathRecord)

    if bool(errorLogin) == True:
        print("ID or Password Incorrect")
        print(bool(errorLogin))
        driver.quit()
        return

def openRecord():
    XpathRecord = "//a[@href='https://maimaidx-eng.com/maimai-mobile/record/']"
    gotoRecord = driver.find_elements(by=By.XPATH, value=XpathRecord)[1].click
    gotoRecord()
    
def extractRecords():
    record = []
    XpathsearchRecordClass = '//div[@class="p_10 t_l f_0 v_b"]'
    searchRecordClass = driver.find_elements(by=By.XPATH, value=XpathsearchRecordClass)
    for records in searchRecordClass:
        record.append(records.get_attribute('innerHTML'))
    return record
    
def extractRecordsHits():
    idxURL = "https://maimaidx-eng.com/maimai-mobile/record/playlogDetail/?idx={}"
    idxRecord = [] 
    hitRecord = []
    XpathsearchIdx = '//input[@name="idx"]'
    searchIdx = driver.find_elements(by=By.XPATH, value=XpathsearchIdx)
    for idxs in searchIdx:
        idxRecord.append(idxs.get_attribute('value'))
    
    for x in idxRecord:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(idxURL.format(x))
        XpathsearchGrayBox = '//div[@class="gray_block m_10 m_t_0 p_b_5 f_0"]'
        searchGrayBox = driver.find_elements(by=By.XPATH, value=XpathsearchGrayBox)
        for hits in searchGrayBox:
            hitRecord.append(hits.get_attribute('innerHTML'))
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return hitRecord
       
def insertRecordstxt():
    records_List = extractRecords()
    hitrecord_List = extractRecordsHits()

    for record in range(0,50):
        file = open(r"./Html_Extracted/{}.txt".format(record+1), "w", encoding="UTF-8")
        file.write(records_List[record])
        file.close()
        file = open(r"./Html_Extracted/{}.1.txt".format(record+1), "w", encoding="UTF-8")
        file.write(hitrecord_List[record])
        file.close()
    
if __name__ == "__main__":
    pass