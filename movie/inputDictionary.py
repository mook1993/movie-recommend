import gensim.models as g
import connectDB


def exec():
    cursor = connectDB.exec()   #DB접속

    model_name = "Dictionary/2feat_5minword_3text"
    model = g.Doc2Vec.load(model_name)
    vocab = model.wv.vocab
    X = model[vocab]


    for word in vocab:
        vector=str(list(X[vocab[word].index]))
        cursor.execute("insert into wordDict(word,vector) values('%s', '%s')"%(word, vector))
        cursor.execute("commit")
