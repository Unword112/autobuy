import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:/Program Files (x86)/chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://shopee.co.th/%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B8%88%E0%B8%AD%E0%B8%A2%E0%B8%84%E0%B8%A7%E0%B8%A1%E0%B8%84%E0%B8%B8%E0%B8%A1%E0%B8%97%E0%B8%B4%E0%B8%A8%E0%B8%97%E0%B8%B2%E0%B8%87-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%A1%E0%B8%9A%E0%B8%99%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%96%E0%B8%B7%E0%B8%AD-1-%E0%B8%8A%E0%B8%B4%E0%B9%89%E0%B8%99-i.100515615.4737356347")
#browser.get("https://shopee.co.th/Sale%E2%80%BC%EF%B8%8F-%F0%9F%94%A5%E0%B8%81%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%81%E0%B8%87%E0%B9%83%E0%B8%99%E0%B8%8A%E0%B8%B2%E0%B8%A2-%E0%B9%80%E0%B8%99%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%B8%E0%B9%88%E0%B8%A1-%E0%B8%A1%E0%B8%B5%E0%B8%8B%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B8%E0%B8%81%E0%B8%95%E0%B8%B1%E0%B8%A7-%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%94%E0%B9%89-%E0%B9%80%E0%B8%A7%E0%B9%89%E0%B8%B2%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%EF%BC%888825-1%EF%BC%89-i.124032559.1887661138")

buybtn = False
langbtn = False
while not langbtn:
    try:
        btnLanguage = browser.find_element_by_class_name("shopee-button-outline")
        btnLanguage.click()

        while not buybtn:
            try:
                addToCartBtn = browser.find_element_by_class_name("btn-tinted")
                print("Button isnt ready.")
                time.sleep(1)
                browser.refresh()
    
            except:
                addToCartBtn = browser.find_element_by_class_name("btn-solid-primary")
                print("Button is ready.")
                addToCartBtn.click()
                buybtn = True
    finally:
        browser.quit()