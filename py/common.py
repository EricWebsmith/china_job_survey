# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:44:37 2019

@author: eric
"""
import inspect

def is_letter_english(letter):
    return ord(letter)<=126

def is_article_english(article):
    english_letters=sum(list(map(is_letter_english,list(article))))
    length=len(article)
    percentage=100*english_letters/length
    return percentage>80

def get_featurenames(o):
    #python reflection
    dictionary=inspect.getmembers(o)
    feature_names=[t[0] for t in  dictionary if not t[0].startswith("__") and not t[0].startswith("get_") and not t[0].startswith("check_")]
    return feature_names

def object2list(job):
    dictionary=inspect.getmembers(job)
    l=[]
    for key, value in dictionary:
        if key.startswith('__') or key.startswith('get_') or key.startswith('check_'):
            continue
        l.append(value)
    return l
        
def object2dict(o):
    dictionary=inspect.getmembers(o)
    d={}
    for key, value in dictionary:
        if key.startswith('__'):
            continue
        d[key]=value
    return d