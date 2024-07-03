import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# 단순히 단어의 등장빈도만으로 wordcloud를 만들어보는 스크립트입니다.

# 데이터 로드
data = pd.read_csv(r'..\crawling_data\naver_news_titles_cleaned20240703.csv')

# 한글 폰트 경로 지정
font_path = "C:\\Windows\\Fonts\\malgun.ttf"

# 단어클라우드 생성 함수
def create_wordcloud(data, title=None):
    wordcloud = WordCloud(
        font_path=font_path,
        background_color='white',
        max_words=200,
        max_font_size=50, 
        scale=3,
        random_state=1
    ).generate_from_frequencies(data)
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    if title: 
        plt.title(title, fontsize=20)

# 모든 기사 제목을 하나의 문자열로 합치기
all_titles = ' '.join(data['Title'])

# 단어 빈도 계산
word_counts = Counter(all_titles.split())

# 전체 데이터에 대한 단어 클라우드 생성 및 저장
plt.figure(figsize=(15, 15))
create_wordcloud(word_counts, title='Top 100 words by frequency')
plt.savefig('../result/top_100_words.png')
plt.close()

# 카테고리별 단어 클라우드 생성 및 저장
categories = data['Category'].unique()
fig, axes = plt.subplots(3, 2, figsize=(20, 30))
axes = axes.flatten()

for i, category in enumerate(categories):
    subset = data[data['Category'] == category]
    subset_titles = ' '.join(subset['Title'])
    subset_word_counts = Counter(subset_titles.split())
    
    plt.sca(axes[i])
    create_wordcloud(subset_word_counts, title=f'Top 100 words by frequency in {category}')

# 레이아웃 조정 및 저장  
plt.tight_layout()
plt.savefig('../result/category_wordclouds.png')
plt.close()