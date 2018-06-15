import pickle

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

from src.word2VecUtility import Word2VecUtility


def exec(train_dataSet):
    clean_train = []   #각 영화별로 모든 영화의 리뷰가 문장단위로 토큰화 되어 저장, [[0번째 영화], [1번째 영화], ...]
    passwords = ['감동', '웃기', '웃김', '눈물', '펑펑', '슬프', '슬펐', '먹', '꿀잼', '존잼', '사랑스럽']
    stopwords = ['영화']

    for movie in train_dataSet:
        movie_train=[]
        for sentence in movie["content"]:
            movie_train.extend(Word2VecUtility.review_to_sentences(sentence, withPoomsa=False, stopwords=stopwords))
        clean_train.append(movie_train)

    # print(clean_train)
    # print(len(clean_train))
    # 각 영화에서 가장 빈번하게 등장하는 핵심 키워드를 추출하여 반환(tfid)
    vectorizer = CountVectorizer(analyzer='word',
                                 tokenizer=None,
                                 preprocessor=None,
                                 stop_words=None,
                                 min_df=2,  # 토큰이 나타날 최소의 문서 개수
                                 ngram_range=(1, 1),  # 하나의 토큰은 단어가 1개~3개인 것으로 구성
                                 max_features=5000  # 토큰의 갯수는 최대 2만개
                                )
    pipeline = Pipeline([
        ('vect', vectorizer),
        ('tfidf', TfidfTransformer(smooth_idf=True)),
    ])


    # [list] CountVectorizer에 적용할수 있도록 알맞게 변환 ("0번째 영화에 등장 단어들","~~~~","~~~~") 와 같은 형태
    train_formatted=[]
    for movie_ele in clean_train:
        tmpStr=""
        for state in movie_ele:
            tmpStr+=(" ".join(state)+" ")
        train_formatted.append(tmpStr)


    train_freq_featList=pipeline.fit_transform(train_formatted)    #각 영화별 리뷰의 단어빈도수를 구함
    vocab=vectorizer.get_feature_names()


    #각각의 단어들의 빈도수를 피클파일로 저장
    pickle.dump(vectorizer.vocabulary_,open("../../vector_files/freq_vaca.pkl","wb"))  #각 단어와 그 단어의 인덱스 저장
    # with open('freq_vaca.pkl','rb') as f:
    #     a=pickle.load(f)


    print('-------Freq words-------')
    # [Array] 각 영화의 리뷰마다 가장 비번하게 등장하는 단어순으로 인덱스 정렬
    train_freq_featArr=train_freq_featList.toarray()
    sorted_voca=np.argsort(-train_freq_featArr)
    keyWords=lambda docInd:[[vocab[ind],train_freq_featArr[docInd][ind]] for ind in sorted_voca[docInd]]  # [Array]
    keyWords_eachMovie=[keyWords(i) for i in range(0,train_freq_featArr.shape[0])]
    # for i in range(0,9):
    #     print(train_dataSet[i]['title'][0],'---->',keyWords_eachMovie[i][:5])

    #미리 학습시켜놓은 단어사전 로드
    import gensim.models as g
    model_name = "../../vector_files/2feat_5minword_3text"
    model = g.Doc2Vec.load(model_name)
    vocab = model.wv.vocab
    X = model[vocab]
    # from sklearn.manifold import TSNE
    # tsne = TSNE(n_components=2)  # 단어를 표현할 벡터의 차원은 2차원
    # X_tsne = tsne.fit_transform(X)  # 100개의 단어에 대해서만 벡터화, 각 단어별 벡터화정보 저장(i행에는 vocab[i]에 해당하는 단어의 벡터정보가 담겨있음)

    vect=[]
    #각 영화의 feat를 2차원 벡터로 축소 (등장하는 단어빈도 * 해당단어의 벡터값)
    compactedInfos=[]
    for mv_Ind in range(0, len(keyWords_eachMovie)):
        sum=0
        cnt=0
        if len(train_dataSet[mv_Ind])==0:
            continue
        for w_Ind in range(1,100):
            word=keyWords_eachMovie[mv_Ind][w_Ind]
            if(word[0] in vocab):
                sum+=word[1] * X[vocab[word[0]].index]
                cnt=cnt+1
        mv_code=train_dataSet[mv_Ind]['code'][0]
        mv_title=train_dataSet[mv_Ind]['title'][0]
        mv_vector=sum/cnt
        vect.append(mv_vector)
        compactedInfos.append((int(mv_code),str(mv_title),list(mv_vector)))

    pickle.dump(compactedInfos, open("../../vector_files/movie_vector.pkl", "wb"))
    # # 각 영화간의 거리를 시각화
    # import matplotlib as mpl
    # from matplotlib import pyplot as plt
    # from matplotlib import font_manager, rc
    # #titleList=[train_dataSet[i]["title"][0] for i in range(0,len(train_dataSet))]
    # titleList=[]
    # for i in range(0,len(compactedInfos)):
    #     print(i)
    #     titleList.append(compactedInfos[i][1])
    #
    # df = pd.DataFrame(vect, index=titleList, columns=['x', 'y'])
    # mpl.rcParams['axes.unicode_minus'] = False
    # font_name=font_manager.FontProperties(fname="font/malgun.ttf").get_name()
    # rc('font', family=font_name)
    # mpl.rcParams.update({'font.size':10})
    #
    # fig = plt.figure()
    # fig.set_size_inches(40, 20)
    # ax = fig.add_subplot(1, 1, 1)
    # ax.scatter(df['x'], df['y'])
    #
    # for word, pos in df.iterrows():
    #     ax.annotate(word, pos, fontsize=30)
    # plt.show()

    return compactedInfos