from selenium.webdriver import Chrome
from time import sleep
from PIL import Image
import cv2
import numpy as np

url = 'https://static.gordiansoftware.com/'

driver = Chrome()

# driver.maximize_window()
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

sleep(3)
driver.execute_script("window.scrollBy(0,768)", "")

sleep(3)
driver.save_screenshot('Seat Selection.png')


# element =  driver.find_element_by_id('trigger')
# location = element.location
# size = element.size

sleep(2)
# #to get the x axis
# x = location['x']
# print(x)
# #to get the y axis
# y = location['y']
# print(y)
# # to get the length the element
# height = location['y']+size['height']
# print(height)
# # to get the width the element
# width = location['x']+size['width']
# print(width)

img = cv2.imread('Seat Selection.png')
print(img.shape) # Print image shape
# cv2.imshow("original", img)

# Cropping an image
cropped_image = img[420:620, 3:1325]

# Display cropped image
# cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Seat Selection.png", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

driver.quit()
