from src import countVec, loadDataset

trainDaset= loadDataset.exec("../data3/*.txt")
countVec.exec(trainDaset)
# word2Vec.exec(trainDaset) #영화 리뷰에 등장한 단어들을 벡터화 하여 단어집으로 저장
#inputDictionary.exec()    #단어집파일의 내용을 DB에 저장
#inputMovieVector.exec(trainDaset)   #영화들을 벡터화하여 DB에 저장
