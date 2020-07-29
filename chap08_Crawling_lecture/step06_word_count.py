'''
1. pickle file load
2. 텍스트 전처리
3. word count
'''
import pickle


# 1-1) pickle file load
file = open('./chap08_Crawling/data/new_crawling.pickle', mode='rb')
news_crawling = pickle.load(file)
print(type(news_crawling)) # <class 'list'>
print(news_crawling)

# 1-2) 텍스트 전처리
def clean_text(texts) :
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)
    # 5. 공백 제거
    texts_re5 = ' '.join(texts_re4.split())

    return texts_re5

clean_news = [clean_text(news) for news in news_crawling]
print(clean_news)

# 1-3) word count
word_count = {} # 빈 set
for text in clean_news:
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# 1-4) 2음절 이상 단어 선택
word_count2 = word_count.copy() # 객체 복제
for word in word_count.keys(): # key값만 넘기겠다
    if len(word) < 2:
        del word_count2[word]
print(word_count2)
print(type(word_count2)) # <class 'dict'>

# 1-5) top10, top5
''' pip install collections-extended '''
from collections import Counter
count = Counter(word_count2)
# 필요없는말 제거
del count['none']
del count['[바로잡습니다]']
top5 = count.most_common(5)
print(top5)
top10 = count.most_common(10)
print(top10)

# 1-6) list[(),()] -> DataFrame
import pandas as pd
top10_df = pd.DataFrame(top10, columns=['word', 'count'])
print(top10_df)

# 1-7) 한글폰트 지원
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 1-7) 시각화 (선)
''' pip install matplotlib '''
import matplotlib.pyplot as plt
plt.plot(top10_df['word'], top10_df['count']) # 앞 x축, 뒤 y축
plt.title('top10 word count')
plt.show()

# 1-9) 시각화 (막대)
plt.bar(top10_df['word'], top10_df['count'])
plt.title('top10 word count')
plt.show()


