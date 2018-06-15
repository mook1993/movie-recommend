import pickle
import sys
import gensim.models as g
import numpy as np
from konlpy.tag import Twitter


def getRecommendMovie(data=""):
    # integra = mood + ' ' + etc
    integra = data

    twt = Twitter()
    tokens = twt.pos(integra)
    passtag = ['Noun', 'Adjective']
    keywords = [w[0] for w in tokens if w[1] in passtag]

    model_name = "../../vector_files/2feat_5minword_3text"
    model = g.Doc2Vec.load(model_name)
    vocab = model.wv.vocab

    cnt = 0
    sum = np.asarray([0., 0.])
    for word in keywords:
        if word not in set(vocab):
            continue
        sum += model[word]
        cnt += 1

    userVec = (sum / cnt) if cnt!=0 else 0

    with open('../../vector_files/movie_vector.pkl', 'rb') as f:
        movies = pickle.load(f)

    minDiff = sys.maxsize
    recommendMovie = movies[0]
    for movie in movies:
        a = np.asarray(userVec)
        b = np.asarray(movie[2])
        diff = np.linalg.norm(np.sum((a - b) ** 2, axis=0))
        if (diff < minDiff):
            recommendMovie = movie
            minDiff=diff
    # print(recommendMovie)
    return recommendMovie


getRecommendMovie()