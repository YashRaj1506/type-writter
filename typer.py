from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument('--start-maximized') 


driver = webdriver.Chrome(options=options)


driver.get('https://www.monkeytype.com')  


time.sleep(3) 

accept_button = driver.find_element(By.CLASS_NAME, 'acceptAll')

# Click the "Accept All" button
ActionChains(driver).move_to_element(accept_button).click().perform()


# time.sleep(5)

word_active = driver.find_element(By.CLASS_NAME, 'word.active')

# Find all the letter tags inside it
letters = word_active.find_elements(By.TAG_NAME, 'letter')

letters_text = ''.join([letter.text for letter in letters])
print("Extracted Text:", letters_text)

body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(letters_text)

time.sleep(2)
# Close the browser
driver.quit()
