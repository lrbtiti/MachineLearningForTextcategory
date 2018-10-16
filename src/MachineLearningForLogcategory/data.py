# !/usr/bin/env python
# coding: utf-8

from sklearn import datasets


class DataSet(object):

    def __init__(self, data_path):
        self._data_sets = datasets.load_files(data_path)
    
    @property
    def data(self):
        return self._data_sets.data

    @property
    def category_ids(self):
        return self._data_sets.target

    @property
    def category_names(self):
        return self._data_sets.target_names

    @property
    def file_names(self):
        return self._data_sets.filenames

