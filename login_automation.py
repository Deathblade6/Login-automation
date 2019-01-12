#you  must have the chroome driver in your PATH.
from selenium import webdriver
import pickle
import sys


driver=webdriver.Chrome()
driver.get("http://soe.cusat.ac.in/moodle/login/index.php")
usr_name_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
login_btn = driver.find_element_by_id("loginbtn")
usr_name_field.send_keys("_insert_your_username")#Just change the value inside "" with whatever you're username is 
password_field.send_keys("_insert_your_password")#Just change the value inside "" with whatever you're password is 
login_btn.click()

driver.get("http://soe.cusat.ac.in/moodle/course/view.php?id=6")
latest_update = driver.find_element_by_id("section-0")
htmlString = latest_update.get_attribute('innerHTML')

try: 
    file = pickle.load( open( 'source.p', 'rb'))
    if file == htmlString:
        print("Values haven't changed!")
        sys.exit(0)
    else:
        pickle.dump( htmlString, open( 'source.p', "wb" ) )  
        print('Saving')
except IOError: 
    pickle.dump( htmlString, open( 'source.p', "wb" ) )
    print('Created new file.')


