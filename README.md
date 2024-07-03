## TF-IDF와 유사도 검색을 활용한 뉴스 추천기 실습

이 레포는 학생들이 중요도 평가, 유사도 검색을 쉽게 이해하고 실습할 수 있도록  
TF-IDF 알고리즘과 코사인 유사도 계산을 사용해  
뉴스 추천기를 만드는 자료가 담긴 레포입니다.

천천히 따라하며 파이썬, 크롤링, 중요도 평가, 유사도 검색의 기초를 배워보세요.

## 프로젝트 목표
- 웹 크롤링을 통해 뉴스 데이터를 수집합니다.
- 수집된 데이터를 전처리하여 TF-IDF으로 어떤 단어들이 중요한지 평가해보고, wordcloud로 시각화합니다.
- 코사인 유사도를 통해 사용자가 현재 보고 있는 기사와 유사한 기사를 추천합니다.

## 라이브러리 설치
```bash
pip install pandas numpy selenium scikit-learn konlpy matplotlib wordcloud
```
  
- Pandas: 데이터 처리를 위해 필요합니다.
- NumPy: 수치 계산을 위해 사용됩니다.
- Selenium: 웹 크롤링을 위한 도구입니다.
- Scikit-learn: TF-IDF 벡터화와 코사인 유사도 계산을 위해 사용됩니다.
- Matplotlib: 결과를 시각화하기 위해 사용됩니다.
- WordCloud: 워드 클라우드 생성을 위해 사용됩니다.

## 디렉토리 구조
- `crawling_data/`: 웹 크롤링을 통해 수집된 뉴스 데이터가 저장되는 폴더입니다.
- `models/`: 훈련된 모델과 토큰화 파일이 저장되는 폴더입니다.
- `stopwords.csv`: 데이터 전처리 시 사용되는 불용어 사전입니다.
- `src/`:
  - `job01_crawling_headline.py`: 네이버 뉴스에서 헤드라인들을 크롤링하는 스크립트
  - `job02_data_cleaned.py`: 크롤링된 데이터들을 정제하는 스크립트
  - `job03_wordcloud.py`: 워드 클라우드를 생성하는 스크립트. 빈도 수 기반
  - `job04_if_idf_wordcloud.py`: IF-IDF 알고리즘으로 워드 클라우드를 생성하는 스크립트
  - `job05_news_recommendation.py`: IF-IDF 기반의 뉴스 추천 스크립트

## 프로젝트 진행 순서
1. Selenium으로 네이버 뉴스의 헤드라인들을 크롤링합니다.
2. 크롤링된 데이터를 정제합니다.
3. 정제된 데이터로 워드 클라우드를 만들어봅니다.
4. TF-IDF로 워드 클라우드를 만들어봅니다.
5. 코사인 유사도 검색 기반의 뉴스 추천기 프로그램을 만듭니니다.

## 참고자료
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [WordCloud Documentation](https://amueller.github.io/word_cloud/)

실제 데이터로 작업해보면 유사도 검색을 쉽게 이해할 수 있습니다. 하나씩 따라해보세요.
