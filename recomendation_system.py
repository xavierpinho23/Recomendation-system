# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:53:35 2018

@author: XAVIER

recommentadation system

"""
import open_data
import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from collections import Counter
import math
from sklearn.cluster import AgglomerativeClustering, DBSCAN

def recomend_product(user_id):
    """
    Recomend products based on similar buyers
    """
    #user_id = "A2DG65AWX5RJ4J"
    
    list_of_products = open_data.get_products_of_a_user(user_id) #products bought by the user
    
    L = {}
    
    for product in list_of_products:
        
        users = open_data.get_users_of_a_product(product) #people who bought the same items
        
        for user in users:
            list_of_products_2 = open_data.get_products_of_a_user(user[0]) #products bought for people who had bought the same items
            
            for product_2 in list_of_products_2:
                
                rank = open_data.get_ranking(product_2,user[0]) #get the overall of the product chose by the user
                
                if int(rank)> 3:    #only if it's greater than 3 it's added to the list
                    
                    L[user[1]] = product_2 #dictionary with {user_id : product_id}
                
    return L


a = recomend_product("A2DG65AWX5RJ4J")
print(a)
    
    
                
        
        
        