# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:27:12 2018

@author: XAVIER

open dataset for Musical Instruments Reviews
"""
import pandas as pd
import numpy as np
import gzip
import csv
import os

print("------- Importation Complete ----------")
home = os.getcwd()
os.chdir(home)

def parse(path): 
    g = gzip.open(path, 'rb') 
    for l in g: 
        yield eval(l) 
    
def getDF(path): 
    i = 0 
    df = {} 
    for d in parse(path): 
        df[i] = d 
        i += 1 
    return pd.DataFrame.from_dict(df, orient='index')   

def get_all_dataset():
    col_Names=["reviewerID", "asin", "rating", "unixReviewTime"]
    df = pd.read_csv(path+"ratings_Musical_Instruments.csv", encoding = "utf-8", engine='python',names=col_Names)
    return df

def get_user_and_instrument_and_review_id():
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        list_review=[]
        for line in reader:
            list_review.append([line[2], line[1], line[8]])  #product_id, user_id and review_id
        return list_review

def get_all_users():
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        list_users = []
        for line in reader:
            list_users.append(line[2])
    return np.unique(list_users)

def get_users_of_a_product(product_id):
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        list_users = []
        for line in reader:
                if line[2] == product_id:
                    list_users.append(line[3])
    return np.unique(list_users)


def get_products_of_a_user(user_id):
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        list_movies = []
        for line in reader:
                if line[1] ==  user_id:
                    list_movies.append(line[2])
    return list_movies


def get_review(product_id, user_id):
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        for line in reader:
                if line[2] == product_id:
                    if line[1] == user_id:
                        return line[5]

#def get_dict_users_products():
#    d = {}
#    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
#        reader = csv.reader(musical_instrument_file)
#        for line in reader:
#            d[line[3]] = get_products_of_a_user(line[3])
#    return d

def get_text_reviews_and_id():
    reviews = []
    ids_reviews = []
    with open(path+'Reviews_Musical_Instruments.csv', 'r') as musical_instrument_file:
        reader = csv.reader(musical_instrument_file)
        for i in reader:
            reviews.append(i[5])  # last but one index
            ids_reviews.append(i[8]) #last index
    return reviews, ids_reviews

def open_opinion_lexicon_neg():
    list_neg = []
    with open(path+'opinion-lexicon-English/negative-words.txt', 'r') as opinion_lexicon_file:
        reader = csv.reader(opinion_lexicon_file)
        for i in reader:
            list_neg.append(i[0])
    return list_neg


def open_opinion_lexicon_pos():
    list_pos = []
    with open(path+'opinion-lexicon-English/positive-words.txt', 'r') as opinion_lexicon_file:
        reader = csv.reader(opinion_lexicon_file)
        for i in reader:
            list_pos.append(i[0])
    return list_pos

path = "C:/Users/XAVIER/Desktop/4º Ano - 1º Semestre/Inteligência Artificial/RecomendationSystem/Recomendation-system/"

#Function's tests

df = getDF(path+'reviews_Musical_Instruments_5.json.gz')
dfx =df.head()
df.to_csv(path+"Reviews_Musical_Instruments.csv")

df1 = get_all_dataset()
df1x = df1.head()

lista1 = get_users_of_a_product(product_id = 'B00004Y2UT')

lista2 = get_user_and_instrument_and_review_id()

lista3 = get_products_of_a_user(user_id = "A2IBPI20UZIR0U")

lista4 = get_review(product_id = '1384719342', user_id = "A2IBPI20UZIR0U")

#lista5 = get_dict_users_products()

lista6, lista7 = get_text_reviews_and_id()

lista8 = open_opinion_lexicon_neg()

lista9 = open_opinion_lexicon_pos()
