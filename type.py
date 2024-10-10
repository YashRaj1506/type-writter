from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
options.add_argument('--start-maximized')

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# Open the website
driver.get('https://www.monkeytype.com')

# Wait for the page to load
time.sleep(3)

# Accept cookies by clicking the "Accept All" button
accept_button = driver.find_element(By.CLASS_NAME, 'acceptAll')
ActionChains(driver).move_to_element(accept_button).click().perform()

# Allow time for any transitions after accepting cookies
time.sleep(5)

# Locate the 'word active' div which contains the current word
word_active = driver.find_element(By.CLASS_NAME, 'word.active')

# Find all the letter tags inside the active word
letters = word_active.find_elements(By.TAG_NAME, 'letter')

# Check if letters are extracted correctly
if not letters:
    print("No letters found in the active word.")
else:
    # Extract the text from each letter element
    letters_text = ''.join([letter.text for letter in letters])
    print("Extracted Text:", letters_text)

    # Find the body element to send keys
    body = driver.find_element(By.TAG_NAME, 'body')

    # Simulate typing by sending each letter one by one with a small delay
    for letter in letters_text:
        body.send_keys(letter)  # Type each letter individually
        time.sleep(0.1)  # Add a delay between keystrokes

# Pause for a while to see the result
time.sleep(2)

# Close the browser
driver.quit()
