#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:59:27 2022

@author: brandon
"""
# send alert via WhatsApp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service


def send_whatsapp(phone_number, msg):
    wassup_url = rf'https://web.whatsapp.com/send?phone={phone_number}&text&type=phone_number&app_absent=0'

    # Setting url for Chrome profile and webdriver options
    chrome_options = Options()
    chrome_options.add_argument('--headless')

        # Use Service to specify the path to the ChromeDriver executable
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)


    # Open chrome browser, ignore error
    # The error appears to be a bug in the v103 chrome
    try:
        driver.get(wassup_url)
    except Exception as e:
        print(e)

    # Wait for chat box to be present
    wait = WebDriverWait(driver, 30)
    
    # inp_xpath is prone to changing. If code fails use chrome tools to find correct xpath
    inp_xpath = '///*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
    chat_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

    # Send a message
    chat_box.send_keys(msg + Keys.ENTER)

    # Close the browser
    driver.quit()

# Example call
phone_number = "123456789"  # Replace this with your number
message = 'Snow expected tonight, check your email for snow plow reports!' #enter your text message here
send_whatsapp(phone_number, message)