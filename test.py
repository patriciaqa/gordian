from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from time import sleep
from PIL import Image
import cv2
import numpy as np
import sys

#setting browser
url = 'https://static.gordiansoftware.com/'

driver = Chrome()

driver.set_window_size(1366, 768)

driver.get(url)

sleep(2)

def confirm_select_seat():
    try:
        driver.find_element_by_xpath('//*[@id="select-seat"]').click()
    except Exception:
        # if seat is exit row
        painel = driver.find_element_by_id('gordian-overlay')
        if painel.find_element_by_xpath('//*[@id="exit-overlay"]/div/div'):
            driver.find_element_by_id('accept_exit_regulations').click()
        driver.find_element_by_xpath('//*[@id="select-seat"]').click()
    finally:
        driver.find_element_by_xpath('//*[@id="next-button"]').click()


# Seat selection 24B
driver.find_element_by_xpath('//*[@id="gordian-compartments"]/div[7]/div[1]/button[2]').click()
confirm_select_seat()

sleep(2)

# Seat selection 24C
driver.find_element_by_xpath('//*[@id="gordian-compartments"]/div[7]/div[1]/button[3]').click()
confirm_select_seat()

# Screenshot
sleep(3)
driver.execute_script("window.scrollBy(0,768)", "")
sleep(3)
driver.save_screenshot('Seat Selection.png')

sleep(2)

img = cv2.imread('Seat Selection.png')

# Cropping an image
cropped_image = img[420:620, 3:1325]

# Save the cropped image
cv2.imwrite("Seat Selection.png", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

driver.quit()
