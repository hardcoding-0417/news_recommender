import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Tf-idf Vectorizer로 벡터화한 뒤,
# 벡터간 내적 계산으로 코사인 유사도를 도출하여
# 지금 내가 보고 있는 문서와 흡사한 문서를 추천해주는 실습입니다.

# 데이터 로드
data = pd.read_csv(r'../crawling_data/naver_news_titles_cleaned20240703.csv')

# tf-idf 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Title'])

# 코사인 유사도 계산 함수
def get_recommendations(title, top_n=5):
    # 입력된 제목의 tf-idf 벡터 계산
    title_tfidf = vectorizer.transform([title])
    
    # 모든 기사와의 코사인 유사도 계산
    cos_similarities = cosine_similarity(title_tfidf, tfidf_matrix).flatten()
    
    # 유사도가 높은 기사의 인덱스 추출
    related_docs_indices = cos_similarities.argsort()[::-1][:top_n]
    
    # 추천 기사 반환
    return data.iloc[related_docs_indices]

sample_title = data['Title'][3333]  # 현재 보고 있는 기사
print(f"관심 기사: {sample_title}")
print("추천 기사:")
print(get_recommendations(sample_title))

# TfidfVectorizer를 CountVectorizer로 바꿔서 시도해보세요.