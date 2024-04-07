from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import requests




def get_soup(url):
	res = requests.get(url)
	soup = bs(res.content, 'html.parser')
	return soup

def get_naver_news(all_links):
	naver_links = []
	for link in all_links:
		href = link.get_attribute('href')	
		if "n.news.naver" in href:
			naver_links.append(href)
		else:
			pass
	return naver_links

def find_elements_css(driver, tag_and_class):
	element_list = driver.find_elements(By.CSS_SELECTOR, tag_and_class)
	return element_list

def scroller(driver):
	last_height = driver.execute_script('return document.body.scrollHeight') 
	while True:
		driver.execute_script(f'return window.scrollTo(0, {last_height})') #스크롤
		time.sleep(0.5)
		new_height = driver.execute_script('return document.body.scrollHeight') #높이 다시산출		
		if new_height == last_height:
			print('스크롤 완료')
			break
		last_height = new_height


