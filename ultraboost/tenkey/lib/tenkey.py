from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

quotes = [
    "Don't worry about what anybody else is going to do. The best way to predict the future is to invent it",
    "The secret to life is to love who you are - warts and all",
    "Today my kitchen is family central. Life happens there",
    "Look for opportunities in every change in your life",
    "The light heart lives long",
    'The story of life is quicker than the wink of an eye',
    "Life really does begin at forty. Up until then, you are just doing research",
    "Life is a question and how we live it is our answer",
    "Accept life as it is. Then work to make it the way you want it to be",
    "Parenting is a lifetime assignment",
    "Life is accepting what is and working from that",
    "Life is a long lesson in humility",
    "Persist while others are quitting",
    "Where there is love there is life",
    "Mornings contain the secret to an extraordinarily successful life.",
    "Little decisions you make alter your life, but they rarely do so all at once"
    "There is no life as complete as the life that is lived by choice",
    "Everyone's life is a fairy tale, written by God's fingers"
]

timeout = [
    5
]

driver = webdriver.Firefox(executable_path='path/to/geckodriver')
driver.get("url/to/comment")
username = driver.find_element_by_name("email")
username.send_keys("email_login")
pw = driver.find_element_by_name("pass")
pw.send_keys("pw")
pw.send_keys(Keys.RETURN)
time.sleep(10)
count = 0
while count < 200:
    print(count)
    actions = ActionChains(driver)
    msg = random.choice(quotes)
    actions.send_keys(msg)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    timer = random.choice(timeout)
    time.sleep(timer)
    count += 1
driver.close()
