[![Build Status](https://codefirst.iut.uca.fr/api/badges/PyPloteam/PlotaFakeNews/status.svg)](https://codefirst.iut.uca.fr/PyPloteam/PlotaFakeNews)

### Built with

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

# Fake News Detector

## Getting started

Clone repo:

```shell
git clone https://codefirst.iut.uca.fr/git/PyPloteam/PlotaFakeNews.git
```

Install requirements using:

```shell
pip install -r requirements.txt
```

## Training script

```shell
cd src/
```

```shell
python3 main.py
```

## Launch web app

```shell
cd src/app/
```

```shell
python3 manage.py runserver
```

## Dataset informations

[FakeNews Dataset](https://www.kaggle.com/datasets/algord/fake-news)

| **title** | **news_url** | **source_domain** | _tweet_num_ | **real** |
|---|---|---|---|---|
| title of the article | URL of the article | web domain where article was posted | _number of retweets for this article_ | 1 is real and 0 is fake |

_(N.B. Italic columns are not used for learning models)_

## References

- [scikit-learn models](https://scikit-learn.org/stable/supervised_learning.html)

- [Label encoder _with scikit-learn_](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)

- [Django documentation](https://www.djangoproject.com/en/5.0/)

- [Provenance](https://github.com/KaiDMML/FakeNewsNet)

## Authors

[LIVET Hugo](https://codefirst.iut.uca.fr/git/hugo.livet)

[DE LA FUENTE Axel](https://codefirst.iut.uca.fr/git/axel.de_la_fuente)

## Acknowledgements

Thanks to our professor for his guidance and feedback throughout the development of this project.

- SAMIR Chafik