from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.hko.gov.hk/en/")
elem = driver.find_element(by=By.CSS_SELECTOR, value=".area_current")
records = []
# cells = driver.find_elements_by_css_selector(".area_current")
tempc = driver.find_element_by_css_selector(".hkoMinTemp")
records.append(tempc.text.strip())
tempf = driver.find_element_by_css_selector(".hkoMaxTemp")
records.append(tempf.text.strip())
tempnow = driver.find_element_by_css_selector(".hkoTemp")
records.append(tempnow.text.strip())
mist = driver.find_element_by_css_selector(".hkoRH")
records.append(mist.text.strip())
print(records)
