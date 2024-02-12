from django.db import models
from urllib.parse import urlparse

# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    
    class Meta:
        app_label = 'app'
    
    def __str__(self):
        return self.title

def get_domain(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc.startswith('www.'):
        return parsed_url.netloc[4:]
    else:
        return parsed_url.netloc

from .preprocessing import *
from .classifier import *
import pandas as pd
import numpy as np

def prediction(title, url):
    domain = get_domain(url)
    
    input_df = pd.DataFrame({'title': title, 'news_url': url, 'source_domain': domain}, index = ['1'])
    concat_df = pd.concat([load_datas(), input_df], ignore_index=True)

    input_df_tokenized = tokenize_datas(concat_df).tail(1)
    input_df_tokenized.drop("tweet_num", axis=1, inplace=True)
    input_df_tokenized.drop("real", axis=1, inplace=True)

    #return input_df_tokenized

    X, y = no_split_process()

    prediction, knn = knn_classifier(X, y, input_df_tokenized)

    return prediction

