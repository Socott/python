# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import time
# chromedriver = "G:/chromedriver"
# os.environ['webdriver.chrome.drive'] = chromedriver
# driver = webdriver.Chrome(chromedriver)#模拟打开浏览器
# driver.get("http://www.taobao.com")#打开网站
# driver.maximize_window()#窗口最大化
# input_str = driver.find_element(By.ID,"q")
# input_str.send_keys('ipad')
# time.sleep(1)
# input_str.clear()
# input_str.send_keys('i7-8700 CPU')
# button = driver.find_element_by_class_name('btn-search')
# button.click()

from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
