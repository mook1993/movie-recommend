import gensim.models as g
import pandas as pd
from gensim.models import word2vec
from sklearn.manifold import TSNE
from word2VecUtility import Word2VecUtility


def exec(train_dataSet):
    # 불용어 제거, 특정품사만 허용
    passtag = ['Noun']
    stopwords = set(['최고', '정말', '역시', '진짜', '영화', '시리즈', '명작', '마지막', '편이',
                     '마무리', '너무', '시대', '지금', '재미', '보고', '모두', '부작', '제일',
                     '가장', '편도', '약간', '다시', '느낌', '편의', '생각', '별로', '조금', '하다',
                     '보다', '되다', '만들다', '재밌다', '전작', '전편', '속편', '원작'])
    password = set(['감동', '슬픔', '웃김', '웃기다', '배꼽', '눈물', '공포', '무섭다',
                    '무섭', '지렸다', '지림', '먹먹', '아련', '저리다', '괴물', '유령'])

    clean_train = []   #모든 영화의 리뷰가 문장단위로 토큰화 되어 저장, [[stat1 tok], [stat2 tok], ...]
    for movie in train_dataSet:
        for sentence in movie["content"]:
            clean_train.extend(Word2VecUtility.review_to_sentences(sentence, withPoomsa=False))

    print(clean_train)

    # 파라메터값 지정
    num_features = 2  # 문자 벡터 차원 수
    min_word_count = 5  # 최소 문자의 빈도 수
    num_workers = 4  # 병렬 처리 스레드 수
    context = 3  # 문자열 창 크기
    downsampling = 10  # 문자 빈도 수 Downsample

    # 리뷰에 등장한 모든 단어를 벡터화, 서로 유사한 단어끼리는 유사한 값을 가지게 된다.
    model = word2vec.Word2Vec(clean_train, #리스트, ["","","",""...]
                              workers=num_workers,
                              size=num_features,
                              min_count=min_word_count,
                              window=context,
                              sample=downsampling)
    model.init_sims(replace=True)


    model_name = "Dictionary/2feat_5minword_3text"
    model.save(model_name)

    model = g.Doc2Vec.load(model_name)
    vocab = list(model.wv.vocab)
    print(vocab)

    #단어벡터 내용
    X = model[vocab]
    tsne = TSNE(n_components=2)  # 단어를 표현할 벡터의 차원은 2차원
    X_tsne = tsne.fit_transform(X[:100, :])  # 100개의 단어에 대해서만 벡터화, 각 단어별 벡터화정보 저장(i행에는 vocab[i]에 해당하는 단어의 벡터정보가 담겨있음)
    df = pd.DataFrame(X_tsne, index=vocab[:100], columns=['x', 'y'])
    print('Data Frame------')
    print(df)


    # mpl.rcParams['axes.unicode_minus'] = False
    # font_name=font_manager.FontProperties(fname="font/malgun.ttf").get_name()
    # rc('font', family=font_name)
    # fig = plt.figure()
    # fig.set_size_inches(40, 20)
    # ax = fig.add_subplot(1, 1, 1)
    # ax.scatter(df['x'], df['y'])
    # 
    # for word, pos in df.iterrows():
    #     ax.annotate(word, pos, fontsize=30)
    # plt.show()

if __name__ == "__main__":
    exec()


