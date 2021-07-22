from selenium.webdriver import Chrome
from time import sleep
from PIL import Image


url = 'https://static.gordiansoftware.com/'
width = 1291
height = 144
x = 23
y = 1126

driver = Chrome()

driver.set_window_size(1366, 768)

driver.get(url)

sleep(2)

driver.find_element_by_xpath('//*[@id="gordian-compartments"]/div[7]/div[1]/button[2]').click()

driver.find_element_by_xpath('//*[@id="select-seat"]').click()

driver.find_element_by_xpath('//*[@id="next-button"]').click()

sleep(2)

driver.find_element_by_xpath('//*[@id="gordian-compartments"]/div[7]/div[1]/button[3]').click()

driver.find_element_by_xpath('//*[@id="select-seat"]').click()

driver.find_element_by_xpath('//*[@id="next-button"]').click()

sleep(7)

driver.execute_script("window.scrollBy(0,768)", "")

sleep(7)

driver.save_screenshot('Finish Selection.png')

# x = location['x'];
# y = location['y'];
# width = location['x']+size['width'];
# height = location['y']+size['height'];
im = Image.open('Finish Selection.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('Seat Selection.png')

driver.quit()
