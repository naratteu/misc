pushd "%~dp0"
set now=%date%
md %now%
start python "onnuri.py" "%now%/paper.csv" "http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=&shop_table=SJTT.MKT_PAPER_SHOP&city_cd=&txtKey=A.MARKET_NAME&txtParam="
start python "onnuri.py" "%now%/ele.csv" "http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=&shop_table=SJTT.MKT_ELE_SHOP&city_cd=&txtKey=A.MARKET_NAME&txtParam="
start python "onnuri.py" "%now%/mobile.csv" "http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopup.do?cpage=1&county_cd=&shop_table=SJTT.MKT_MOBILE_SHOP&city_cd=&txtKey=A.MARKET_NAME&txtParam="