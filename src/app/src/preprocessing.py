import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

def process():
    df = load_datas()

    df = tokenize_datas(df)

    X, y = features_selection(df)

    X_train, X_test, y_train, y_test = split_df(X, y)

    return X_train, X_test, y_train, y_test 

def no_split_process():
    df = load_datas()

    df = tokenize_datas(df)

    X, y = features_selection(df)

    return X, y

def load_datas():
    return pd.read_csv("../../datas/FakeNewsNet.csv")

def tokenize_datas(df):
    le = LabelEncoder()
    label = le.fit_transform(df['news_url'])
    label1=le.fit_transform(df['title'])
    label2=le.fit_transform(df['source_domain'])
    df.drop("news_url", axis=1, inplace=True)
    df.drop("title", axis=1, inplace=True)
    df.drop("source_domain", axis=1, inplace=True)

    df["news_url"] = label
    df["title"] = label1
    df["source_domain"] = label2

    return df

def features_selection(df):
    features = ["title", "news_url", "source_domain"]

    return df[features].fillna(''),  df["real"]


def split_df(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.30, random_state=42)
    return X_train, X_test, y_train, y_test

