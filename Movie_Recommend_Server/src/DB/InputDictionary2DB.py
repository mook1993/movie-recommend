# 딕셔너리 파일의 데이터셋들을 DB에 저장

import gensim.models as g
from src.DB import connectDB


def exec():
    cursor = connectDB.exec()   #DB접속

    model_name = "../../vector_files/2feat_5minword_3text"
    model = g.Doc2Vec.load(model_name)
    vocab = model.wv.vocab
    X = model[vocab]


    for word in vocab:
        vector=str(list(X[vocab[word].index]))
        cursor.execute("insert into wordDict(word,vector) values('%s', '%s')"%(word, vector))
        cursor.execute("commit")
