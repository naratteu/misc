import time
from selenium import webdriver

driver = webdriver.Edge('msedgedriver')
#driver.set_window_size(800,600)
driver.maximize_window()
count = 4

driver.get("https://earth.nullschool.net/ko/#current/particulates/surface/level/overlay=pm2.5/orthographic=-242.68,37.82,1979/loc=127.132,37.659")
time.sleep(4)
driver.execute_script("document.querySelector('#toggle-menu').click()")
time.sleep(4)
driver.save_screenshot('capture/%03d.png' % count)
for i in range(count-1, -1, -1):
	driver.execute_script("document.querySelector('#nav-prev-1').click()")
	time.sleep(4)
	driver.save_screenshot('capture/%03d.png' % i)
driver.quit()