#!/usr/bin/python
# coding = 'UTF-8'
from time import sleep

from appium import webdriver
import logging

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'de.danoeh.antennapod'
desired_caps['appActivity'] = 'de.danoeh.antennapod.activity.SplashActivity'
desired_caps['eventTimings'] = True
desired_caps['app'] = '/Users/evanna/Desktop/lizi/app-free-release-signed.apk'
logging.info("logging app...")

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# wait to lauch the activity
sleep(2)

# click
button_2 = driver.find_element_by_id("de.danoeh.antennapod:id/imgvCover")
button_2.click()

# press key
driver.press_keycode(24)

# pinch
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
action1 = TouchAction(driver).press(el=None, x=width * 0.2, y=height * 0.2).wait(1000).move_to(el=None,
                                                                                              x=width * 0.4,
                                                                                              y=height * 0.4).release()
action2 = TouchAction(driver).press(el=None, x=width * 0.8, y=height * 0.8).wait(1000).move_to(el=None,
                                                                                               x=width * 0.6,
                                                                                               y=height * 0.6).release()
pinch_action = MultiAction(driver)
pinch_action.add(action1, action2)
pinch_action.perform()

# get the last page source
page_source = driver.page_source
