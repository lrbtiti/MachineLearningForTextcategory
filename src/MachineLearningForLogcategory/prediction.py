# !/usr/bin/env python
# coding: utf-8
import sys, re, os
from sklearn.externals import joblib
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import heapq
import numpy as np


class Prophesy(object):

    def predict(self):
        pass


@click.command()
@click.option('--file_path', required=True, help='the prdict datas full path.')
@click.option('--model_path', required=True, help='the useable model path.')
def predict_result(file_path, model_path):
    test_datas = DataSet(file_path)
    text_clf = joblib.load(model_path)
    docs_test = test_datas.data
    predicted = text_clf.predict(docs_test)  # 预测类型的索引
    predict_proba = text_clf.predict_proba(docs_test) # 预测类型的概率
    test_counts = predict_proba.shape[0]  # 测试集的总数
    threshold = 0.6
    for i in range(test_counts):
        every_proba = predict_proba[i].tolist()
        max_proba = max(every_proba)
        max_proba_index = every_proba.index(max_proba) # 概率最大的索引
        file_name = test.filenames[i].split('/')
        if every_proba[max_proba_index] > threshold: # 输出概率大于阈值
            train.target_names[predicted[i]]
            result_to_db(file_name[-1], class_id)


if __name__ == "__main__":
    predict_result()