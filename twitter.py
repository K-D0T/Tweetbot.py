from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import getpass

username = input("Type your username: ")
password = getpass.getpass("Type your password... dont worry its safe: ")
tweet = input("Type up a tweet: ")

driver = webdriver.Chrome(executable_path='/Users/K-Dot/Environment/my_env/lib/python3.7/site-packages/chromedriver')

start = time.time()

driver.get("https://twitter.com/")


usr = '//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/div[1]/input'
uname = driver.find_element_by_xpath(usr)
uname.click()
uname.send_keys(username)

psw = '//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/div[2]/input'
passw = driver.find_element_by_xpath(psw)
passw.click()
passw.send_keys(password)

log = '//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/input[1]'
lin = driver.find_element_by_xpath(log)
lin.click()

btn = '//*[@id="global-new-tweet-button"]'
bttn = driver.find_element_by_xpath(btn)
bttn.click()

twt = '//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]'
twtt = driver.find_element_by_xpath(twt)
twtt.click()
twtt.send_keys(tweet)

tweetbutton = '//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[2]/span/button[2]'
twb = driver.find_element_by_xpath(tweetbutton)
twb.click()

end = time.time()

print("Would ya look at that it only took", end - start, "seconds to tweet!")