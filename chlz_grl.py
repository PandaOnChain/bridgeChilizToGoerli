from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # чтобы парсить адреса
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
from multiprocessing import Pool

import undetected_chromedriver as uc

from web3 import Web3
from json import loads

import random


mtmsku: list = open('eth_atom.txt', 'r', encoding='utf-8').read().splitlines()
addres = []

for wallet in mtmsku:
    addres.append(wallet.split(':')[0])

pswrd = "###"


def Confirm():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.refresh()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()[contains(.,'Confirm')]]"))).click()
    driver.switch_to.window(driver.window_handles[0])


def DBVT():
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/form/section[2]/section[2]/div/div/input'))).clear()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/form/section[2]/section[2]/div/div/input'))).send_keys(str(random.randint(2, 6)))
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/form/section[3]/section/div[2]/label/div/span'))).click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/form/section[5]/button'))).click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/div[4]/div[2]/button[1]'))).click()
        time.sleep(1)
        ConfirmJala()
        time.sleep(15)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//*[text()[contains(.,'In Transit')]]")))

    except:
        pass


def ChckCnnctWllt():
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/div[1]/button'))).click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/aside/section/ul/li/button/span'))).click()
        driver.switch_to.window(driver.window_handles[1])
        driver.get(
            "chrome-extension://dkhpanfopmlnehhnibfobghhkpebfbni/popup.html")
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Next')]"))).click()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Connect')]"))).click()
        except:
            print("Probuyu reject")
            try:
                if driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]').text == "Reject":
                    wait.until(EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]'))).click()
            except:
                print("PZDC NHY BLT Connect kshka ne proshel")
        driver.switch_to.window(driver.window_handles[0])
    except:
        try:
            driver.switch_to.window(driver.window_handles[1])
            driver.get(
                "chrome-extension://dkhpanfopmlnehhnibfobghhkpebfbni/popup.html")
            try:
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(text(),'Next')]"))).click()
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(text(),'Connect')]"))).click()
            except:
                print("Probuyu reject")
                try:
                    if driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]').text == "Reject":
                        wait.until(EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/div[3]/footer/button[1]'))).click()
                except:
                    #print("PZDC NHY BLT Connect kshka ne proshel")
                    pass
            driver.switch_to.window(driver.window_handles[0])
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mouse-parallax-container"]/section/section/section/div/article/div[1]/button'))).click()
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/aside/section/ul/li/button/span'))).click()
        except:
            pass


def poshla_zhara(adrs):
    print(addres.index(adrs))
    chop = webdriver.ChromeOptions()
    chop.add_argument('--lang=en')
    chop.add_argument(
        r"\chillz\profiles\\" + adrs)
    chop.add_argument("--disable-blink-features=AutomationControlled")
    chop.add_extension("metamask-chrome-10.6.4.crx")

    global driver
    driver = webdriver.Chrome(chrome_options=chop)
    global wait
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    global handle
    handle = driver.window_handles
    driver.switch_to.window(handle[0])
    unlock = driver.find_element_by_xpath(
        "//*[contains(@class,'button')]").text
    if unlock == "Unlock":
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id, 'password')]"))).send_keys("SobakaAwAw")
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class,'button')]"))).click()
    driver.get("https://scoville-bridge.chiliz.com/transfer")

    ChckCnnctWllt()
    DBVT()
    driver.close()
    driver.quit()


# def main():
#     process_count = int(input("Enter the number of processes: "))
#     p = Pool(processes=process_count)
#     p.map(poshla_zhara, addres)
#     print("Успех!!! не плакай!")


def main1():
    for adrs in addres[5:]:
        poshla_zhara(adrs)


if __name__ == "__main__":
    # main()
    main1()
