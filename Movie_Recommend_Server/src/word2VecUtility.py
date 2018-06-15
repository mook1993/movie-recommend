# 데이터셋을 전처리하기 위한 유틸리티

import re
from multiprocessing import Pool
import nltk
import numpy as np
import pandas as pd
from konlpy.tag import Twitter


class Word2VecUtility(object):

    @staticmethod   #한 문장을 토큰화 해서 반환
    def review_to_wordlist(setence, stopwords=set([]), passwords=set([]), withPoomsa=True):
        passtag = ['Noun','Adjective']  #명사만 고려
        clean_sentence = re.sub('[!|<|>|?|:|.|,]', ' ', str(setence))   # 특수 기호 제거
        twt=Twitter()
        tokenize = lambda sentence: twt.pos(sentence, norm=True, stem=True)  # 스테밍 처리 후 토큰화
        tokens = tokenize(clean_sentence)  # [list], train_tokens[i]는 i번째 문서의 리뷰에 대한 단어/품사 정보가 들어있음

        if(len(passwords)==0):
            if not withPoomsa:
                return [w[0] for w in tokens if not w[0] in stopwords and w[1] in passtag]
            words = [w for w in tokens if not w[0] in stopwords and w[1] in passtag]
            return(words)
        else:
            if not withPoomsa:
                return [w[0] for w in tokens if w[0] in passwords and w[1] in passtag]
            words = [w for w in tokens if w[0] in passwords and w[1] in passtag]
            return(words)

    @staticmethod
    def review_to_join_words( review, remove_stopwords=False ):
        words = Word2VecUtility.review_to_wordlist(\
            review, remove_stopwords=False)
        join_words = ' '.join(words)
        return join_words

    @staticmethod   #결과값은 문장단위로 토큰화된 리스트, 토큰은 (단어, 품사)의 형태
    def review_to_sentences(review, stopwords=[], passwords=[], withPoomsa=True ):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        # 1. nltk tokenizer를 사용해서 단어로 토큰화 하고 공백 등을 제거한다.
        raw_sentences = tokenizer.tokenize(review.strip())
        # 2. 각 문장을 순회한다.
        sentences = []
        for raw_sentence in raw_sentences:
            # 비어있다면 skip
            if len(raw_sentence) > 0:
                # 문장을 토큰화한 결과 리스트를 append
                sentences.append(Word2VecUtility.review_to_wordlist(raw_sentence, stopwords=stopwords, passwords=passwords, withPoomsa=withPoomsa))
        return sentences


    # 참고 : https://gist.github.com/yong27/7869662
    # http://www.racketracer.com/2016/07/06/pandas-in-parallel/
    # 속도 개선을 위해 멀티 스레드로 작업하도록
    @staticmethod
    def _apply_df(args):
        df, func, kwargs = args
        return df.apply(func, **kwargs)

    @staticmethod
    def apply_by_multiprocessing(df, func, **kwargs):
        # 키워드 항목 중 workers 파라메터를 꺼냄
        workers = kwargs.pop('workers')
        # 위에서 가져온 workers 수로 프로세스 풀을 정의
        pool = Pool(processes=workers)
        # 실행할 함수와 데이터프레임을 워커의 수 만큼 나눠 작업
        result = pool.map(Word2VecUtility._apply_df, [(d, func, kwargs)
                for d in np.array_split(df, workers)])
        pool.close()
        # 작업 결과를 합쳐서 반환
        return pd.concat(result)