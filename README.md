# Naver-News-Scraping
Naver News Scraping

# 개요
1.'네이버뉴스' url 추출을 위해 selenium 활용
  - 검색 키워드 encoding을 위한 urllib.parse.qoute 활용 
  - 동적페이지 스크래핑을 위해 javascript 활용 스크롤 구현

2.추출한 url을 통해 BeautifulSoup을 활용해 뉴스기사 추출
  - 기사 본문만 추출
  - 정규표현식, replace(), strip()을 활용한 데이터 정제
  - 작성날짜, 언론사명, 제목, 기사 추출
    
3.데이터 저장
  - dictionay 자료형으로 변환하여 DataFrame으로 변환
  - 최종 excel파일로 저장(최종 결과물 아래 사진)

![image](https://github.com/vornameryuDev/Naver-News-Scraping/assets/164843831/f62c47e8-518a-43c0-aedc-5fd83347cea8)

