# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:51:33 2018

@author: Acer
"""
import time
from selenium import webdriver
import random
def main():
    driver=webdriver.Chrome('C:\\Users\\Acer\\Downloads\\chromedriver_win32\\chromedriver')
    driver.get("http://soe.cusat.ac.in/moodle/login/index.php")
    name = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    login = driver.find_element_by_id("loginbtn")
    name.send_keys("12180021") #Just change the value inside "" with whatever you're username is 
    password.send_keys("Qwerty1$") #Just change the value inside "" with whatever you're password is 
    login.click()
#    time.sleep(random.randint(5,10)*1)
#    driver.close()
#    quit()
main()
