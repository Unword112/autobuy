import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:/Program Files (x86)/chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://www.bestbuy.com/site/apple-watch-series-6-gps-44mm-space-gray-aluminum-case-with-black-sport-band-space-gray/6215931.p?skuId=6215931")
#browser.get("https://www.bestbuy.com/site/monster-hunter-rise-deluxe-edition-nintendo-switch/6433189.p?skuId=6433189")

buybtn = False

btnlg = False

while not btnlg:
    try:
        clickbtnlg = browser.find_element_by_class_name("us-link")
        clickbtnlg.click()
        print("United States")
        break
    except:
        print("United States")
        break

while not buybtn:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")
        print("Button isnt ready.")
        time.sleep(1)
        browser.refresh()
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-secondary")
        addToCartBtn.click()
        print("Button is ready.")
        buybtn = True      
        
comfirmed = False

while not comfirmed:
    try:
        addCart = browser.find_element_by_class_name("add-to-cart-button")
        addCart.click()
        print("Add Cart")
        break
        comfirmed = True
    except:
        print("Not Add cart")
        break

while not comfirmed:
    try:
        checkoutbtn = browser.find_element_by_class_name("checkout-buttons")
        checkoutbtn.click()
        print("Check out!")
        break
    except:
        print("Not Well to Check out")
        break