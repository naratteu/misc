import time
from selenium import webdriver

driver = webdriver.Chrome("chromedriver") #Edge('msedgedriver')

driver.get("http://www.sbiz.or.kr/sijangtong/nation/onnuri/onnuriMktList.do")
time.sleep(2)

onnuriList = driver.find_element_by_id("onnuriList")

# 종이상품권
tab = driver.find_element_by_id("paperBtn")
tab.click()
time.sleep(1)
for i in range(1,35):
    driver.execute_script("fnPage(" + str(i) + ")")
    #print("#","fnPage(" + str(i) + ")")
    time.sleep(1)
    shopPopBtn = onnuriList.find_elements_by_class_name("shopPopBtn")
    for v in shopPopBtn:
        mktcd = v.get_attribute("mktcd")
        print("http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListPopup.do?mkt_cd=%s&shop_table=%s" % (mktcd, "SJTT.MKT_PAPER_SHOP"))

# 전자상품권
tab = driver.find_element_by_id("eleBtn")
tab.click()
time.sleep(1)
for i in range(1,35):
    driver.execute_script("fnPage(" + str(i) + ")")
    #print("#","fnPage(" + str(i) + ")")
    time.sleep(1)
    shopPopBtn = onnuriList.find_elements_by_class_name("shopPopBtn")
    for v in shopPopBtn:
        mktcd = v.get_attribute("mktcd")
        print("http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListPopup.do?mkt_cd=%s&shop_table=%s" % (mktcd, "SJTT.MKT_ELE_SHOP"))

# 모바일상품권
tab = driver.find_element_by_id("mobileBtn")
tab.click()
time.sleep(1)
for i in range(1,35):
    driver.execute_script("fnPage(" + str(i) + ")")
    #print("#","fnPage(" + str(i) + ")")
    time.sleep(1)
    shopPopBtn = onnuriList.find_elements_by_class_name("shopPopBtn")
    for v in shopPopBtn:
        mktcd = v.get_attribute("mktcd")
        print("http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListPopup.do?mkt_cd=%s&shop_table=%s" % (mktcd, "SJTT.MKT_MOBILE_SHOP"))
