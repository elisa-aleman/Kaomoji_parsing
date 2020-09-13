#-*- coding: utf-8 -*-

import os
import pathlib

#######################
######## Paths ########
#######################

def make_log_file(filename):
    '''
    Make Log file path string
    '''
    halfpath = os.path.join(os.path.dirname(os.getcwd()), 'logs')
    fullpath = os.path.join(halfpath, filename)
    file_parent = fullpath.rsplit("/",1)[0]+"/"
    pathlib.Path(file_parent).mkdir(parents = True, exist_ok=True)
    return fullpath

def make_data_path(filename):
    '''
    Make Data file path string
    '''
    halfpath=os.path.join(os.path.dirname(os.getcwd()), 'data')
    fullpath = os.path.join(halfpath, filename)
    file_parent = fullpath.rsplit("/",1)[0]+"/"
    pathlib.Path(file_parent).mkdir(parents = True, exist_ok=True)
    return fullpath

def make_keyword_path(filename):
    '''
    Make Keyword file path string
    '''
    halfpath = os.path.join(os.path.dirname(os.getcwd()), 'keywords')
    fullpath = os.path.join(halfpath, filename)
    file_parent = fullpath.rsplit("/",1)[0]+"/"
    pathlib.Path(file_parent).mkdir(parents = True, exist_ok=True)
    return fullpath

def make_model_path(filename):
    '''
    Make Model file path string 
    '''
    halfpath= make_data_path('models')
    fullpath = os.path.join(halfpath, filename)
    file_parent = fullpath.rsplit("/",1)[0]+"/"
    pathlib.Path(file_parent).mkdir(parents = True, exist_ok=True)
    return fullpath

if __name__ == '__main__':
    pass