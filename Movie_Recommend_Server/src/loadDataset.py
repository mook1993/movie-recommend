#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 데이터셋 읽어옴
import glob
import pandas as pd

def exec(path):
    allFiles=glob.glob(path)
    train_dataSet=pd.DataFrame(pd.read_csv(f,header=0, sep='|', quoting=3, error_bad_lines=False) for f in allFiles) #[DataFrame] 모든 훈련데이터 로드
    train_dataSet=train_dataSet[0]  #train_dataSet[i]에는 i번째 영화의 리뷰정보가 있음
    return train_dataSet


if __name__ == "__main__":
    exec()

