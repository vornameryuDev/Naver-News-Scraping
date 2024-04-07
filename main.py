from urllib import parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

from inspectors import find_elements_css, get_naver_news, get_soup, scroller

import time
import pandas as pd


#keyword and date (test)
search_keyword = "촉법소년"
encoded_keyword = parse.quote(search_keyword) #검색어 encoding
start_date = "2024.01.01"
end_date = "2024.01.31"

#kewyword and date (real)
# search_keyword = input("검색어입력: ")
# start_date = input("검색 시작 날짜(yyyy.mm.dd.로 입력): ")
# end_date = input("검색 종료 날짜(yyyy.mm.dd로 입력) ")
# encoded_keyword = parse.quote(search_keyword) #검색어 encoding

url = f"https://search.naver.com/search.naver?where=news&query={encoded_keyword}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={start_date}&de={end_date}"

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#드라이버 실행
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)
driver.get(url)

time.sleep(1)

#스크롤
scroller(driver)

#네이버뉴스링크 얻기
a_links = find_elements_css(driver, 'a.info') #모든 링크 얻기
naver_links = get_naver_news(a_links) #네이버 뉴스만 추리기

news_info_list = []
for url in naver_links:
	news_info_dict = {}
	print(url)
	soup = get_soup(url) #soup 얻기
	try:
		company = soup.select_one("em.media_end_linked_more_point") #신문사
		date = soup.select_one("span.media_end_head_info_datestamp_time._ARTICLE_DATE_TIME") #작성일자
		title = soup.select_one("#title_area") #기사제목
		article = soup.select_one("#dic_area") #기사내용	
		if article.find("strong") == None: # strong 없으면
			if article.find("span") == None: #span 없으면
				pass
			else: #span 있으면
				article.find("span").decompose() #span tag 삭제
		else: #strong 있으면
			if article.find("span"): #span 있으면
				article.find('span').decompose()
			article.find('strong').decompose()

		# 딕셔너리 저장
		news_info_dict["url"] = url
		news_info_dict["date"] = date.get_text().split(" ")[0]
		news_info_dict["company"] = company.get_text()
		news_info_dict["title"] = title.get_text()
		news_info_dict["article"] = article.get_text().strip().replace("\n", "").replace("\t", " ")

		#리스트에 저장
		news_info_list.append(news_info_dict) #리스트에 저장
		
	except Exception as error:
		print(error)
		pass

# 데이터프레임화 및 저장
df = pd.DataFrame(news_info_list)
print(df.head())

df.to_excel("naver_news_scraping_test.xlsx") #엑셀파일 저장



	






	















