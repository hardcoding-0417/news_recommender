import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# if-idf로 중요한 단어만 wordcloud로 만들어보는 실습입니다.

# 데이터 로드
data = pd.read_csv(r'..\crawling_data\naver_news_titles_cleaned20240703.csv')

# tf-idf 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Title'])

# tf-idf 점수를 데이터프레임으로 변환
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

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

# 전체 데이터에 대한 단어 클라우드 생성
tfidf_top100 = tfidf_df.sum().sort_values(ascending=False).head(100)
print(tfidf_top100.head(5)) 

plt.figure(figsize=(15, 15))
create_wordcloud(dict(tfidf_top100), title='Top 100 words by TF-IDF')
plt.savefig('../result/top_100_words_by_if_idf.png')
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
    create_wordcloud(subset_word_counts, title=f'Top words by tf-idf in {category}')

# 레이아웃 조정 및 저장
plt.tight_layout()
plt.savefig('../result/category_wordclouds_by_if_idf.png')
plt.close()
