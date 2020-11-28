from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller


geckodriver_autoinstaller.install() 
profile = webdriver.FirefoxProfile("/home/steve1442/.mozilla/firefox/vn0acv8k.default-release")
driver = webdriver.Firefox(profile)


driver.implicitly_wait(10000)
def buyItem(url):
   # try:
        driver.get(url)
        assert "Amazon" in driver.title
        elem = driver.find_element_by_name("submit.add-to-cart")
        elem.click()
        driver.get("https://www.amazon.com/gp/cart/view.html")
        elem = WebDriverWait(driver, 1000000000).until(EC.element_to_be_clickable((By.NAME, "proceedToRetailCheckout")))
        elem.click()
        elem = WebDriverWait(driver, 1000000000).until(EC.element_to_be_clickable((By.CLASS_NAME, "a-declarative")))
        elem = driver.find_element_by_link_text("Deliver to this address")
        elem.click()
        elem = driver.find_element_by_class_name("a-button-text")
        elem = WebDriverWait(driver, 1000000000).until(EC.element_to_be_clickable((By.CLASS_NAME, "a-button-text")))
        elem.click()
        elem = WebDriverWait(driver, 1000000000).until(EC.element_to_be_clickable((By.NAME, "ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")))
        elem.click()
        elem = WebDriverWait(driver, 1000000000).until(EC.element_to_be_clickable((By.NAME, "placeYourOrder1")))
        elem.click()
   

buyItem("https://www.amazon.com/Communion-Bread-approx-500-pieces/dp/B001VHYZP2/ref=sr_1_2?dchild=1&keywords=communion+wafers&qid=1589154839&sr=8-2")