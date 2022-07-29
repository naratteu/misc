import time
import csv
import re
import sys
from selenium import webdriver

def main(argv):
    print("파싱실행", argv)
    csv_file = argv[1]
    web_addr = argv[2]
    driver = webdriver.Chrome("chromedriver")

    with open(csv_file, 'w+', newline='') as csvfile:
        wr = csv.writer(csvfile)
        driver.get(web_addr)
        time.sleep(3)
        try:
            lastpage = driver.find_element_by_css_selector("#onnuriShopSrchPopList > table > tbody > tr:nth-child(2) > td > a:last-child")
            lastpageindex = re.search(r'(?<=fnPage\()\d+(?=\);)', lastpage.get_attribute("onclick")).group(0)
            print("페이지카운트", lastpageindex)
        except:
            print("마지막페이지파싱에러나서 페이지카운트 1로")
            lastpageindex = 1
        for i in range(1, int(lastpageindex)):
            #페이지 이동후 대기
            driver.execute_script("fnPage(%s)" % i)
            time.sleep(3)
            #테이블파싱
            table = driver.find_element_by_css_selector("#onnuriShopSrchPopList > table > tbody > tr:nth-child(1) > td > table")
            #cvs에 테이블 적기
            for row in table.find_elements_by_css_selector('tr'):
                wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])

            print("적음(%s/%s)" % (i, lastpageindex))

# module이 아닌 main으로 실행된 경우 실행된다
if __name__ == "__main__":
    try:
        main(sys.argv)
    except:
        print(sys.exc_info())
    finally:
        input('Press Enter to exit')