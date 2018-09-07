# !/usr/bin/env python
# coding: utf-8
import sys
from sklearn.externals import joblib
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

def build_model(train_path):
    # 读取训练集文件
    train = datasets.load_files(train_path)  # 训练文件

    # 构建Pipeline（管道）
    text_clf = Pipeline([('vect', CountVectorizer(stop_words='english', token_pattern='\w+', max_df=0.7, min_df=2)),
                         ('tfidf', TfidfTransformer(norm ='l2')),
                         ('clf', SVC(kernel='linear', C=5, class_weight='balanced', probability=True)),
                         ])

    # 调用分类器
    text_clf.fit(train.data, train.target)

    # 训练完成之后，使用joblib进行保存
    joblib.dump(text_clf, 'text_clf.m')

if __name__ == "__main__":
    train_path = "/home/machinelearning_workshop/train_output/train"
    build_model(train_path)