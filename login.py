import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# LAUNCHING BROWSER

# driver = webdriver.Chrome(executable_path="C:\\Users\\FL_LPT-373\\Downloads\\chromedriver_win32.exe")
# c_service = chrome_service('Drivers/chromedriver.exe')
c_service = chrome_service("Drivers/chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\\Users\\FL_LPT-373\\Downloads\\chromedriver_win32\\chromedriver.exe")

# driver = webdriver.Chrome(service=c_service)
# service = Service('C:\\Users\\FL_LPT-373\\Downloads\\chromedriver_win32.exe')
driver.maximize_window()
driver.get("https://www.nykaa.com/")
driver.implicitly_wait(10)

# login
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
driver.find_element(By.XPATH, "//button[text()='Sign in with Mobile / Email']").click()
driver.find_element(By.NAME, 'emailMobile').send_keys('8332062227')
driver.find_element(By.ID, 'submitVerification').click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[@class='button big fill full ']").click()
time.sleep(5)
# driver.find_element()
# driver.find_element(By.XPATH,"//div[@class='outline-wrapper']").click()
# driver.find_element(By.XPATH, "(//div[@class='outline-wrapper'])[30]").click()
# print("nykka")
time.sleep(5)
select = driver.find_element(By.XPATH, "//a[text()='brands']")
ActionChains(driver).move_to_element(select).perform()
driver.find_element(By.XPATH,
                    "//img[@src='https://adn-static2.nykaa.com/media/wysiwyg/cms/beauty/menu/nykaa-cosmetics.png']").click()
driver.find_element(By.XPATH, "//html").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
select1 = driver.find_element(By.XPATH, "//img[@src='https://images-static.nykaa.com/media/catalog/product/tr:w-220,"
                                        "h-220,cm-pad_resize/3/e/3ec6a0dNYKAC00001480_1n.jpg']")
ActionChains(driver).move_to_element(select1).perform()

driver.find_element(By.XPATH, "//span[text()='Add to Bag']").click()
time.sleep(5)
# select2 = driver.find_element(By.XPATH, "//img[@src='https://images-static.nykaa.com/media/catalog/product/tr:w-220,"
#                                         "h-220,cm-pad_resize/3/e/3ec6a0dNYKAC00001480_1n.jpg']")
select2 =driver.find_element(By.XPATH, "//img[@src='https://images-static.nykaa.com/media/catalog/product/tr:w-220,"
                                       "h-220,cm-pad_resize/3/e/3ec6a0dNYKAC00001480_1n.jpg']")


ActionChains(driver).move_to_element(select2).perform()
driver.find_element(By.XPATH, "//span[text()='Add to Bag']").click()
time.sleep(5)

select3 = driver.find_element(By.XPATH, "//button[@type='submit']")
ActionChains(driver).move_to_element(select3).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Add to Bag']").click()
# driver.find_element(By.XPATH, "(//span[text()='Add to Bag'])[3]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@class='css-g4vs13']").click()
time.sleep(5)
driver.close()

