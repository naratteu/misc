import time
import csv
import re
from selenium import webdriver

driver = webdriver.Chrome("chromedriver")

with open('주소_전자.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    with open('리스트_전자.txt') as f:
        lines = f.readlines()
        for i, v in enumerate(lines):
            driver.get(v)#"http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListPopup.do?mkt_cd=137103&shop_table=SJTT.MKT_PAPER_SHOP")
            time.sleep(3)
            try:
                lastpage = driver.find_element_by_css_selector("#onnuriShopPopList > table > tbody > tr:nth-child(2) > td > a:last-child")
                lastpageindex = re.search(r'(?<=fnPage\()\d+(?=\);)', lastpage.get_attribute("onclick")).group(0)
            except:
                lastpageindex = 1
            for i in range(1, int(lastpageindex)):
                driver.execute_script("fnPage(%s)" % i)
                time.sleep(3)
                table = driver.find_element_by_css_selector("#onnuriShopPopList > table > tbody > tr:nth-child(1) > td > table")
                for row in table.find_elements_by_css_selector('tr'):
                    wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
