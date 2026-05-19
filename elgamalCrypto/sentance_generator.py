from selenium import webdriver
import time
from tqdm import tqdm
import pyperclip


with open('sentence.txt', 'r') as file:
    s = file.readlines()

s = list(set(s))

with open("sentence.txt", 'w') as file:
    for w in s:
        file.write(w)
    

quit()

pyperclip.set_clipboard("xsel")

options = webdriver.ChromeOptions()
options.add_argument("--force-device-scale-factor=0.25")
driver = webdriver.Chrome(options=options)

driver.get("https://www.thewordfinder.com/random-sentence-generator/")
time.sleep(2)
for i in tqdm(range(1000)):
    driver.find_element('xpath', "//button[@class='btn btn-lg btn-success']").click()
    time.sleep(2)
    driver.find_element('xpath', "//a[@id='copyGeneratedSentences']").click()
    time.sleep(0.5)
    text = pyperclip.paste()
    text = text.strip()
    with open("sentence.txt", 'a') as file:
        file.write(text+'\n')

