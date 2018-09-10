# -*- coding: utf-8 -*-
#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import FirefoxOptions
import csv

firefox_options = FirefoxOptions()
firefox_options.set_headless()
browser=webdriver.Firefox(options = firefox_options)
browser.get("https://www.aqistudy.cn/")
try:

    for name in ['北京', '天津', '石家庄', '辛集', '唐山', '秦皇岛', '保定', '定州', '张家口', '承德', '沧州', '廊坊', '衡水']:
        frame = browser.find_element_by_xpath('//div[@class="panel-body panel-body-noheader panel-body-noborder"]/iframe')
        browser.switch_to_frame(frame)   ##切换到相应的frame

        input1=browser.find_element_by_id("city")
        input1.clear()
        input1.send_keys(name)
        input1.send_keys(Keys.ENTER)
        time.sleep(1)

#        action = ActionChains(browser)
#        browser.find_element_by_xpath('//input[@id="city"]').click()
#        time.sleep(1)
#        action.move_to_element(browser.find_element_by_xpath('//div[@class="citySelector"]')).perform()
#        time.sleep(1)
#        browser.find_element_by_xpath('//div[@id="cityBox"]//a[position()=' + str(i) + ']').click()
#        time.sleep(1)
        stations = browser.find_elements_by_xpath('//div[@class="datagrid-view2"]//tr')[1:]
        for station in stations:
            item = {}
            item["city_name"] = station.find_element_by_xpath('./td[1]').text
            item["date"] = browser.find_element_by_xpath('//span[@id="dateSpan"]').text
            item["time"] = browser.find_element_by_xpath('//span[@id="timeSpan"]').text
            item["AQI"] = station.find_element_by_xpath('./td[position()=2]').text
            item["quality"] = station.find_element_by_xpath('./td[position()=3]').text
            item["pm2_5"] = station.find_element_by_xpath('./td[position()=4]').text
            item["pm10"] = station.find_element_by_xpath('./td[position()=5]').text
            item["co"] = station.find_element_by_xpath('./td[position()=6]').text
            item["no2"] = station.find_element_by_xpath('./td[position()=7]').text
            item["o3"] = station.find_element_by_xpath('./td[position()=8]').text
            item["so2"] = station.find_element_by_xpath('./td[position()=9]').text
            item["source"] = station.find_element_by_xpath('./td[position()=10]').text
            print(item)
            with open('aqi.csv','a') as f:
                f_write = csv.writer(f)
                f_write.writerow((item["city_name"],item["date"],item["time"],item["AQI"],item["quality"],item["pm2_5"],item["pm10"],item["co"],item["no2"],item["o3"],item["so2"],item["source"]))
        browser.refresh()
        time.sleep(1)
finally:
    browser.close()
