import preprocessing
import classifier
import analysis

if __name__ == '__main__':
    print("Start learning... :)")

    df = preprocessing.load_datas()
    df.head(5)
